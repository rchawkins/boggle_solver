boggle_solver
=============

Produces all possible words longer than 3 letters using the given board, printing them in order by length. The source word 
list is assumed to be available at '/usr/share/dict/words'.  The word list doesn't appear to include plurals, so longer
words are possible.

Sample output:

```
% ./boggle.py

---------------------
| i | t | s | a | w |
---------------------
| m | i | t | g | n |
---------------------
| e | t | p | b | e |
---------------------
| c | v | i | j | h |
---------------------


['astite', 'begnaw', 'bittie', 'henbit', 'pisang', 'ptisan', 'timist', 'tipiti', 'tisane', 'titbit', 'vectis', 'angst', 
'begat', 'metis', 'mitis', 'stage', 'stane', 'stang', 'stawn', 'stime', 'stite', 'tangs', 'vitta', 'agen', 'atip', 
'atis', 'bena', 'beng', 'bite', 'biti', 'bitt', 'ceti', 'emit', 'gane', 'gast', 'gawn', 'gena', 'gnat', 'gnaw', 'item', 
'jibe', 'jiti', 'jive', 'mist', 'mite', 'mitt', 'nasi', 'nast', 'piet', 'pist', 'pita', 'sage', 'sane', 'sang', 'sawn', 
'sime', 'site', 'stag', 'staw', 'stim', 'tane', 'tang', 'tawn', 'time', 'tite', 'titi', 'wage', 'wane', 'wang', 'wast', 
'watt', 'age', 'ast', 'awn', 'beg', 'ben', 'bit', 'gan', 'gas', 'gat', 'gaw', 'gen', 'hen', 'imi', 'ist', 'its', 'jib', 
'met', 'nag', 'nat', 'naw', 'neb', 'pie', 'pit', 'sag', 'san', 'sat', 'saw', 'sie', 'sip', 'sit', 'tag', 'tan', 'taw', 
'tec', 'tib', 'tie', 'tip', 'tit', 'tst', 'vei', 'vet', 'wag', 'wan', 'was', 'wat']
```
