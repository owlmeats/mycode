#!/usr/bin/env python3

ipchk = input('Apply an IP address: ') # this line now prompts the user for input


#if ipchk:
#    print('Looks like the IP address was set: ' + ipchk)
#else: # if data is NOT provided: 
#    print('You did not provide any input.')



if ipchk == '192.168.70.1': # if a match on 192.168.70.1
    print('Looks like the IP address of the Gateway was set: ' + ipchk + ' This is not recommended.')
elif ipchk:  # if Any data is provided, this will test true
    print('Looks like the IP address was set: ' + ipchk )
else: # if data is NOT provided
    print('You did not provide input.') 


