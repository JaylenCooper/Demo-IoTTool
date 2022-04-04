#!/bin/python

import base64
import os
import sys

import requests

manager_url = 'http://localhost:7020/'
command_url = manager_url + 'command/send/'

device_type = os.environ.get('BL_DEVICE_TYPE')
device_ip = os.environ.get('BL_DEVICE_IP')
device_mac = os.environ.get('BL_DEVICE_MAC')

soundbar_volume_up = "JgBIAAABLJUUERURFREUERURFREUEhQ2FDYUNhI4FDUVNRU1FTUVERQRFREVERQ2FBEVERURFBIUNhQ2FDYUERU1FTUVNRU2FAANBQAAAAAAAAAAAAAAAAAA"
soundbar_volume_down = "JgCQAAABLZQUERURFREUEhQSFBEVERU1FTYUNhQ2FDYUNhQ2FDYUEhQ2FBEVNhQ2FREUEhQSFBIUEhQ2FREVERQ2FDYUNhQ2FAAFKAABL5QSExURFBIUEhUQFREVERU1EzcTNxM3EzcSOBI4EjgSExQ2ExMUNhI4EhMVERQRFREVERU1FREUEhQ2FDYUNhQ2FAANBQAAAAAAAA=="
soundbar_mute = "JgCQAAABLpMUERURFREVERQSFBEVERU1FTUVNRU1FTUVNRU1FTUUEhQRFTUVNRU1FTUVERQSFBEVNRURExMUERURFTUVNRU1FQAFKAABL5MVERQRFREVERQSFBEVERU1FTUVNRU1FTYUNhQ2FDYUEhQRFTUVNRU1FTUVERQSFBIUNhQRFREVERURFDYUNhU1FQANBQAAAAAAAA=="
soundbar_power = "JgCQAAABLZMVERQRFREVERURFBIUERU2FDYUNRU2FDYUNhQ2FDUVERURFDYUEhQRFTYUERURFBIUNhQSFDYUNhQRFTUVNRU1FQAFJwABL5MVERQRFREVERQRFREVERU1FTUUNhQ2FDYUNhQ2FDUVERURFDYUERURFTUVERQSFBEVNRURFDYUNhQRFTYUNRU1FQANBQAAAAAAAA=="

commands = {
    'volume_up': soundbar_volume_up,
    'volume_down': soundbar_volume_down,
    'mute': soundbar_mute,
    'unmute': soundbar_mute,
    'sound_on': soundbar_power,
    'sound_off': soundbar_power
}

if not device_type or not device_ip or not device_mac:
    print('Device environment variables not defined')
    exit(1)

if len(sys.argv) <= 0:
    print('Command not defined')
    exit(1)

command_to_send = sys.argv[1]


def send_command(command):
    params = {
        'type': device_type,
        'host': device_ip,
        'mac': device_mac,
        'command': (base64.b64decode(command)).hex()
    }

    r = requests.get(url=command_url, params=params)
    print(r.json())


for command_key in commands.keys():
    if command_to_send == command_key:
        send_command(commands[command_to_send])
