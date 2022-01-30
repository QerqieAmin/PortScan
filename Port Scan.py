import pyfiglet
import termcolor
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("Scanning open ports")
ascii_banner = termcolor.colored(ascii_banner , "green")
print(ascii_banner)

print("Example 1.1.1.1")
target = input("Enter Ip Target ==>> ")

# Add Banner
print("-" * 50)
print(termcolor.colored("Scanning Target: " , "yellow") , termcolor.colored(target , "blue"))
print(termcolor.colored("Scanning started at:" , "yellow") , termcolor.colored(str(datetime.now()) , "blue"))
print("-" * 50)

try:
	
	# will scan ports between 1 to 65,535
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		
		# returns an error indicator
		result = s.connect_ex((target,port))
		if result ==0:
			print(termcolor.colored("Port {} is open".format(port) , "green"))
		s.close()
		
except KeyboardInterrupt:
		print("\n Exiting Program !!!!")
		sys.exit()
except socket.gaierror:
		print("\n Hostname Could Not Be Resolved !!!!")
		sys.exit()
except socket.error:
		print("\ Server not responding !!!!")
		sys.exit()
