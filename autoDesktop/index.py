import json, time
import paramiko

jsonFile = open('autoDesktop/env.json')
env = json.load(jsonFile)
sshVars = env["ssh"]

# connection variables
host = sshVars["host"]
username = sshVars["username"]
password = sshVars["password"]
port = 22

# connect to host
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port, username, password)

command="cat test.test"

stdin, stdout, stderr = client.exec_command(command)

time.sleep(5)
print(stdout.read().strip())

client.close()

