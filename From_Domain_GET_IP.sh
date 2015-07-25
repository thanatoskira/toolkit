#!/bin/bash
for line in `cat  Domain_result.txt`
do
    echo -ne $line "\t\t"
    ping $line -c 2 -w 1| grep PING | awk '{print $3}' | sed 's/[()]//g'
done
