#!/bin/bash

# Run leet.py
start=$(date +%s)
python3 python/run/leet.py
end=$(date +%s)
duration=$(( end - start ))
echo "leet.py execution time: $duration seconds"

# Run create_dic.py
start=$(date +%s)
python3 python/run/create_dic.py
end=$(date +%s)
duration=$(( end - start ))
echo "create_dic.py execution time: $duration seconds"

# Run breakhim.py
start=$(date +%s)
python3 python/run/breakhim.py
end=$(date +%s)
duration=$(( end - start ))
echo "breakhim.py execution time: $duration seconds"