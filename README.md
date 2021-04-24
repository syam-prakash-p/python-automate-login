# Python server login script
---
#### requirement 
if you enabled password based authentication please install sshpass 
#### directory stracture
```sh
├── login.py              # login script
└── .server_conf          # server config data directory
    ├── aws               # change files with your server details
    └── azure

```
##### execute below commands
```sh
$ chmod +x login.py 
$ ln -s ~/<your_path>/login.py ~/bin/log_in 
$ log_in 

Available provider

0  azure

1  aws

choose a provider/ q to quite : 0

Available servers

0  azure-s1

1  azure-s2
```
