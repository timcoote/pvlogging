# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|

    config.ssh.forward_agent=true

    user = "vagrant"


  config.vm.define "sut", autostart: false do |sut|

    # attempt to get nfs sync folders, does not work:
    # sut.vm.network "private_network", type: "dhcp"
#    sut.vm.network "public_network", bridge: "en0: Wi-Fi (Wireless)"  # use external dhcp so that other rfc 1918 machines can be reached. device name changed on new macbook
    sut.vm.network "forwarded_port", guest: 8787, host: 8787 
    sut.vm.hostname = 'R-on-fedora'

    sut.vm.provider :virtualbox do |vb|
     config.vm.box = "fedora/32-cloud-base"
     #sut.vm.box = "test-mercury-baseline"
     sut.vm.box_url = "file://../remote-mercury/output-vagrant/package.box"
     #vb.customize ["modifyvm", :id, "--memory", "1024"]
     vb.customize ["modifyvm", :id, "--memory", "2048"]
     vb.customize ["modifyvm", :id, "--cpus", "3"]
     # does not work. Possibly issue with bridged public nic?
     config.vm.synced_folder ".", "/vagrant", type: "rsync", rsync__exclude: [ ".git/", "./output-vagrant"]
    end
 

# required on vm to enable copying up to S3. This assumes that the user has valid AWS credentials in ~/.aws/credentials
    sut.vm.provision "file", source: "~/.aws/credentials", destination: "/home/#{user}/.aws/credentials"

    sut.vm.provision "shell", inline: <<-SHELL
       systemctl restart postsrsd
#       cd /vagrant && rake deploy
       dnf install -y rstudio-server R-shiny
       dnf install -y R-Rcpp-devel 
    SHELL
  end


end
