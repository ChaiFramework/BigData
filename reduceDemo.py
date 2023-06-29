#!/usr/bin/env python3
import sys
s=0
int_count=[]
for line in sys.stdin:
    line = line.strip()
    taxiNum, count, kms = line.split('\t')

    for i in count:
        try:

            int_count.append(int(i))
        except:
            continue
    print(int_count)
    print('%s\t%s\t%s' % (taxiNum, sum(int_count), kms))
