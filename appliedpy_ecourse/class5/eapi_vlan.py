#!/usr/bin/env python
'''
Using Arista's eapilib, create a script that allows you to add a VLAN (both the
VLAN ID and the VLAN name).  Your script should first check that the VLAN ID is
available and only add the VLAN if it doesn't already exist.  Use VLAN IDs
between 100 and 999.  You should be able to call the script from the command
line as follows:

   python eapi_vlan.py --name blue 100     # add VLAN100, name blue

If you call the script with the --remove option, the VLAN will be removed.

   python eapi_vlan.py --remove 100          # remove VLAN100

Once again only remove the VLAN if it exists on the switch.  You will probably
want to use Python's argparse to accomplish the argument processing.

Note, in the lab environment, if you want to directly execute your script, you
will need to use '#!/usr/bin/env python' at the top of the script (instead of
'!#/usr/bin/python').
'''

import eapilib
import jsonrpclib
import argparse


def check_vlan_exists(eapi_conn, vlan_id):
    '''
    Check if the given VLAN exists

    Return either vlan_name or False
    '''

    vlan_id = str(vlan_id)
    command_str = 'show vlan id {}'.format(vlan_id)
    commands = [command_str]

    try:
        response = eapi_conn.run_commands(commands)
        check_vlan = response[0]['vlans']
        if check_vlan.get(vlan_id) is not None:
            vlan_name = check_vlan[vlan_id]['name']
            return vlan_name

    except jsonrpclib.jsonrpc.ProtocolError:
        pass

    return False


def configure_vlan(eapi_conn, vlan_id, vlan_name=None):
    '''
    Add the given vlan_id to the switch

    Set the vlan_name (if provided)

    Note, if the vlan already exists, then this will just set the vlan_name
    '''

    command_str1 = 'vlan {}'.format(vlan_id)
    commands = [command_str1]
    if vlan_name is not None:
        command_str2 = 'name {}'.format(vlan_name)
        commands.append(command_str2)

    return eapi_conn.config(commands)


def main():
    '''
    Add/remove vlans from Arista switch in an idempotent manner
    '''

    arista_dict = dict(
        hostname='10.10.10.10',
        port=8243,
        username='username',
        password='********'
    )

    eapi_conn = eapilib.create_connection(**arista_dict)

    # Argument parsing
    parser = argparse.ArgumentParser(
        description="Idempotent addition/removal of VLAN to Arista switch"
    )
    parser.add_argument("vlan_id", help="VLAN number to create or remove", action="store", type=int)
    parser.add_argument(
        "--name",
        help="Specify VLAN name",
        action="store",
        dest="vlan_name",
        type=str
    )
    parser.add_argument("--remove", help="Remove the given VLAN ID", action="store_true")

    cli_args = parser.parse_args()
    vlan_id = cli_args.vlan_id
    remove = cli_args.remove
    vlan_name = cli_args.vlan_name

    # Check if VLAN already exists
    check_vlan = check_vlan_exists(eapi_conn, vlan_id)

    # check if action is remove or add
    if remove:
        if check_vlan:
            print "VLAN exists, removing it"
            command_str = 'no vlan {}'.format(vlan_id)
            eapi_conn.config([command_str])
        else:
            print "VLAN does not exist, no action required"

    else:

        if check_vlan:
            if vlan_name is not None and check_vlan != vlan_name:
                print "VLAN already exists, setting VLAN name"
                configure_vlan(eapi_conn, vlan_id, vlan_name)
            else:
                print "VLAN already exists, no action required"

        else:
            print "Adding VLAN including vlan_name (if present)"
            configure_vlan(eapi_conn, vlan_id, vlan_name)


if __name__ == "__main__":

    main()

