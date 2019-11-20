#! /bin/bash

apt update
apt install -y nano
apt install -y git
apt install -y net-tools
apt install -y openssh-server

apt install -y wget unzip make gcc build-essential
apt install -y php php-cli php-common libapache2-mod-php apache2-utils sendmail inotify-tools
wget https://github.com/ossec/ossec-hids/archive/3.1.0.tar.gz
tar -xvzf 3.1.0.tar.gz
cd ossec-hids-3.1.0
sh install.sh
/var/ossec/bin/ossec-control start

# git clone https://github.com/ossec/ossec-wui.git
# mv  ossec-wui /srv
# cd /srv/ossec-wui
# ./setup.sh
# nano /etc/apache2/sites-enabled/ossec-wui.conf

# <VirtualHost *:80>
#      DocumentRoot /srv/ossec-wui/
#      ServerName ossec.example.com
#      ServerAlias www.ossec.example.com
#      ServerAdmin admin@example.com
 
#      <Directory /srv/ossec-wui/>
#         Options +FollowSymlinks
#         AllowOverride All
#         Require all granted
#      </Directory>

#      ErrorLog /var/log/apache2/moodle-error.log
#      CustomLog /var/log/apache2/moodle-access.log combined
# </VirtualHost>

# a2enmod rewrite
# service apache2 restart
