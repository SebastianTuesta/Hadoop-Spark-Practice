#!/opt/conda/bin python
# -*-coding:utf-8 -*
import sys
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 

import collections

counter = collections.Counter()

for line in sys.stdin:
    word, count = line.split('\t')
    count = int(count)

    counter[word] += count

for w in counter.most_common(2):
    print(f"{w[0]}\t{w[1]}")