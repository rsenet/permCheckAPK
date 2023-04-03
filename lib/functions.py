#!/usr/bin/env python3
import adbutils
import time
import sys


def get_connected_devices():
    """Return all connected devices
    """
    adb = adbutils.AdbClient(host="127.0.0.1", port=5037)

    return adb


def display_connected_device():
    """Display all connected devices
    """
    adb = get_connected_devices()

    for device in adb.list():
        print(f" - {device.serial}")


def check_device_exists(device):
    """Check if the specified device truly exists

    :param device: Device to audit
    """
    checked = False

    for element in get_connected_devices().device_list():
        if device in str(element):
            checked = True

    return checked


def show_device_info(device):
    """Display information regarding the device

    :param device: Device to audit
    """
    adb = get_connected_devices()
    d = adb.device(serial=device)

    print(f"[x] Getting information on {device} - {d.prop.device} ({d.prop.model})")


def get_user_installed_applications(device):
    """Retrieve the list of user installed applications

    :param device: Device to audit
    """
    appList = exec_command(device, "pm list packages -3")
    appList = appList.replace("package:", "")
    appList = appList.split("\n")

    return appList


def get_application_permission(device, application):
    """Retrieve the permission of the specified application

    :param device: Device to audit
    :param application: Application to audit
    """
    updated_perm = []
    permissions = exec_command(device, "appops get %s" % application)
    permissions = permissions.replace("Uid mode: ", "")
    permissions = permissions.split("\n")

    for permission in permissions:
        updated_perm.append(permission.split(":")[0])

    return updated_perm


def exec_command(device, cmd):
    """Execute a specific command on the specified device

    :param device: Device to audit
    :param cmd: Commande to execute
    """
    adb = get_connected_devices()
    d = adb.device(serial=device)

    return d.shell(cmd)

