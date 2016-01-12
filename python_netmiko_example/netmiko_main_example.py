#!/usr/bin/python

from netmiko import ConnectHandler
from DEVICE_CREDS import *
# DEVICE_CREDS.py is just a dictionary which represts the devices' properties
# can use "dir()" to check imported directories

cisco_conn = ConnectHandler(**cisco_881) # make ssh connections to devices listed in DEVICE_CREDS.py
arista_conn = ConnectHandler(**arista_veos_sw)
hp_conn = ConnectHandler(**hp_procurve)

cisco_conn.enable()
# after connect to devices successfully, for example, to cisco_881
# user "find_prompt()" method to check the cisco CLI status:
# (in python interface)
#   >>> cisco_conn.find_prompt()
#   >>> 'cisco_881> '
#
# Then user "enable()" method to enter the privilege-level CLI:
# (in python interface)
#   >>> cisco_conn.enble()
#   >>> cisco_conn.filename_upper_camelnd_prompt()
#   >>> 'cisco_881# '

show_output = cisco_conn.send_command("show ip int bri")
print (show_output)
# Using "send_command(<cli command>)" method to send CLI commands (which will
# not change the configuration) to devices remotely

show_output = cisco_conn.send_command("show ip rou | in 10.10.0.0")
print (show_output)

cmd_int = ['interface e1/1', 'switch mode access', 'switch access vlan 10', 'show vlan | in e1/1']
show_output = cisco_conn.send_config_set(cmd_int)
print (show_outpu)
# Using "send_config_set()" method to send CLI commands (which will change the
# configutation) to devices, and this will force the device entering config-mode
# Also, using a list to store many commands, and pass it to "send_command()" method

