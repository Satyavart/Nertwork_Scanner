Network Scanner

A simple python program for scaning and fetching all the devices connected to network you are connected to.

1. !st use "route -n" to check IP of the network you are connected to.
2. Then use


		python Network_Scanner.py -t 172.17.28.1/24   

		"/24" is used to search for all network within the subnet.
