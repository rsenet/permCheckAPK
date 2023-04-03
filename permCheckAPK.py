#!/usr/bin/env python3
from lib.functions import *
import argparse

__author__  = 'Regis SENET'
__email__   = 'regis.senet@orhus.fr'
__git__     = 'https://github.com/rsenet/permcheckapk'
__version__ = '0.1'
short_desc  = "Android Application Permission Checker"

arg_parser = argparse.ArgumentParser(description=short_desc)
arg_parser.add_argument('--device', help="Specify the device")
arg_parser.add_argument('--list', action='store_true', help="List all user installed applications")
arg_parser.add_argument('--perm', help="Return applications with the specified permission")
u_args = arg_parser.parse_args()
device = u_args.device
listapp = u_args.list
permcheck = u_args.perm

try:
    if not u_args.device:
        print("[x] Please specify the device (--device)")
        display_connected_device()

    else:
        if check_device_exists(device):
            # Get device info
            if listapp:
                print("[x] User Installed Application on %s" % device)
                for application in get_user_installed_applications(device):
                    print(" - %s" % application)

            # Get all permission on all user installed applications
            else:
                if not permcheck:
                    for application in get_user_installed_applications(device):
                        print("\n[x] '%s' has the following permission" % application)
                        for permission in get_application_permission(device, application):
                            print(" - %s" % permission.split(":")[0])

                else:
                    for application in get_user_installed_applications(device):
                        permissions = get_application_permission(device, application)

                        if permcheck in permissions:
                            print("\n[x] '%s' has the following permission" % application)

                            for permission in permissions:
                                print(" - %s" % permission.split(":")[0])

        else:
            print("[x] Device does not exists - Leaving")

except KeyboardInterrupt:
    print("[x] Leaving")