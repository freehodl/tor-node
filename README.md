# Inspiration

You could use TOR if you don't want anyone to know you're even using Bitcoin.
-Satoshi Nakamoto 

# Requirements
1. Bitcoin Core - https://bitcoincore.org/en/download
2. LND - https://github.com/lightningnetwork/lnd - will still configure Bitcoin full node if no LND node is present
3. Windows 7+, macOS 10.12.6+, Ubuntu 18.04.1

If you don't have nodes set up we suggest using https://github.com/lightning-power-users/node-launcher.

# Install

Download and open the latest release for your operating system:
https://github.com/freehodl/onion-node/realeases

# Onion Node

Onion Node makes it easy to run a Bitcoin full node and LND node over Tor.

1. Finds Bitcoin Core and LND  
2. Downloads appropriate Tor package for the operating system (Linux(Debian), macOS, or Windows) 
3. Installs Tor
2. Appends configuration perameters to bitcoin.conf, lnd.conf, and torrc

macOS

![Onion Node on macOS](https://github.com/freehodl/onion-node/blob/master/macos.png)

