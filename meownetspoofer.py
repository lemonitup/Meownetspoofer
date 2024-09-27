#!/usr/bin/python
import subprocess
print("""
  /\_/\\  
 ( o.o ) 
  > ^ <  
 /     \\  
|       |  
 \\     /  
  `~~~`   

""")
print("Welcome to Meownetspoofer.")

interface = input("Interface name (e.g., eth0, wlan0): ")
old_MAC_address = input("Enter your old MAC address: ")
changed_MAC_address = input("Enter your new MAC address: ")
change_ip=input("Do you want to change ip address?(Yes or No) : ")
if change_ip.lower()== "yes":
    #if ip change is allowed
    old_IP_address=input("Enter your old ip address: ")
    changed_IP_address=input("Enter your new ip address: ")
    old_ip_netmask=input("Enter your old ip netmask: ")
    changed_IP_netmask=input("Enter your new ip netmask: ")
def user_file (old_MAC_address ,old_IP_address , old_ip_netmask): #to ask user if they want the previous ip/mac address to be outputted so they can remember
    file_name =input("Enter your text file: ")
    with open(file_name, "a") as file:
        file.write(f"Old MAC Address: {old_MAC_address}\n")
        if change_ip.lower() == "yes":
            file.write(f"Old IP Address: {old_IP_address}\n")
            file.write(f"Old IP Netmask: {old_ip_netmask}\n")
       
    
ask_file=input("Do you want to write the old MAC and IP into a file?")
if ask_file.lower()=="yes":
    user_file(old_MAC_address ,old_IP_address , old_ip_netmask)

       
import subprocess

def changing_network(interface, old_MAC_address, changed_MAC_address, change_ip, old_IP_address, changed_IP_address, old_ip_netmask, changed_IP_netmask):
    
    print(f"Processing your old MAC address {old_MAC_address}, into your new MAC address {changed_MAC_address}")
    print(f"Changing interface {interface}")

    # to bring the interface down to change the MAC address
    subprocess.run(["sudo", "ifconfig", interface, "down"], shell=False)

    # to change the mac address
    subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", changed_MAC_address], shell=False)

    # to bring the interface up
    subprocess.run(["sudo", "ifconfig", interface, "up"], shell=False)

    print(f"Your MAC address has been changed to {changed_MAC_address}")

    # if user want to change or spoof ip address then it can change
    if change_ip.lower() == "yes":
        if old_IP_address and changed_IP_address and old_ip_netmask and changed_IP_netmask:
            print(f"Changing old network: {old_IP_address} and {old_ip_netmask} to new network: {changed_IP_address} and {changed_IP_netmask}")
            subprocess.run(["sudo", "ifconfig", interface, changed_IP_address, "netmask", changed_IP_netmask], shell=False)

    #to show if the network configuration is correct
    subprocess.run(["sudo", "ifconfig"], shell=False)
#call the changing netowrk function.
changing_network(interface, old_MAC_address, changed_MAC_address, change_ip, old_IP_address, changed_IP_address, old_ip_netmask, changed_IP_netmask)


