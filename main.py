import ipaddress
#from ipaddress import *
#IPv4Address('192.0.2.6') in IPv4Network('192.0.2.0/28')
#from ipaddress import IPv4Address
#from ipaddress import IPv4Network
#IPv4Address('192.0.2.6') in IPv4Network('192.0.2.0/28')

fd1=open("file1.txt","r")
fd2=open("file2.txt","r")
fd3=open("file3.txt","r")
input1=input("Bir IP adresi giriniz:")
input2=input("Bir IP adresi giriniz:")

value1=fd1.read().splitlines()
value2=fd2.read().splitlines()
value3=fd3.read().splitlines()

print(value1)
print(value2)
print(value3)
print("input1: ",input1)
print("input2: ",input2)

input=list()
input.append(input1)
input.append(input2)

for ip_addr in input:
    for ip in value1:
        if bool(ipaddress.IPv4Address(ip_addr) in ipaddress.IPv4Network(ip)) == True:
            print("value1: ",ip_addr)
            break

    for ip_addr in value2:
        if bool(ipaddress.IPv4Address(ip_addr) in ipaddress.IPv4Network(ip)) == True:
            print("value2: ", ip_addr)
            break

    for ip_addr in value3:
        if bool(ipaddress.IPv4Address(ip_addr) in ipaddress.IPv4Network(ip)) == True:
            print("value3: ",ip_addr)
            break