django-docker-foundation-template
=============

Template for Django App + Foundation using Docker


Mac OS X  instructions
----------------------
(tested on mavericks)
vagrant, virtualbox and curl

Create and empty directory and run the following command in terminal:

    $ curl https://raw.github.com/zunayed/django_docker_foundation_template/master/Vagrantfile > Vagrantfile

then within the directory type 

    $ vagrant up

This should take a few minutes since its downloading a VM

    $ vagrant ssh

Then install git and curl on the VM:

    $ sudo apt-get install curl git

Now continue on to the linux instructions

Linux Instructions
------------------

clone my git repo:

    $ git clone https://github.com/zunayed/django_docker_foundation_template

now build the docker container With a tag for easier reuse

    $ sudo docker build  -t <your username>/django-docker django_docker_foundation_template

Running the container

    $ sudo docker run -d -p :8000 <your username>/django-docker

In the vagrantfile I have setup a port forwarding from the VM to your local machine for 8080.
Notice at the end of the vagrant file you will see this set up:

Vagrant.configure("2") do |config|
  config.vm.network "forwarded_port", guest: 8000, host: 8080,
    auto_correct: true
end
    

Dockerfile
----------
Use this to build a new image

    $ sudo docker build .

With a tag for easier reuse

    $ sudo docker build  -t <your username>/django-docker .

Running the container

    $ sudo docker run -d -p :8000 <your username>/django-docker
    
Get your container's IP Address:

    sudo docker inspect <container_id> | grep IPAddress | cut -d '"' -f 4

Now go to `<your container's ip>:8000` in your browser
