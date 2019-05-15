#!/usr/bin/env python3

######
#
# Malware and ransomware update list
#
######


import requests
import os
import subprocess

BlackListFile = '/etc/unbound/black_lists/malware_protect'
urls = ["http://mirror1.malwaredomains.com/files/justdomains",
        "https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist",
        "https://ransomwaretracker.abuse.ch/downloads/RW_DOMBL.txt",
        "http://isc.sans.edu/feeds/suspiciousdomains_Low.txt",
        "http://isc.sans.edu/feeds/suspiciousdomains_Medium.txt",
        "http://isc.sans.edu/feeds/suspiciousdomains_High.txt"]

if os.path.isfile('malwarelist.txt'):
    os.remove('malwarelist.txt')

for url in urls:
    try:
        r = requests.get(url)
        if os.path.isfile(BlackListFile):
            os.remove(BlackListFile)
        else:
            pass
        with open('malwarelist.txt', 'ba') as f:
            f.write(r.content)
    except TimeoutError:
        continue
    except ConnectionError:
        break
def isLineEmpty(line):
    return len(line.strip()) == 0
try:
    with open('malwarelist.txt', 'r') as f:
        line = f.readlines()
        seen = []
        for a in line:
            if not a.startswith("#") and a not in seen and a != "" and not isLineEmpty(a):
                with open(BlackListFile, 'a+') as fe:
                    local_zone = "local-zone: " + "\"" + a.replace('\n', '') + "\"" + " inform_deny\n"
                    local_data = "local-data: " + "\"" + a.replace('\n', '') + " A 127.0.0.1\"\n"
                    fe.write(local_zone)
                    fe.write(local_data)
                    seen.append(a)

        subprocess.call(["/usr/sbin/unbound-control", "reload"])
except IOError:
    print("File open error")
