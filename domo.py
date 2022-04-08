#!/bin/python

import base64
import json
import os
import sys

import requests


class Domo:
    config_home = os.environ.get('DOMO_ROOT', os.path.expanduser('~') + '/.config/domo/')
    config_path = os.path.join(config_home + 'config.json')

    f = open(config_path)
    config = json.load(f)

    broadlink_config = config['broadlink']
    manager_url = broadlink_config['manager_url']
    command_url = manager_url + broadlink_config['command_endpoint']

    switchbot_token = config['switchbot']['token']

    def main(self):
        if len(sys.argv) <= 0:
            print('Command not defined')
            exit(1)

        device = sys.argv[1]

        if device == 'switchbot':
            command_to_send = ''
            commands = ''
        else:
            command_to_send = sys.argv[2]
            device_config = self.broadlink_config['devices'][device]
            commands = device_config['commands']

            for command_key in commands.keys():
                if command_to_send == command_key:
                    self.send_command(device_config, commands[command_to_send])

    def send_command(self, device_config, command):
        params = {
            'type': device_config['type'],
            'host': device_config['ip'],
            'mac': device_config['mac'],
            'command': (base64.b64decode(command)).hex()
        }
        requests.get(url=self.command_url, params=params)
        print('Done')


if __name__ == '__main__':
    Domo().main()
