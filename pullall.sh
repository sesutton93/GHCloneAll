#!/bin/bash
cd ..
#python clone_all/repolist.py --u username --p password -d #| 
python clone_all/repolist.py --t token -d |
while read url; do
  git clone $url &
done 
wait
echo "all jobs done"

