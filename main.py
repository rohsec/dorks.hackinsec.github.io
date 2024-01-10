import re
from pyscript import document
from time import sleep

bred='\033[1;31m'
bblue='\033[1;34m'
bgreen='\033[1;32m'
yellow='\033[0;33m'
red='\033[0;31m'
blue='\033[0;34m'
green='\033[0;32m'
reset='\033[0m'
BASE_URL = "https://crt.sh/?q={}&output=json"
subdomains = set()
wildcardsubdomains = set()
choices=['n','y']

def logo():
    print(f"""{blue}            _                   
           | |                  
  _ __ ___ | |__  ___  ___  ___ 
 | '__/ _ \| '_ \/ __|/ _ \/ __|
 | | | (_) | | | \__ \  __/ (__ 
 |_|  \___/|_| |_|___/\___|\___|
{yellow}<---- {green}Twitter: {red}@rohsec{yellow} ---->
{reset}
This is a demonstration of how BugBounty scripts can be run in a web browser
""")   


def dorker():
    logo()
    domain=input("Enter a domain: ")
    domain_pattern = r"^(?![0-9]+$)(?!-)(?:[a-zA-Z0-9-]{0,62}[a-zA-Z0-9]\.)+(?:[a-zA-Z]{2,})$"
    with open('dorks1.txt', "r") as f1:
        x1=f1.readlines()
        x="xxxx "
    f1.close()
    if(re.match(domain_pattern,str(domain))):
        for i in x1:
            if(i.startswith('#')):
                print(f"{red}{i.strip()}{reset}")
            else:
                print(f"{blue}{i.replace('example.com',domain)[1:].strip()}{reset}")
    else:
        print("Invalid domain inserted...Try again!!")
        dorker()

prog=document.getElementById('prog')
sleep(4)
prog.remove()        
dorker()
print(f"{yellow}>>>>>>>>>>>{bgreen} Tool Created By {bred}@rohsec{bgreen} for demonstration purposes{yellow} <<<<<<<<<<<<<{reset}")
print("You can buy me a coffee at https://buymeacoffee.com/rohsec")