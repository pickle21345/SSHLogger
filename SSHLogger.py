import paramiko
import time
import argparse

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # no known_hosts error

#Declaring Lists for Logs Related to Various Services for Troubleshooting
GeneralLogs = ["/var/log/messages", "/var/log/warnings"]
Test = [""]
VPN = [""]
Custom = []

#Declaring Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-H", "--Host")
parser.add_argument("-p", "--Port")
parser.add_argument("-U", "--User")
parser.add_argument("-P", "--Password")
parser.add_argument("-L", "--List")
parser.add_argument("-C", "--Custom")
parser.add_argument("-W", "--Write")## Not Implemented
parser.add_argument("-X", "--Proxy")## https://gist.github.com/tintoy/443c42ea3865680cd624039c4bb46219
args = parser.parse_args()

# Function to Grab Output from Logs over SSH
def run(files):
    for x in files:
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("cat "+x)
        time.sleep(1)
        output = ssh_stdout.read()
        print(str(output).replace('\\n','\n'))

#Connect to route using usernmae/password authentication
if args.Port is None:
    ssh.connect(hostname=args.Host,username=args.User,password=args.Password)
else:
    ssh.connect(hostname=args.Host,username=args.User,password=args.Password,port=args.Port)


#Working on it    
"""
if args.List is not None:
    match args.List:
        case "GeneralLogs":
            run(GeneralLogs)
        case "ClientVPN":
            run(ClientVPN)
        case "NonMeraki":
            run(NonMeraki)
else:
    Custom.append(args.Custom)
    run(Custom)    
"""

# Close connection.
ssh.close()

