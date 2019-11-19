#! /bin/bash

apt update
apt install -y nano
apt install -y net-tools
apt install -y wget
apt install -y git
apt install -y make
apt install -y autoconf autogen
apt install -y gcc

apt install -y libpcre3-dev libpcre3
apt install -y libyaml-dev
apt install -y liblognorm-dev liblognorm2
apt install -y libesmtp-dev
apt install -y libmaxminddb0 libmaxminddb-dev 

# apt install -y geoip-database-contrib geoipupdate
# cd /usr/local/share/GeoIP2
# sudo wget http://geolite.maxmind.com/download/geoip/database/GeoLite2-Country.tar.gz
# sudo gzip -d GeoLite2-Country.tar.gz

apt install -y libhiredis-dev
apt install -y libpcap-dev

git clone https://github.com/beave/sagan
cd sagan
./autogen.sh
./configure	#SYNTAX ERROR, INSTALLATION STUCK
make
make install