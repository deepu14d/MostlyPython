# Scan an IP

import nmap
import time

scanner = nmap.PortScanner()
print("\n********************************************")
print("   This is a simple nmap automation tool!   ")
print("********************************************\n")

ip = input("Enter the IP address you wanna scan....")
print("The IP you entered is: ", ip)
type(ip)

time.sleep(0.5)

option = input("""\n Please select the type of scan you want to run
	1) SYS ACK Scan
	2) UDP Scan
	3) Comprehensive Scan \n Enter 1, 2 or 3: """)
print("You have selected option: ",option, "\n")

time.sleep(0.5)

try:
	if option == '1':
		print("Nmap version: ", scanner.nmap_version())
		print("Scanning...")
		time.sleep(2.3)
		print("Please wait it can take some time")
		scanner.scan(ip, '1-1024', '-v -sS')
		print(scanner.scaninfo())
		print("IP status: ", scanner[ip].state())
		print(scanner[ip].all_protocols())
		print("Open ports: ", scanner[ip]['tcp'].keys())

	elif option == '2':
		print("Nmap version: ", scanner.nmap_version())
		print("Scanning...")
		time.sleep(2.3)
		print("Please wait it can take some time")
		scanner.scan(ip, '1-1024', '-v -sU')
		print(scanner.scaninfo())
		print("IP status: ", scanner[ip].state())	
		print(scanner[ip].all_protocols())
		print("Open ports: ", scanner[ip].all_udp())

	elif option == '3':
		print("Nmap version: ", scanner.nmap_version())
		print("Scanning...")
		time.sleep(2.3)
		print("Please wait it can take some time")
		scanner.scan(ip, '1-1024', '-v -sS -sV -sC -A -O')
		print(scanner.scaninfo())
		print("IP status: ", scanner[ip].state())	
		print(scanner[ip].all_protocols())
		print("Open ports: ", scanner[ip]['tcp'].keys())

	else:
		print("Please enter a valid option")

except KeyError as err:
	print(f"Check you input and try again. Is {err} an IP?")