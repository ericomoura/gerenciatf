#! /bin/bash

if [ $1 -eq 1 ]
then
    echo '2013-11-01T10:01:04.600374-04:00 arrakis ossec-exampled[9123]: test connection from 192.168.1.1 via test-protocol1' >> /home/testlog.log

elif [ $1 -eq 2 ]
then
    echo 'May 22 02:13:22 localhost sshd[13949]: Accepted publickey for vagrant from 10.0.2.2 port 64565 ssh2: RSA SHA256:WeegtaAAFxNXdrRFSJfQ7Yc1sJQLOqYZTzr4uRjByyQ' >> /home/testlog.log

else
    echo Invalid argument
fi
