# vmstats

## Setup environment 

### On Ubuntu install following dependencies

sudo apt-get update
sudo apt-get install rabbitmq
sudo apt-get install -y mongodb
sudo rabbitmq-plugins enable rabbitmq_management
sudo easy_install pika
sudo easy_install pymongo

### For other machines, please follow instructions from,
### https://www.rabbitmq.com/download.html
### http://docs.mongodb.org/manual/administration/install-on-linux/

### configurations are set in vm.config for utilization levels, mongo db url and rabbit parameters

## Execution

Please see simulation help using,

./simulate -h

Create Simulation environment for 100 VMs using,

./simulate -c 100 -r 10

### It will create 100 fake-qemu-kvm processes, 10 hypervisor channel listners and 10 RabbitMQ Queues.

Run Stat check collected for 100 Seconds using,

./vm-check -c 10 -i 10

### It will collect stats 10 time at the interval of 10 seconds. It will disply unused VMs

Note:
This excercise will create lots of processes for VM simulator and hypervisor communication clients. Please use larger machines to test  large number of VMs(> 1000). Also, larger VM simuation will take more time to start all fake processes and environment.

### Mongo data can be seen using,

###mongo
###> db.montior.find()

### Clean up: please run following command to remove all fake VMs.

pkill fake-qemu-kvm

### Clean up rabbitmq Queues using,

./rabbit-purge hypervisor

