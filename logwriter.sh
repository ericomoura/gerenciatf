#! /bin/bash

if [ $1 -eq 1 ]
then
    echo 2013-11-01T10:01:04.600374-04:00 arrakis ossec-exampled[9123]: test connection from 192.168.1.1 via test-protocol1 >> /home/testlog.log
else
    echo Invalid argument
fi
