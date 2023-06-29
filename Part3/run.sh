#!/bin/bash    
hadoop jar hadoop-streaming-3.1.4.jar \
-D mapred.reduce.tasks=3 \
-D map.output.key.field.separator=: \
-D mapred.text.key.partitioner.options=-k1,2 \
-file ./mapper.py \
-mapper "./mapper1.py 2 3 3 2" \
-file ./reducer.py \
-reducer ./reducer.py \
-input /input \
-output /output \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner