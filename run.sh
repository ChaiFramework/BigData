#!/bin/bash    
hadoop jar ../hadoop-streaming-3.1.4.jar \
-D mapred.reduce.tasks=3 \
-file ./mapper.py \
-mapper ./mapper.py \
-file ./reducer.py \
-reducer ./reducer.py \
-input /3littlepigs.txt \
-output /output







