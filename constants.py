import os
from os.path import expanduser
import platform
from typing import Dict


class StringConstant(object):
    def __init__(self, name: str):
        self.name = name.lower()

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return other.name == self.name

    def __ne__(self, other):
        return str(other).lower() != self.name

class OperatingSystem(StringConstant):
    pass


DARWIN: OperatingSystem = OperatingSystem('darwin')
LINUX: OperatingSystem = OperatingSystem('linux')
WINDOWS: OperatingSystem = OperatingSystem('windows')
OPERATING_SYSTEM = OperatingSystem(platform.system())

IS_MACOS = OPERATING_SYSTEM == DARWIN
IS_LINUX = OPERATING_SYSTEM == LINUX
IS_WINDOWS = OPERATING_SYSTEM == WINDOWS

# Only relevant for Windows
LOCALAPPDATA = os.path.abspath(os.environ.get('LOCALAPPDATA', ''))
APPDATA = os.path.abspath(os.environ.get('APPDATA', ''))
PROGRAMS = os.environ.get('Programw6432', '')


LND_DIR_PATH: Dict[OperatingSystem, str] = {
    DARWIN: expanduser('~/Library/Application Support/Lnd/'),
    LINUX: expanduser('~/.lnd/'),
    WINDOWS: os.path.join(LOCALAPPDATA, 'Lnd')
}

LND_CONF_PATH: Dict[OperatingSystem, str] = {
    DARWIN: expanduser('~/Library/Application Support/Lnd/lnd.conf'),
    LINUX: expanduser('~/.lnd/lnd.conf'),
    WINDOWS: os.path.join(LOCALAPPDATA, r'Lnd\lnd.conf')
}

BITCOIN_DATA_PATH: Dict[OperatingSystem, str] = {
    DARWIN: expanduser('~/Library/Application Support/Bitcoin/'),
    LINUX: expanduser('~/.bitcoin'),
    WINDOWS: os.path.join(APPDATA, 'Bitcoin')
}

BITCOIN_CONF_PATH: Dict[OperatingSystem, str] = {
    DARWIN: expanduser('~/Library/Application Support/Bitcoin/'),
    LINUX: expanduser('~/.bitcoin/bitcoin.conf'),
    WINDOWS: os.path.join(APPDATA, r'Bitcoin\bitcoin.conf')
}

TOR_DATA_PATH: Dict[OperatingSystem, str] = {
    WINDOWS: os.path.join(APPDATA, r'tor'),
    DARWIN: '/var/tmp/dist/tor/etc/tor/'
}

TOR_TORRC_PATH: Dict[OperatingSystem, str] = {
    WINDOWS: os.path.join(APPDATA, r'tor\torrc'),
    DARWIN: '/var/tmp/dist/tor/etc/tor/torrc',
    LINUX: '/usr/share/tor/tor-service-defaults-torrc'
}

TOR_PATH: Dict[OperatingSystem, str] = {
    WINDOWS: os.path.join(LOCALAPPDATA, 'tor'),
    DARWIN: expanduser('~/Library/Application Support/Tor')
}

TOR_EXE_PATH: Dict[OperatingSystem, str] = {
    WINDOWS: os.path.join(LOCALAPPDATA, r'tor\tor\tor.exe')
}