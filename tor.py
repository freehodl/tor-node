import sys
import getpass
import lsb_release
import time
import urllib
import subprocess
import zipfile
import os
import os.path
from os.path import expanduser
from urllib.request import urlopen
from subprocess import call, Popen, PIPE
from tempfile import NamedTemporaryFile
from typing import List, Optional

from constants import BITCOIN_DATA_PATH, BITCOIN_CONF_PATH, TOR_DATA_PATH, \
    TOR_TORRC_PATH, LND_CONF_PATH , TOR_PATH, TOR_EXE_PATH, OPERATING_SYSTEM, IS_WINDOWS, \
    IS_MACOS, IS_LINUX, LND_DIR_PATH
from tqdm import tqdm
import time

class Tor(object):

    def find_nodes():
        print('Onion Node is preparing your system...')
        for i in tqdm(range(100), desc="Looking for nodes"):
            time.sleep(0.02)
        if not os.path.exists(str(BITCOIN_DATA_PATH[OPERATING_SYSTEM])):
            print('Onion Node was unable to find a Bitcoin full node on this system')
            time.sleep(1)
            print('Setup a Bitcoin full node before using Onion Node')
            print('Try https://github.com/lightning-power-users/node-launcher')
            sys.exit("Onion Node is shutting down...")
        elif not os.path.exists(str(LND_DIR_PATH[OPERATING_SYSTEM])):
            print('Onion Node was unbale to find a LND node on this system')
            time.sleep(1)
            print('Setup an LND node before using Onion Node') 
            print('Try https://github.com/lightning-power-users/node-launcher')
            sys.exit("Onion Node is shutting down...")

    def edit_bitcoin_conf()
        for i in tqdm(range(100), desc="Configuring bitcoin.conf"):
            time.sleep(0.02)
        f = open(str(BITCOIN_CONF_PATH[OPERATING_SYSTEM]) , 'a')
        f.write('proxy=127.0.0.1:9050\n')
        f.write('listen=1\n')
        f.write('bind=127.0.0.1\n')
        f.write('debug=tor\n')
        f.close()


    def edit_lnd_conf():
        for i in tqdm(range(100), desc="Configuring lnd.conf"):
            time.sleep(0.02)
        f = open(str(LND_CONF_PATH[OPERATING_SYSTEM]) , 'a')
        f.write(' \n')
        f.write('[Application Options]\n')
        f.write('listen=localhost\n')
        f.write(' \n')
        f.write('[tor]\n')
        f.write('tor.active=1\n')
        f.write('tor.v3=1\n')
        f.write('tor.streamisolation=1\n')
        f.close()

    def downloadtor():
        for i in tqdm(range(100), unit_scale=True, desc="Downloading Tor", unit='epoch'):
            time.sleep(0.12)
        if IS_WINDOWS:
            url = 'https://www.torproject.org/dist/torbrowser/8.0.4/tor-win32-0.3.4.9.zip'
            f = urllib.request.urlopen(url)
            file = f.read()
            f.close()
            f2 = open('tor-win32-0.3.4.9.zip', 'wb')
            f2.write(file)
            f2.close()
        elif IS_MACOS:
            url = 'https://www.torproject.org/dist/torbrowser/8.0.4/TorBrowser-8.0.4-osx64_en-US.dmg'
            urllib.request.urlretrieve(url, expanduser('~/Downloads/TorBrowser-8.0.4-osx64_en-US.dmg'))

    def deb_install():

        def deb_permissions():
            for i in tqdm(range(100), desc="Updating user permissions"):
                time.sleep(0.02)
            bashcommand_chmod = 'sudo chmod a+rw /etc/apt/sources.list'
            subprocess.run(['bash', '-c', bashcommand_chmod])

        def deb_install_tor():
            release = lsb_release.get_lsb_information()
            codename = release.get('CODENAME')
            deba = 'deb http://deb.torproject.org/torproject.org ', str(codename),' main\n'
            deb_line = ""
            deb_line = deb_line.join(deba)
            debb = 'deb-src http://deb.torproject.org/torproject.org ', str(codename), ' main'
            deb_src = ""
            deb_src = deb_src.join(debb)
            f = open('/etc/apt/sources.list', 'a')
            f.write(deb_line)
            f.write(str(deb_src))
            f.close()
            print('Installing Tor.....')
            bashcommand_gpg_key = 'gpg --keyserver keys.gnupg.net --recv 886DDD89'
            bashcommand_gpg_export = 'gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | sudo apt-key add -'
            bashcommand_update = 'sudo apt-get update'
            bashcommand_install_tor = 'sudo apt-get install tor deb.torproject.org-keyring'
            subprocess.run(['bash', '-c', bashcommand_gpg_key])
            subprocess.run(['bash', '-c', bashcommand_gpg_export])
            subprocess.run(['bash', '-c', bashcommand_update])
            subprocess.run(['bash', '-c', bashcommand_install_tor])

        def deb_modify_user():
            for i in tqdm(range(100), desc="Adding user to Tor user group"):
                time.sleep(0.02)
            for line in open("/usr/share/tor/tor-service-defaults-torrc"):
                if "User" in line:
                    newline = line.replace("User ", "")
                    newline = str(newline.rstrip())
                    tor_user = str(newline)
                continue
            username = str(getpass.getuser())
            bashcommand_modify = 'sudo usermod -a -G ', str(tor_user), ' ', str(username)
            bashcommand_usermod = ""
            bashcommand_usermod = bashcommand_usermod.join(bashcommand_modify)
            subprocess.run(['bash', '-c', bashcommand_usermod])
            print('NOTE: You may need to restart your node after Onion Node setup is complet')
            print('Oninion Node setup is complete!')
            time.sleep(3)       
        
        if IS_LINUX:
            deb_permissions()
            deb_install_tor()
            deb_modify_user()

    def installtor():
        for i in tqdm(range(100), desc="Adding user to Tor user group"):
                time.sleep(0.12)
        if IS_WINDOWS:
            torpath = str(TOR_PATH[OPERATING_SYSTEM])
            if not os.path.exists(torpath):
                os.makedirs(torpath)
            zip_ref = zipfile.ZipFile(r'tor-win32-0.3.4.9.zip', 'r')
            zip_ref.extractall(torpath)
            zip_ref.close()
        elif IS_MACOS:
            bash_torpath = expanduser('~/Library/Application\ Support/Tor/')
            torpath = expanduser('~/Library/Application Support/Tor/')
            if not os.path.exists(torpath):
                os.makedirs(torpath)
            bashcommand_attach = 'hdiutil attach ~/Downloads/TorBrowser-8.0.4-osx64_en-US.dmg'
            bashcommand_detach = 'hdiutil detach /Volumes/Tor\ Browser'
            cp = ["cp -R /Volumes/Tor\ Browser/Tor\ Browser.app ", str(bash_torpath)]
            bashcommand_cp =  ""
            bashcommand_cp = bashcommand_cp.join(cp)
            subprocess.run(['bash', '-c', bashcommand_attach])
            subprocess.run(['bash', '-c', bashcommand_cp])
            subprocess.run(['bash', '-c', bashcommand_detach])

    def runtor():
        for i in tqdm(range(100), desc="Starting Tor"):
                time.sleep(0.02)
        if IS_WINDOWS:
            subprocess.Popen(str(TOR_EXE_PATH[OPERATING_SYSTEM]))
        elif IS_MACOS:
            subprocess.Popen(expanduser('~/Library/Application Support/Tor/Tor Browser.app/Contents/MacOS/Tor/tor.real'))
        print('NOTE: You may need to restart your node after Onion Node setup is complet')
        print('Oninion Node setup is complete!')
        time.sleep(1)       


    def write_torrc():
        for i in tqdm(range(100), desc="Adding user to Tor user group"):
                time.sleep(0.02)
        if IS_WINDOWS or IS_MACOS:
            tordatapath = str(TOR_DATA_PATH[OPERATING_SYSTEM])
            if not os.path.exists(tordatapath):
                os.makedirs(tordatapath)
            f = open(str(TOR_TORRC_PATH[OPERATING_SYSTEM]), 'a')
            f.write(' \n')
            f.write('ControlPort 9051\n')
            f.write('CookieAuthentication 1\n')
            f.write(' \n')
            f.write('HiddenServiceDir ')
            f.write(os.path.join(tordatapath, 'bitcoin-service'))
            f.write('\n')
            f.write('HiddenServicePort 8333 127.0.0.1:8333\n')
            f.write('HiddenServicePort 18333 127.0.0.1:18333\n')
            f.close()

    
def launch():
    if IS_MACOS or IS_WINDOWS:
        Tor.find_nodes()
        Tor.edit_bitcoin_conf()
        Tor.edit_lnd_conf()
        Tor.downloadtor()
        Tor.installtor()
        Tor.write_torrc()
        Tor.runtor()
    elif IS_LINUX:
        Tor.find_nodes()
        Tor.edit_bitcoin_conf()
        Tor.edit_lnd_conf()
        Tor.deb_install()

launch()



