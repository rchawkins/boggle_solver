#!/usr/bin/env python

import sys

MIN_WORD_SIZE = 3


with open('/usr/share/dict/words', 'r') as f:
    DICTIONARY = { w.strip().lower() for w in f if not w.istitle() and len(w) > 2 }


class TrieNode(object):
    def __init__(self, parent, c, prefix):
        self.parent = parent
        self.is_word = True if prefix in DICTIONARY else False
        self.char = c
        self.prefix = prefix
        self.children = {}


    def __str__(self):
        return '<TrieNode({}) char: {} prefix: {} is_word: {}>'.format(id(self),
                                                                       self.char,
                                                                       self.prefix,
                                                                       self.is_word)

class Trie(object):
    def __init__(self, source):
        self.root = TrieNode(None, None, None)

        self._build(source)

    def _build(self, string_list):
        for word in string_list:
            node = self.root

            if word[0] not in node.children:
                node.children[word[0]] = TrieNode(node, word[0], word[0])

            for i, c in enumerate(word, 1):
                if c not in node.children:
                    node.children[c] = TrieNode(node, c, word[0:i])
                node = node.children[c]
        return self.root


    def find(self, prefix):
        node = self.root
        for i in prefix:
            try:
                node = node.children[i]
            except KeyError:
                return False

        return node


    def dump(self, node=None):
        node = self.root if not node else node

        if not node:
            node = self.root

        for n in node.children.values():
            if n:
                print n
                self.dump(n)


def next_moves(board, prefix_list):
    """
    returns a list of (position, char) tuples containing valid moves, excluding
    positions already considered
    """
    (row_count, col_count) = board_dimensions(board)

    moves = []
    curr_row = prefix_list[-1][0][0]
    curr_col = prefix_list[-1][0][1]
    for row in (-1, 0, 1):
        for col in (-1, 0, 1):
            new_row = curr_row + row
            new_col = curr_col + col
            if (0 <= new_row < row_count and
                0 <= new_col < col_count and
                (new_row, new_col) not in [ i[0] for i in prefix_list ]):
                moves.append(((new_row, new_col), board[new_row][new_col]))

    return moves


def positions_to_prefix(prefix_list):
    """
    Convert a list of (position, char) tuples to a prefix string:

    [((0,0), 'f'), ((0,1), 'o'), ((0,2), 'o')] ==> 'foo'
    """
    return ''.join([ i[1] for i in prefix_list ])


def format_board(board):
    (row_count, col_count) = board_dimensions(board)
    rep = ''

    rep += ('-' + ('----' * col_count) + '\n')
    for row in board:
        rep += '| ' +  ' | '.join(row)     + ' |\n'
        rep += ('-' + ('----' * col_count) + '\n')
    return rep


def board_dimensions(board):
    return (len(board), len(board[0]))


if '__main__' == __name__:

    board = '''itsaw
               mitgn
               etpbe
               cvijh'''.split()

    (row_count, col_count) = board_dimensions(board)

    print
    print format_board(board)
    print

    letters = ''.join([ i for i in board ])

    # restrict word list to words using only letters in 'board'
    possible_words = { w for w in DICTIONARY if not [ i for i in w if i not in letters]}

    prefix_trie = Trie(possible_words)

    # seed with all possible starting positions
    positions = [ [((r,c), board[r][c]),] for r in range(0, row_count) for c in range(0, col_count) ]

    found_words = []

    while positions:
        path = positions.pop()
        candidate_prefix = positions_to_prefix(path)
        node = prefix_trie.find(candidate_prefix)

        if not node:
            continue

        if node.is_word and len(node.prefix) >= MIN_WORD_SIZE:
            found_words.append(node.prefix)

        for pos in next_moves(board, path):
            next_move = list(path) # list copy
            next_move.append(pos)
            positions.append(next_move)

    print sorted(set(found_words), key=lambda x: (-len(x), x))
