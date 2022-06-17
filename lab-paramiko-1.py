import paramiko
import time
import getpass

ip_address=input("masukan ip address perangkat : ") or "192.168.1.1"
username=input("masukan username perangkat: ") or "cisco"
password=getpass.getpass() or "cisco"
#port=input("masukan port SSH: ")


###proses login ke perangkat
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address, username=username, password=password)

print(f"Login success to device {ip_address}")
#####masukan command cisco 
conn=ssh_client.invoke_shell()

conn.send("enable\n")
conn.send("cisco\n")

conn.send("conf t\n")
conn.send("int lo1\n")
conn.send("ip add 1.1.1.1 255.255.255.255\n")
conn.send("end\n")

conn.send("term leng 0\n")
conn.send("show run\n")

time.sleep(3)

output=conn.recv(65535)
print(output.decode())
ssh_client.close()
