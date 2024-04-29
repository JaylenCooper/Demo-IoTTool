import os

from domo.main import Domo


def start():
    config_home = os.environ.get('DOMO_ROOT', os.path.expanduser('~') + '/.config/domo/')
    config_path = os.path.join(config_home + 'config.json')
    domo = Domo(config_path)
    domo.run()


if __name__ == '__main__':
    start()
