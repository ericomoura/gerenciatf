#! /bin/bash

apt-get update
apt-get install iputils-ping
apt-get install gcc

wget https://github.com/ossec/ossec-hids/archive/3.1.0.tar.gz -P /tmp
cd /tmp
tar xzf 3.1.0.tar.gz
cd ossec-hids-3.1.0
./install.sh