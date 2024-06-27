import socket

#START HERE

#TODO - allow for client-side user to manually input a hostname

#Get host name to launch client
hostName=socket.gethostname()
HOST=hostName #PC Host Name
PORT=8080 #Port to access

#Ask user for inputs corresponding to basic math operations
#Validate inputs to ensure numbers (float type) and an operator are used
#Use while loops to continue to prompt for correct input until one is given
while True:
    rawInput1 = input("Enter number 1: ")
    try:
        float(rawInput1)
        number1 = rawInput1.strip().encode('utf-32')
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    rawInput2 = input("Enter number 2: ")
    try:
        float(rawInput2)
        number2 = rawInput2.strip().encode('utf-32')
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    rawInput3 = input("Enter operation: ")
    if (rawInput3=="+" or rawInput3=="-" or rawInput3=="/" or rawInput3=="*"):
        opVar = rawInput3.strip().encode('utf-32')
        break
    else:
        print("Invalid input. Please enter an operator without spaces. (+, -, /, or *)")

with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as sock:
    #Connect to server and send three numbers in order
    try:
        sock.connect((HOST, PORT))
        sock.sendall(opVar)
        data = sock.recv(1024)
        sock.sendall(number1)
        data = sock.recv(1024)
        sock.sendall(number2)
        data = sock.recv(1024)
        #Decode the final value as utf-32 spring for printing
        data = sock.recv(1024).decode('utf-32')
    except ConnectionRefusedError:
        print("Connection refused on server side. Please try again.\nIf the error persists, please contact support at dgallagher7@student.cscc.edu.")
        exit()

#If program has not exited due to error, print result
print(f"The result of the operation is {data!r}")
