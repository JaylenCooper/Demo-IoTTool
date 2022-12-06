#!/usr/bin/env python3

import base64
import hashlib
import hmac
import json
import os
import sys
import time
import requests
import tinytuya


def get_switchbot_auth_params(token, secret, nonce):
    t = int(round(time.time() * 1000))
    string_to_sign = '{}{}{}'.format(token, t, nonce)
    string_to_sign = bytes(string_to_sign, 'utf-8')
    secret = bytes(secret, 'utf-8')
    sign = base64.b64encode(hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())
    return str(sign, 'utf-8'), str(t), nonce


class Domo:
    def __init__(self, config_filepath):
        with open(config_filepath) as file:
            self.config = json.load(file)

        self.broadlink_config = self.config['broadlink']
        self.manager_url = self.broadlink_config['manager_url']
        self.command_url = self.manager_url + self.broadlink_config['command_endpoint']
        self.broadlink_devices = self.broadlink_config['devices']
    
        self.switchbot_config = self.config['switchbot']
        self.switchbot_devices = self.switchbot_config['devices']
        self.switchbot_base_url = self.switchbot_config['base_url']
        self.sign, self.t, self.nonce = get_switchbot_auth_params(
            self.switchbot_config['token'],
            self.switchbot_config['secret'],
            self.switchbot_config['nonce']
        )
        self.switchbot_headers = {
            'Content-type': 'application/json; charset=utf8',
            'Authorization': self.switchbot_config['token'],
            'sign': self.sign,
            't': self.t,
            'nonce': self.nonce
        }
    
        self.tuya_config = self.config['tuya']
        self.tuya_devices = self.tuya_config['devices']

    def main(self):
        if len(sys.argv) <= 0:
            print('Command not defined')
            exit(1)

        device = sys.argv[1]
        command = sys.argv[2]

        if device in self.broadlink_devices:
            self.send_broadlink_command(self.broadlink_devices[device], command)

        if device in self.switchbot_devices:
            self.send_switchbot_command(self.switchbot_devices[device], command)

        if device in self.tuya_devices:
            self.send_tuya_command(self.tuya_devices[device], command)

    def send_broadlink_command(self, device_config, command):
        commands = device_config['commands']
        if command in commands:
            params = {
                'type': device_config['type'],
                'host': device_config['ip'],
                'mac': device_config['mac'],
                'command': (base64.b64decode(commands[command])).hex()
            }
            requests.get(url=self.command_url, params=params)

    def send_switchbot_command(self, device_config, command):
        device_id = device_config['device_id']
        commands = device_config['commands']
        if command in device_config['commands']:
            command_url = self.switchbot_base_url + '/v1.1/devices/' + device_id + '/commands'
            data = {
                "command": commands[command],
                "parameter": "default",
                "commandType": "command"
            }
            requests.post(url=command_url, headers=self.switchbot_headers, data=json.dumps(data))

    def get_switchbot_devices(self):
        # Check documentation for more info: https://github.com/OpenWonderLabs/SwitchBotAPI#get-device-list
        devices = requests.get(url=self.switchbot_base_url + '/v1.1/devices', headers=self.switchbot_headers)
        devices = devices.json()['body']
        print(devices)

    @staticmethod
    def send_tuya_command(device_config, command):
        if command in device_config['commands']:
            device = tinytuya.OutletDevice(
                dev_id=device_config['id'],
                address=device_config['ip'],
                local_key=device_config['key'],
                version=device_config['ver'])

            if 'on' in command:
                device.turn_on()
            if 'off' in command:
                device.turn_off()


if __name__ == '__main__':
    config_home = os.environ.get('DOMO_ROOT', os.path.expanduser('~') + '/.config/domo/')
    config_path = os.path.join(config_home + 'config.json')
    domo = Domo(config_path)
    domo.main()
