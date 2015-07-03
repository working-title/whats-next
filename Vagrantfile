# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.network "forwarded_port", guest: 80, host: 8000

  config.vm.synced_folder ".", "/srv/project"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
  end
end
