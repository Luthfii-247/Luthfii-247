from encodings import utf_8
from ntpath import join
from numpy import character
import paramiko
import time
import getpass

ip_address=input("masukan ip address perangkat : ") or "192.168.1.1"
username=input("masukan username perangkat: ") or "cisco"
password=getpass.getpass() or "cisco"



###proses login ke perangkat
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address, username=username, password=password)

print(f"Login success to device {ip_address}")

conn=ssh_client.invoke_shell()

conn.send("enable\n")
conn.send("cisco\n")

#check ospf
conn.send("show ip ospf neighbor\n")
conn.send("show ip ospf interface\n")
conn.send("show ip ospf database\n")


#show run command
conn.send("term leng 0\n")
conn.send("show run\n")
time.sleep(3)



output=conn.recv(65535).decode("utf-8")
print(output)


output_txt=open('{0}.txt'.format(ip_address),'w')
output_txt.write(''.join(output))
output_txt.close()

print 
'config in {} saved!!'.format(ip_address)



ssh_client.close()
