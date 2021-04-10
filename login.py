#!/usr/bin/python3
from configparser import ConfigParser
import os
import subprocess

dual,pswd,key=False,False,False
login_home='/home/syam/projects/scripts/login'
conf_dir=f'{login_home}/.server_conf'

conf = ConfigParser()

def display_and_return(input_list,type):
    """
    display input list with numbers and if user input any number 
    corresponding value is selected from the list( index as user input)

    """
    print(f"\nAvailable {type}\n")
    for i in range(len(input_list)):
        print(f"{i}  {input_list[i]}\n")

    def get_and_validate():

        try:
            prov = input(f"choose a {type}/ q to quite : ")
            if prov =='q':
                return False
            else:

                prov = int(prov)
                val=input_list[prov]
        except:
            print("invalid input")
            val=get_and_validate()
        return val


    return get_and_validate()


def login_cmd(authentication,conf,server):
    if authentication=="dual":
        print(f"Enter password {conf[server]['pass']}")
        cmd = f"ssh -i {conf[server]['key']} {conf[server]['user']}@{conf[server]['ip']} -p {conf[server]['port']} "
    elif authentication=="key":
        cmd = f"ssh -i {conf[server]['key']} {conf[server]['user']}@{conf[server]['ip']} -p {conf[server]['port']} "
    elif authentication=="pass":
        cmd = f"sshpass -p {conf[server]['pass']} ssh {conf[server]['user']}@{conf[server]['ip']} -p {conf[server]['port']} "
    else:
        cmd = f"ssh {conf[server]['user']}@{conf[server]['ip']} -p {conf[server]['port']}"

    p = subprocess.run(cmd,stderr=subprocess.PIPE, shell=True)

    if p.returncode != 0:

        print(f"failed to ssh \n {p.stderr.decode()}")




provider = display_and_return(os.listdir(conf_dir),'provider')
if not provider:
    exit()

conf.read(f"{conf_dir}/{provider}")

server = display_and_return(conf.sections(),"servers")
if not server:
    exit()

if "pass" in list(conf[server].keys()) and "key" in list(conf[server].keys()):
    login_cmd("dual", conf,server)

elif "pass" in list(conf[server].keys()):
    login_cmd("pass", conf,server)

elif "key" in list(conf[server].keys()):
    login_cmd("key", conf,server)
else:
    login_cmd("null", conf,server)




