#!/usr/bin/env bash

# Update
echo "Updating Apt"
 sudo apt-get update -qq

echo "Upgrading Packages..."
sudo apt-get upgrade -qq

# Packages
echo "Installing the packages we need :)"
sudo apt-get install -y -qq git \
						python-dev \
						python-pip \

# Setup virtual environment
sudo pip install virtualenvwrapper

echo 'Configuring Python Virtual Environment'

echo 'export WORKON_HOME=$HOME/.virtualenvs' >> ~/.bashrc
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc

export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv working-title

echo 'cd /srv/project' >> ~/.bashrc
echo 'workon working-title' >> ~/.bashrc

# Sync Github
echo 'Cloning our awesome code repo!'
(cd /srv/project ;
 git config --global push.default simple
 pip install -r requirements.txt
)

DEV_PASSWORD='vagrant'

export DEBIAN_FRONTEND=noninteractive

sudo -E apt-get install -y mysql-server
sudo -E apt-get install -y mysql-client

if [ ! -d /var/lib/mysql/mywebsite ];
then
    echo "CREATE USER 'whats_next'@'localhost'" | mysql -u root
    echo "CREATE DATABASE whats_next" | mysql -u root
    echo "GRANT ALL ON whats_next.* TO 'whats_next'@'%'" | mysql -u root
    echo "flush privileges" | mysql -u root
fi

echo "Updating mysql configs in /etc/mysql/my.cnf."
sudo sed -i "s/bind-address.*/bind-address = 0.0.0.0/" /etc/mysql/my.cnf
echo "Updated mysql bind address in /etc/mysql/my.cnf to 0.0.0.0 to allow external connections."

echo "Assigning mysql user whats_next access on %."
sudo mysql -u root --execute "GRANT ALL PRIVILEGES ON *.* TO 'whats_next'@'%'; FLUSH PRIVILEGES;" whats_next
echo "Assigned mysql user whats_next access on all hosts."

sudo service mysql stop
sudo service mysql start

echo 'Done :) - Hopefully!'
