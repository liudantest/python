#!bin/bash
cat subscriber_info.log|grep 'receive IM message' > rec.log
python3 loganalysis.py
