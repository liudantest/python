#!bin/bash
cat subscriber_info.log|grep 'costtime=' > costtime.txt
cat costtime.txt|awk -F 'costtime=' '{print $2}'> result_costtime.txt
