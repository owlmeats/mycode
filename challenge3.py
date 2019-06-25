#!/usr/bin/env python3


hosts = [{"server": "North", "ip": "10.1.2.3"}, {"server": "South", "ip": "10.4.5.6"}, {"server": "West", "ip": "10.7.8.9"}]

# Your task is to add a fourth server:ip dictionary with the values of "East", and "10.10.11.12" to this list.
# THEN, Print out each server and it's IP.


hosts.append({"server": "East", "ip": "10.10.11.12"})
#print(hosts)
#print(hosts[0]["server"], hosts[0]["ip"])
#print(hosts[1]["server"], hosts[1]["ip"])
#print(hosts[2]["server"], hosts[2]["ip"])
#print(hosts[3]["server"], hosts[3]["ip"])


#basic = [1, 2, 3, 4, 5]
# old way = print(basic[0])
#for item in basic:
#    print(item)
#    print(item + 10)



# for loop over list of dictionaries
for info in hosts:
    print(info['server'])

