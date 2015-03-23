# vmstats

Please see simulation help using,

./simulate -h

Create Simulation environment for 100 VMs using,

./simulate -c 100

### It will create 100 fake-qemu-kvm processes, hypervisor channel listners and RabbitMQ Queues.

Run Stat check collected for 10 minutes using,

./vm-check -c 10

Note:
This excercise will create lots of processes for VM simulator and hypervisor communication clients. Please don't test with large number of VMs(> 1000) is small machines with just 1-2 GB RAM.

### Clean up: please run following command to remove all fake VMs.

pkill fake-qemu-kvm

### Clean up rabbitmq Queues using,

python rabbit-purge hypervisor

