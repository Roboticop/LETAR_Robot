import socket
hostname = socket.gethostname()
IpAddr = socket.gethostbyname(hostname)
print("Your computer Name is: " + hostname)
print("Your Computer IP Address is: " + IpAddr)