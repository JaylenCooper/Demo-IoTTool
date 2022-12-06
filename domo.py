#!/bin/python

import base64
import hashlib
import hmac
import json
import os
import sys
import time

import requests
import tinytuya


# More information about tuya check both: https://pypi.org/project/tinytuya/ and https://eu.iot.tuya.com/
# Scan tuya devices using:
# python -m tinytuya scan
# Then check the snapshot.json created file

def get_switchbot_auth_params(token, secret, nonce):
    t = int(round(time.time() * 1000))
    string_to_sign = '{}{}{}'.format(token, t, nonce)
    string_to_sign = bytes(string_to_sign, 'utf-8')
    secret = bytes(secret, 'utf-8')
    sign = base64.b64encode(hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())
    return str(sign, 'utf-8'), str(t), nonce


class Domo:
    config_home = os.environ.get('DOMO_ROOT', os.path.expanduser('~') + '/.config/domo/')
    config_path = os.path.join(config_home + 'config.json')

    f = open(config_path)
    config = json.load(f)

    broadlink_config = config['broadlink']
    manager_url = broadlink_config['manager_url']
    command_url = manager_url + broadlink_config['command_endpoint']
    broadlink_devices = broadlink_config['devices']

    switchbot_config = config['switchbot']
    switchbot_devices = switchbot_config['devices']
    switchbot_base_url = switchbot_config['base_url']
    sign, t, nonce = get_switchbot_auth_params(
        switchbot_config['token'],
        switchbot_config['secret'],
        switchbot_config['nonce']
    )
    switchbot_headers = {
        'Content-type': 'application/json; charset=utf8',
        'Authorization': switchbot_config['token'],
        'sign': sign,
        't': t,
        'nonce': nonce
    }

    tuya_config = config['tuya']
    tuya_devices = tuya_config['devices']
    tuya_api_key = tuya_config['api_key']
    tuya_api_secret = tuya_config['api_secret']
    tuya_api_region = tuya_config['api_region']

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

    def send_tuya_command(self, device_config, command):
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
    Domo().main()
