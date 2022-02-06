# wifi-jammer

Continuously perform deauthentication attacks on all detectable stations.

DISCLAIMER: I am not responsible for the misuse of this software for illicit purposes. Remember: with great power comes great responsibility.

## Pre-requisites

- Python 3
- Debian-based Linux (preferably Kali Linux)
- Wi-fi adapter that supports monitor mode

The following utilities are utilized:

- `airodump-ng`
- `aireplay-ng`
- `airmon-ng`

## Parameters

- `IFACE`: name of the wi-fi interface
- `airodump_output`: name of the output .csv file for monitoring
- `num_packets`: number of deauthentication packets sent to the target

## Usage

Just run `python3 main.py` and see the magic happens!
