# studio-controller

# Install

```shell
install domo.py ~/.local/bin/domo
```

# Config file

Create a `config.json` in `DOMO_ROOT` (default `~/.config/domo/`)

```json
{
  "broadlink": {
    "manager_url": "",
    "command_endpoint": "",
    "devices": [
      {
        "name": "",
        "type": "",
        "ip": "",
        "mac": "",
        "commands": {
          "volume_up": "",
          "volume_down": "",
          "mute": "",
          "unmute": "",
          "sound_on": "",
          "sound_off": ""
        }
      }
    ]
  },
  "switchbot": {
    "token": ""
  }
}
```