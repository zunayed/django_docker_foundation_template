[Mac OS Install](#Mac) |
[Linux Instructions](#Linux) |
[Extra](#Extra) 

Django + Foundation inside a docker container
=============================================

Initial setup needs to download several hundred MBs. After the base vms and containers have been cached future setups should take only a few seconds.

Currently docker isn't nativly supported in Mac OS so we will run a VM layer to get the container up and running

<a name="Mac"/>
## Mac
(tested on mavericks)


You will need to have vagrant, virtualbox and curl installed

Create and empty directory and run the following command in terminal:

    $ curl https://raw.github.com/zunayed/django_docker_foundation_template/master/Vagrantfile > Vagrantfile

then cd within the directory 

    $ vagrant up

This should take a few minutes since it's downloading a VM

    $ vagrant ssh

Then install git and curl on the VM:

    $ sudo apt-get install curl git

Now continue on to the linux instructions

<a name="Linux"/>
## Linux

If you are on ubuntu make sure you install docker via the instructions on their website. If you are on mac os this has already been taken care of in the vagrant VM

clone my git repo:

    $ git clone https://github.com/zunayed/django_docker_foundation_template

now build the docker container with a tag. This may take a few minutes initially. 

    $ sudo docker build  -t <your username>/django-docker django_docker_foundation_template

Running the container

    $ sudo docker run -d -p :8000 <your username>/django-docker

If you go to a browser window and navigate to localhost:8080 you should see hello world


<a name="Extra"/>
## Extra

In the vagrantfile I have setup port forwarding from the VM to your local machine for 8080.
Notice at the end of the vagrant file you will see this set up:
```rb
Vagrant.configure("2") do |config|
  config.vm.network "forwarded_port", guest: 8000, host: 8080,
    auto_correct: true
end
```  

You can get your containers ip address 

    $ sudo docker inspect <container_id> | grep IPAddress

