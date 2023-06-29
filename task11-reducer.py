#!/usr/bin/env python3
import sys
currentTaxi = None
currentCount=0
distance=0
for line in sys.stdin:
    line = line.strip()
    taxiNum, count, kms= line.split('\t')
    try:
        kms=float(kms)
        count=int(count)
    except ValueError:
        continue
    if currentTaxi==taxiNum:
        currentCount+=count
        distance+=kms
    else:
        if currentTaxi:
               print('%s\t%s\t%s' % (taxiNum,currentCount,distance/currentCount))
        currentCount=count
        currentTaxi=taxiNum
        distance=kms
if currentTaxi==taxiNum:
    print('%s\t%s\t%s' % (taxiNum,count,distance/currentCount))
