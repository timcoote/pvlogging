# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|

    config.ssh.forward_agent=true

    user = "vagrant"


  config.vm.define "sut" do |sut|

    # attempt to get nfs sync folders, does not work:
    # sut.vm.network "private_network", type: "dhcp"
#    sut.vm.network "public_network", bridge: "en0: Wi-Fi (Wireless)"  # use external dhcp so that other rfc 1918 machines can be reached. device name changed on new macbook
# port forwarding should r-studio be required for debugging
    sut.vm.network "forwarded_port", guest: 80, host: 8080
    sut.vm.network "forwarded_port", guest: 8787, host: 8787 
    sut.vm.network "forwarded_port", guest: 5901, host: 5902 
    sut.vm.network "forwarded_port", guest: 3838, host: 3838 
    sut.vm.hostname = 'R-on-fedora'

    sut.vm.provider :virtualbox do |vb|
     config.vm.box = "fedora/32-cloud-base"
     # more up to date?
     # still fails config.vm.box = "bento/fedora-30"
     #config.vm.box = "bento/fedora-28"
     # really?
     sut.vm.box_url = "file://../remote-mercury/output-vagrant/package.box"
     vb.customize ["modifyvm", :id, "--memory", "3096"]
     vb.customize ["modifyvm", :id, "--cpus", "3"]
     # does not work. Possibly issue with bridged public nic?
#     config.vm.synced_folder ".", "/vagrant", type: "rsync", rsync__exclude: [ ".git/", "./output-vagrant"]
    end
 

# required on vm to enable copying up to S3. This assumes that the user has valid AWS credentials in ~/.aws/credentials
    sut.vm.provision "file", source: "~/.aws/credentials", destination: "/home/#{user}/.aws/credentials"

    sut.vm.provision "shell", inline: <<-SHELL
       dnf install -y qemu-system-aarch64 rake buildah podman qemu-user-static rpmdevtools
       sudo systemctl restart systemd-binfmt # required after installing qemu-user-static to use interpreter on relevant binaries

# not needed for rpm builds, just if there's a need to spin up R/Rstudio
#       dnf install -y rstudio-server rake # R-shiny
#       dnf install -y libxml2-devel alsa-lib libXcomposite tigervnc-server fontconfig R libcurl-devel openssl-devel R-devtools rpmdevtools
# may need to invoke install.shiny-server, or equiv
    SHELL
  end


end
