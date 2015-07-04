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

export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv working-title

if [ ! -f ~/.edittedbashrc ]
then
	echo 'export WORKON_HOME=$HOME/.virtualenvs' >> ~/.bashrc
	echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc

	echo 'cd /srv/project' >> ~/.bashrc
	echo 'workon working-title' >> ~/.bashrc


	# alias
	echo 'export PROJECT=/srv/project' >> ~/.bashrc
	echo 'alias m="python $PROJECT/manage.py"' >> ~/.bashrc
	echo 'alias dmigrate="m migrate"' >> ~/.bashrc
	echo 'alias update="pip install -r $PROJECT/requirements.txt"' >> ~/.bashrc
	echo 'alias drun="m runserver 0.0.0.0:8000"' >> ~/.bashrc
	echo 'alias dshell="m shell_plus"' >> ~/.bashrc

	touch ~/.edittedbashrc
fi

# Sync Github
echo 'Cloning our awesome code repo!'
(cd /srv/project ;
 git config --global push.default simple
 pip install -r requirements.txt
)

echo 'Done :) - Hopefully!'
