#!/usr/bin/python3

from pwn import *
import signal, requests, pdb
from bs4 import BeautifulSoup

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)


if len(sys.argv) != 2:
    print("\n")
    log.failure("Uso: python3 %s <domain>\n\n" % sys.argv[0])
    sys.exit(1)
    

# Variables globales

objetivo = sys.argv[1]
main_url = f'https://viewdns.info/reverseip/?host={objetivo}&t=1'

def search():
    agent = {'User-Agent':'Firefox'}
    r = requests.get(main_url, headers=agent)
    using_bs4 = BeautifulSoup(r.text,'html5lib')
    search = using_bs4.find(id="null")
    sites = search.find(border="1")
    for x in sites.find_all("tr"):
        print("Sitios: " + x.td.string)
search()
