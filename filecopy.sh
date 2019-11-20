#! /bin/bash

if [ $1 = "fromdocker" ]
then
    docker cp ubuntu:/var/ossec/rules/local_rules.xml ./local_rules.xml
    docker cp ubuntu:/var/ossec/etc/decoder.xml ./decoder.xml
    docker cp ubuntu:/var/ossec/etc/ossec.conf ./ossec.conf

elif [ $1 = "todocker" ]
then
    docker cp ./local_rules.xml ubuntu:/var/ossec/rules/local_rules.xml
    docker cp ./decoder.xml ubuntu:/var/ossec/etc/decoder.xml
    docker cp ./ossec.conf ubuntu:/var/ossec/etc/ossec.conf

else
    echo Invalid argument
fi
