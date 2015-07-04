# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
  end

  # Django
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  # MySQL
  config.vm.network "forwarded_port", guest: 3306, host: 3306

  config.vm.synced_folder ".", "/srv/project"

  config.vm.provision :shell, path: "setup.sh", privileged: false
end
