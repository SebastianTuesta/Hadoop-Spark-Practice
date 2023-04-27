#!/opt/conda/bin python
# -*-coding:utf-8 -*
import sys
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 

for words in sys.stdin:
    # write the results to STDOUT (standard output);
    # what we output here will be the input for the
    # Reduce step, i.e. the input for reducer.py
    #
    # tab-delimited; the trivial word count is 1
    color, *others = words.split(',')
    if color != 'color':
        if color is None or color == '':
            color = 'None'
        print(f'{color}\t1')
