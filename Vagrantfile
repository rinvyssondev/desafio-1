
Vagrant.configure("2") do |config|

  config.vm.box = "centos/7"
  config.vm.disk :disk, size: "50GB", primary: true
  config.vm.network "forwarded_port", guest: 8888, host: 8888
  config.vm.define "teste-zeppelin" do |zep|
    zep.vm.network "public_network"
    zep.vm.provider "virtualbox" do |vb|
        vb.gui = false
        vb.name = "teste-zeppelin"
        vb.memory = "4096"
        vb.cpus = "2"
        #vb.disk :disk, size: "50GB", primary: true
    end
  end
end