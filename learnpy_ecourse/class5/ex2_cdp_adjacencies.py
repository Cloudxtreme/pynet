#!/usr/bin/env python
'''

Disclaimer - This is a solution to the below problem given the content we have
discussed in class.  It is not necessarily the best solution to the problem.
In other words, I generally only use things we have covered up to this point
in the class (with some exceptions which I will usually note).

Python for Network Engineers
https://pynet.twb-tech.com
Learning Python


Create a second program that expands upon the program from Exercise I.

This program will keep track of which network devices are
physically adjacent to each other (physically connected to each
other).

You will accomplish this by adding a new field (adjacent_devices)
to your network_devices inner dictionary.  adjacent_devices will be a
list of hostnames that a given network device is physically
connected to.

For example, the dictionary entries for 'R1' and 'SW1' should look
as follows:

'R1': {'IP': '10.1.1.1',
        'adjacent_devices': ['SW1'],
        'device_type': 'Router',
        'model': '881',
        'vendor': 'Cisco'},
'SW1': {'IP': '10.1.1.22',
         'adjacent_devices': ['R1', 'R2', 'R3', 'R4', 'R5'],
         'device_type': 'Switch',
         'model': 'WS-C2950-24',
         'vendor': 'cisco'},


For output, print network_devices to standard output.

'''

import pprint
import sys

sw1_show_cdp_neighbors = '''

SW1>show cdp neighbors

Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R1           Fas 0/11        153           R S I           881          Fas 1
R2           Fas 0/12        123           R S I           881          Fas 1
R3           Fas 0/13        129           R S I           881          Fas 1
R4           Fas 0/14        173           R S I           881          Fas 1
R5           Fas 0/15        144           R S I           881          Fas 1

'''

sw1_show_cdp_neighbors_detail = '''

SW1> show cdp neighbors detail
--------------------------
Device ID: R1
Entry address(es):
   IP address: 10.1.1.1
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/11, Port ID (outgoing port): FastEthernet1
Holdtime: 153 sec

Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team

advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):

--------------------------
Device ID: R2
Entry address(es):
   IP address: 10.1.1.2
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/12, Port ID (outgoing port): FastEthernet1
Holdtime: 123 sec

Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team

advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):

--------------------------
Device ID: R3
Entry address(es):
   IP address: 10.1.1.3
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/13, Port ID (outgoing port): FastEthernet1
Holdtime: 129 sec

Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team

advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):

--------------------------
Device ID: R4
Entry address(es):
   IP address: 10.1.1.4
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/14, Port ID (outgoing port): FastEthernet1
Holdtime: 173 sec

Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team

advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):

--------------------------
Device ID: R5
Entry address(es):
   IP address: 10.1.1.5
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/15, Port ID (outgoing port): FastEthernet1
Holdtime: 144 sec

Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team

advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):

'''

r1_show_cdp_neighbors = '''

R1>show cdp neighbors 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/11

'''

r1_show_cdp_neighbors_detail = '''

R1>show cdp neighbors detail 
-------------------------
Device ID: SW1
Entry address(es): 
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP 
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/11
Holdtime : 145 sec

Version :
Cisco Internetwork Operating System Software 
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu

advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full

'''

r2_show_cdp_neighbors = '''

R2>show cdp neighbors 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/12

'''

r2_show_cdp_neighbors_detail = '''

R2>show cdp neighbors detail 
-------------------------
Device ID: SW1
Entry address(es): 
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP 
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/12
Holdtime : 145 sec

Version :
Cisco Internetwork Operating System Software 
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu

advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full

'''

r3_show_cdp_neighbors = '''

R3>show cdp neighbors 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/13

'''

r3_show_cdp_neighbors_detail = '''

R3>show cdp neighbors detail 
-------------------------
Device ID: SW1
Entry address(es): 
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP 
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/13
Holdtime : 145 sec

Version :
Cisco Internetwork Operating System Software 
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu

advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full

'''

r4_show_cdp_neighbors = '''

R4>show cdp neighbors 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/14

'''

r4_show_cdp_neighbors_detail = '''

R4>show cdp neighbors detail 
-------------------------
Device ID: SW1
Entry address(es): 
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP 
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/14
Holdtime : 145 sec

Version :
Cisco Internetwork Operating System Software 
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu

advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full

'''

r5_show_cdp_neighbors = '''

R5>show cdp neighbors 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/15

'''

r5_show_cdp_neighbors_detail = '''

R5>show cdp neighbors detail 
-------------------------
Device ID: SW1
Entry address(es): 
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP 
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/15
Holdtime : 145 sec

Version :
Cisco Internetwork Operating System Software 
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu

advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full

'''


# Use show cdp neighbor detail output
cdp_neighbors = (
    sw1_show_cdp_neighbors_detail,
    r1_show_cdp_neighbors_detail,
    r2_show_cdp_neighbors_detail,
    r3_show_cdp_neighbors_detail,
    r4_show_cdp_neighbors_detail,
    r5_show_cdp_neighbors_detail,
)

network_devices = {}


# Iterate over each cdp_neighbor_details string
for cdp_data in cdp_neighbors:

    # Break the cdp neighbor data up into lines
    cdp_data_line = cdp_data.split("\n")

    # Reset hostname for each cdp output
    remote_hostname = ''
    local_hostname = ''

    # Iterate over each line of the cdp data
    for line in cdp_data_line:

        # As a precaution set remote_hostname to '' on every device divider
        if '----------------' in line:
            remote_hostname = ''

        # Find local hostname (assumes no abbreviation in command)
        if 'show cdp neighbors detail' in line:
            local_hostname = line.split("show cdp neighbors detail")[0]
            if '>' in local_hostname:
                local_hostname = local_hostname.split('>')[0]
            elif '#' in local_hostname:
                local_hostname = local_hostname.split('#')[0]
            else:
                sys.exit("Invalid prompt for local hostname - exiting")

            # When you find a new device, initialize it as a blank dictionary
            if not local_hostname in network_devices:
                network_devices[local_hostname] = {}


        # Processing hostname
        if 'Device ID: ' in line:
            (junk, remote_hostname) = line.split('Device ID: ')
            remote_hostname = remote_hostname.strip()

            # When you find a new device, initialize it as a blank dictionary
            if not remote_hostname in network_devices:
                network_devices[remote_hostname] = {}


            # Map adjacencies
            if (local_hostname in network_devices) and remote_hostname:

                # Add adjacent_devices field if it doesn't exist
                if not 'adjacent_devices' in network_devices[local_hostname]:
                    network_devices[local_hostname]['adjacent_devices'] = [remote_hostname]

                # adjacent_devices is already present, append to it
                else:

                    # Add the remote device (if not already on list)
                    if not remote_hostname in network_devices[local_hostname]['adjacent_devices']:
                        network_devices[local_hostname]['adjacent_devices'].append(remote_hostname)


        # Processing IP
        if 'IP address: ' in line:
            (junk, ip) = line.split('IP address: ')
            ip = ip.strip()

            if remote_hostname:
                network_devices[remote_hostname]['ip'] = ip

        # Process vendor, model, and device_type
        if 'Platform: ' in line:

            (platform, capabilities) = line.split(',')

            # Process vendor and model
            (junk, model_vendor) = platform.split("Platform: ")
            (vendor, model) = model_vendor.split()

            # Process device_type
            (junk, capabilities) = capabilities.split("Capabilities: ")
            if 'Router' in capabilities:
                device_type = 'router'
            elif 'Switch' in capabilities:
                device_type = 'switch'
            else:
                device_type = 'unknown'

            if remote_hostname:
                network_devices[remote_hostname]['vendor'] = vendor
                network_devices[remote_hostname]['model'] = model
                network_devices[remote_hostname]['device_type'] = device_type



print '\n'
pprint.pprint(network_devices)
print '\n'

