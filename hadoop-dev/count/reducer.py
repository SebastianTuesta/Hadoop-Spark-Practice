#!/opt/conda/bin python
# -*-coding:utf-8 -*
import sys
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 

current_word = None
acum = 0
word = None

for line in sys.stdin:
    word, count = line.split('\t')
    count = int(count)

    if current_word is None:
        current_word = word
        acum = count
    elif current_word == word:
        acum += count
    else:
        print(f'{current_word}\t{acum}')
        current_word = word
        acum = count

if word is not None:
    print(f'{current_word}\t{acum}')