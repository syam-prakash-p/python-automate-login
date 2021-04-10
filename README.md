"""
# requirement 
if you enabled password based authentication please install sshpass 


#Directory stracture 

syam@localhost:~/projects/scripts/login$ pwd
/home/syam/projects/scripts/login

syam@localhost:~/projects/scripts/login$ tree -a
.
├── .keys                 # key files
│   └── key.pem           
├── login.py              # login script
└── .server_conf          # server config data directory
    ├── aws               # change files with your server details
    └── azure

2 directories, 4 files
syam@localhost:~/projects/scripts/login$ 


syam@localhost:~/projects/scripts/login$ chmod +x login.py 
syam@localhost:~/projects/scripts/login$ 
syam@localhost:~/projects/scripts/login$ ln -s ~/projects/scripts/login/login.py ~/bin/log_in 
syam@localhost:~/projects/scripts/login$ 
syam@localhost:~/projects/scripts/login$ log_in 

Available provider

0  azure

1  aws

choose a provider/ q to quite : 0

Available servers

0  azure-s1

1  azure-s2

2  azure-s3

choose a servers/ q to quite : q         # you can login to the server by selecting the server no, here i just quite
syam@localhost:~/projects/scripts/login$ 

"""



