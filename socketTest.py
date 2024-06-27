
import socket

#TODO-Allow for multiple, successive client connections. Do not close connection after returning first result, and reset listening state to await another incoming connection.
#TODO-Allow for simultaneous client connections.
#TODO-Validate inputs on server side as an extra failsafe.

#Set up hostname and port
hostName=socket.gethostname()
HOST=hostName #PC Host Machine
PORT=8080 #Port to use for Hosting

inputArray= []

#Launch Server
#Socket will time out if a certain amount of time (10 minutes) passes without a connection attempt.
with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as sock:
	sock.settimeout(600) #Time out after 10 minutes
	try:
		#Bind the host socket to server address 
		sock.bind((HOST, PORT))
		print("Bind successful...")
		#Begin listening, wait for client connection
		sock.listen(1) #limit of 1 simultaneous connection, would have to adjust value if allowing for multiple connections
		print("Listening...")

	    #After "Listening..." displays, launch client script to open connection
		conn, addr = sock.accept()
		print("Connection accepted...")		
		with conn:
			#Display connection info and receive data
			print(f"Connected by {addr}")
			while len(inputArray)<3:
				data = conn.recv(1024)
				inputArray.append(data.decode('utf-32'))
				if not data:
					break
				conn.sendall(data)

			#Operator is checked for on client side so we assume it will be valid here
			opVar=inputArray[0]
			#Float type is used on client side inputs so we assume it will be valid here
			number1=float(inputArray[1])
			number2=float(inputArray[2])

			#Check if opVar is valid and perform operation
			if opVar=="+":
				numberResult = number1 + number2
				print(number1," + ",number2," = ",numberResult)
				conn.sendall(str(numberResult).encode('utf-32'))
			elif opVar=="-":
				numberResult = number1 - number2
				print(number1," - ",number2," = ",numberResult)
				conn.sendall(str(numberResult).encode('utf-32'))
			elif opVar=="/":
				numberResult = number1 / number2
				print(number1," / ",number2," = ",numberResult)
				conn.sendall(str(numberResult).encode('utf-32'))		
			elif opVar=="*":
				numberResult = number1 * number2
				print(number1," * ",number2," = ",numberResult)
				conn.sendall(str(numberResult).encode('utf-32'))
			else:
				print("Invalid input! Must choose one of the following: +-/*")

			#Close the connection
			conn.close() 
	except TimeoutError:
		print("Connection timed out. Please relaunch the server and try again.")

exit()
#No code below this line will be run!