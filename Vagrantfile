Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
    config.vm.network "forwarded_port", guest: 22, host: 2222
    config.vm.network "forwarded_port", guest: 15672, host: 15672
    config.vm.network "forwarded_port", guest: 4369, host: 4369
    config.vm.network "forwarded_port", guest: 5672, host: 5672
    config.vm.network "forwarded_port", guest: 5671, host: 5671
    config.vm.network "forwarded_port", guest: 25672, host: 25672
    config.vm.network "forwarded_port", guest: 35672, host: 35672
    config.vm.network "forwarded_port", guest: 35680, host: 35680
    config.vm.network "forwarded_port", guest: 35682, host: 35682
    config.vm.network "forwarded_port", guest: 61613, host: 61613
    config.vm.network "forwarded_port", guest: 1883, host: 1883
    config.vm.network "forwarded_port", guest: 8883, host: 8883
    config.vm.network "forwarded_port", guest: 15674, host: 15674
    config.vm.network "forwarded_port", guest: 15675, host: 15675
    config.vm.network "forwarded_port", guest: 19999, host: 19999
    config.vm.network "public_network", ip: "192.168.22.22"

    config.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
      vb.gui = false
    end
end
