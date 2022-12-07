# Domo

## Introduction
This is a very simple all-in-one script to manage the iot devices from the CLI.
This can be very useful to create other script and automation of the routines in your house.
This idea was born for personal use only. Enjoy.

## Acknowledgments
This script uses other libraries and tools made by others. Please say thanks to the creators of those tools.

## Install

You can install this using an AUR helper if you are on Arch Linux based distro.
```shell
yay -S domo-git
```

Otherwise, first of all install dependencies (assuming you are using python3):
```shell
python -m pip install -r ./requirements.txt
```

Then install the script in a local bin folder
```shell
install domo.py ~/.local/bin/domo
```

If you are planning to use boradlink devices you can run an instance of the broadlink manager using docker.
Please check and say thanks to @t0mer: https://github.com/t0mer/broadlinkmanager-docker.
```shell
docker-compose ip --build -d
```

## Config file

Create a `config.json` in `DOMO_ROOT` (default `~/.config/domo/`, you can set your `DOMO_ROOT` environment variable to change the path):

```json
{
    "broadlink": {
        "manager_url": "YOUR_BROADLINK_MANAGER_URL (http://localhost:7020/)",
        "command_endpoint": "command/send/",
        "devices": {
            "YOUR_DEVICE_NAME_TO_USE_IN_THE_SCRIPT": {
                "type": "THE TYPE OF YOR BROADLINK DEVICE. SOMETHING LIKE 0x649b. CHECK: https://github.com/t0mer/broadlinkmanager-docker",
                "ip": "BROADLINK_DEVICE_IP",
                "mac": "BROADLINK_DEVICE_MAC",
                "commands": {
                    "YOUR_COMMAND": "CODE OF THE COMMAND TO REPRODUCE",
                    "ANOTHER_COMMAND": "YOU CAN USE THE SAME COMMAND CODE TO CREATE ALIASES",
                     ...
                }
            }
        }
    },
    "switchbot": {
        "base_url": "https://api.switch-bot.com",
        "token": "YOUR_TOKEN",
        "secret": "YOUR_SECRET",
        "nonce": "NONCE_AS_NUMBER",
        "devices": {
            "coffee": {
                "device_id": "D87BEDD0A20A",
                "device_type": "YOUR_DEVICE_TYPE (Bot)",
                "commands": {
                    "YOUR_COMMAND": "COMMAND_CODE",
                    ...
                }
            }
        }
    },
    "tuya": {
        "api_key": "YOUR_API_KEY",
        "api_secret": "YOUR_API_SECRET",
        "devices": {
            "YOUR_DEVICE_NAME_TO_USE_IN_THE_SCRIPT": {
                "ip": "DEVICE_IP",
                "key": "LOCAL_KEY",
                "id": "DEVICE_ID",
                "ver": "3.3",
                "commands": {
                    "YOUR_COMMAND": "COMMAND_CODE",
                    ...
                }
            }
        }
    }
}
```

Config example (the values are randomly generated).
```json
{
    "broadlink": {
        "manager_url": "http://localhost:7020/",
        "command_endpoint": "command/send/",
        "devices": {
            "soundbar": {
                "type": "0x649b",
                "ip": "192.168.1.100",
                "mac": "5cc007b12e1e",
                "commands": {
                    "volume_up": "Jg",
                    "volume_down": "JgOPWBKV0N0JBR5EYBTWGHOPWBKV0N0JBR5EYBTWGHOPWBKV0N0JBR5EYBTWGHOPWBKV0N0JBR5EYBTWGHOPWBKV0N0JBR5EYBTWGHOPWBKV0N0JBR5EYBTWGHOPWBKV0N0JBR5EYBTWGHOPWBKV0N0JBR5EYBTWGHOPWBKV0N0JBR5EYBTWGHOPWBKV0N0JBR5EYBTWGH==",
                    "mute": "JgPUN4YWLVL3RWQZ6KM7BEPUN4YWLVL3RWQZ6KM7BEPUN4YWLVL3RWQZ6KM7BEPUN4YWLVL3RWQZ6KM7BEPUN4YWLVL3RWQZ6KM7BEPUN4YWLVL3RWQZ6KM7BEPUN4YWLVL3RWQZ6KM7BEPUN4YWLVL3RWQZ6KM7BEPUN4YWLVL3RWQZ6KM7BEPUN4YWLVL3RWQZ6KM7BE==",
                    "unmute": "Jg9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH==",
                    "power": "JgVEWGD49XC2RJIG0NUWIYVEWGD49XC2RJIG0NUWIYVEWGD49XC2RJIG0NUWIYVEWGD49XC2RJIG0NUWIYVEWGD49XC2RJIG0NUWIYVEWGD49XC2RJIG0NUWIYVEWGD49XC2RJIG0NUWIYVEWGD49XC2RJIG0NUWIYVEWGD49XC2RJIG0NUWIYVEWGD49XC2RJIG0NUWIY==",
                    "on": "Jg0WWVWMDIJONWJ8OVUWQR0WWVWMDIJONWJ8OVUWQR0WWVWMDIJONWJ8OVUWQR0WWVWMDIJONWJ8OVUWQR0WWVWMDIJONWJ8OVUWQR0WWVWMDIJONWJ8OVUWQR0WWVWMDIJONWJ8OVUWQR0WWVWMDIJONWJ8OVUWQR0WWVWMDIJONWJ8OVUWQR0WWVWMDIJONWJ8OVUWQR==",
                    "power_on": "Jg0WWVWMDIJONWJ8OVUWQR0WWVWMDIJONWJ8OVUWQR0WWVWMDIJONWJ8OVUWQR0WWVWMDIJONWJ8OVUWQR0WWVWMDIJONWJ8OVUWQR0WWVWMDIJONWJ8OVUWQR0WWVWMDIJONWJ8OVUWQR0WWVWMDIJONWJ8OVUWQR0WWVWMDIJONWJ8OVUWQR0WWVWMDIJONWJ8OVUWQR==",
                    "off": "JgIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2O==",
                    "power_off": "JgIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2O==",
                    "bass_up": "JgIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2OIHFVLP2S58EPPWTO3P2O==",
                    "bass_down": "JgMFRTJ5MGNCJ5BQH9FMA3MFRTJ5MGNCJ5BQH9FMA3MFRTJ5MGNCJ5BQH9FMA3MFRTJ5MGNCJ5BQH9FMA3MFRTJ5MGNCJ5BQH9FMA3MFRTJ5MGNCJ5BQH9FMA3MFRTJ5MGNCJ5BQH9FMA3MFRTJ5MGNCJ5BQH9FMA3MFRTJ5MGNCJ5BQH9FMA3MFRTJ5MGNCJ5BQH9FMA3=="
                }
            },
            "air_conditioner": {
                "type": "0x649b",
                "ip": "192.168.1.100",
                "mac": "5cc007b12e1e",
                "commands": {
                    "power": "Jg9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH",
                    "on": "Jg9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH",
                    "power_on": "Jg9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH",
                    "off": "JgPUN4YWLVL3RWQZ6KM7BEPUN4YWLVL3RWQZ6KM7BEPUN4YWLVL3RWQZ6KM7BEPUN4YWLVL3RWQZ6KM7BEPUN4YWLVL3RWQZ6KM7BEPUN4YWLVL3RWQZ6KM7BE",
                    "power_off": "JgPUN4YWLVL3RWQZ6KM7BEPUN4YWLVL3RWQZ6KM7BEPUN4YWLVL3RWQZ6KM7BEPUN4YWLVL3RWQZ6KM7BEPUN4YWLVL3RWQZ6KM7BEPUN4YWLVL3RWQZ6KM7BE",
                    "change_mode": "Jg9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH9NC6152LY4SGE4VW2BEH"
                }
            },
            "led": {
                "type": "0x649b",
                "ip": "192.168.1.100",
                "mac": "5cc007b12e1e",
                "commands": {
                    "power": "Jg7PPPPE6IKZLJ1SRKOPZ47PPPPE6IKZLJ1SRKOPZ47PPPPE6IKZLJ1SRKOPZ47PPPPE6IKZLJ1SRKOPZ47PPPPE6IKZLJ1SRKOPZ47PPPPE6IKZLJ1SRKOPZ4",
                    "on": "Jg7PPPPE6IKZLJ1SRKOPZ47PPPPE6IKZLJ1SRKOPZ47PPPPE6IKZLJ1SRKOPZ47PPPPE6IKZLJ1SRKOPZ47PPPPE6IKZLJ1SRKOPZ47PPPPE6IKZLJ1SRKOPZ4",
                    "power_on": "Jg7PPPPE6IKZLJ1SRKOPZ47PPPPE6IKZLJ1SRKOPZ47PPPPE6IKZLJ1SRKOPZ47PPPPE6IKZLJ1SRKOPZ47PPPPE6IKZLJ1SRKOPZ47PPPPE6IKZLJ1SRKOPZ4",
                    "off": "JgQCWB9CXE86DVBZ71IZ08QCWB9CXE86DVBZ71IZ08QCWB9CXE86DVBZ71IZ08QCWB9CXE86DVBZ71IZ08QCWB9CXE86DVBZ71IZ08QCWB9CXE86DVBZ71IZ08",
                    "power_off": "JgQCWB9CXE86DVBZ71IZ08QCWB9CXE86DVBZ71IZ08QCWB9CXE86DVBZ71IZ08QCWB9CXE86DVBZ71IZ08QCWB9CXE86DVBZ71IZ08QCWB9CXE86DVBZ71IZ08",
                    "less_light": "Jg99XQACC5MLV3UD8YC7E499XQACC5MLV3UD8YC7E499XQACC5MLV3UD8YC7E499XQACC5MLV3UD8YC7E499XQACC5MLV3UD8YC7E499XQACC5MLV3UD8YC7E4",
                    "less": "Jg99XQACC5MLV3UD8YC7E499XQACC5MLV3UD8YC7E499XQACC5MLV3UD8YC7E499XQACC5MLV3UD8YC7E499XQACC5MLV3UD8YC7E499XQACC5MLV3UD8YC7E4",
                    "more_light": "JgR2ILVL80XB2QG8EL4B9KR2ILVL80XB2QG8EL4B9KR2ILVL80XB2QG8EL4B9KR2ILVL80XB2QG8EL4B9KR2ILVL80XB2QG8EL4B9KR2ILVL80XB2QG8EL4B9K",
                    "more": "JgR2ILVL80XB2QG8EL4B9KR2ILVL80XB2QG8EL4B9KR2ILVL80XB2QG8EL4B9KR2ILVL80XB2QG8EL4B9KR2ILVL80XB2QG8EL4B9KR2ILVL80XB2QG8EL4B9K"
                }
            }
        }
    },
    "switchbot": {
        "base_url": "https://api.switch-bot.com",
        "token": "UJu8eM6Rb0Ox3nJLWjgdcjAeWagWxdmVNDGnfYIac6y1pXtnfzWvO2JTEaAnMFVwbHzX0M2Mt7ddZzDrplCbeDOsxG3X7I5I",
        "secret": "8U5JoavM68yVFqBtr74CHBwxbUINPnfH",
        "nonce": "1983374623984",
        "devices": {
            "coffee_machine": {
                "device_id": "E55CCPO0F68L",
                "device_type": "Bot",
                "commands": {
                    "press": "press"
                }
            }
        }
    },
    "tuya": {
        "api_key": "AaIHhkzVfC5q4yDObmJY",
        "api_secret": "fez72tVYlDfIXGM9R2EgD2ClbKidC1iL",
        "api_region": "eu",
        "devices": {
            "christmas_tree": {
                "ip": "192.168.1.101",
                "key": "MeO6hFID8zwzQzSS",
                "id": "Erpv6kB4FcpBfoWocnfn",
                "ver": "3.3",
                "commands": {
                    "power_on": "power_on",
                    "on": "on",
                    "power_off": "power_off",
                    "off": "off"
                }
            },
            "led_studio": {
                "ip": "192.168.1.102",
                "key": "MeO6hFID8zwzQzSS",
                "id": "Ie4ridhSeUHZvoBMF6fC",
                "ver": "3.1",
                "commands": {
                    "power_on": "power_on",
                    "on": "on",
                    "power_off": "power_off",
                    "off": "off"
                }
            }
        }
    }
}
```

## Supported IoT frameworks/devices

### Broadlink
Please check https://github.com/t0mer/broadlinkmanager-docker for broadlink device connection and usage.

### Switchbot
Please check https://github.com/OpenWonderLabs/SwitchBotAPI for SwitchBot API documentation.

### Tuya
You can find mode information about tuya checking both: https://pypi.org/project/tinytuya/ and https://tuya.com/
#### Scan tuya devices
```shell
python -m tinytuya scan
```
Then check the `snapshot.json` created file
#### Tuya wizard:
```shell
python -m tinytuya wizard
```
Then check the `tinituya.json` and the `devices.json` created files to discover information about your device.

#### Tuya limitations
Currently this script supports only tuya devices on/off.
If you want to control more features you can use the `tinytuya` library to discover the commands to send to the device.