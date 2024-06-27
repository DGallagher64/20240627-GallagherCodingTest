
[Overview]

This is a simple program intended to demonstrate the capabilities of python's socket module.

A server launches, then waits for input from a client for 10 minutes. The client takes 3 user inputs and sends them to the server, which calculates a simple mathematical operation and returns a value before closing the connection and exiting. Client finally outputs said value to end user, then exits.

---

[Prerequisites]
Ensure python is installed on your machine.

Python can be acquired here:
https://www.python.org/
Recommended version: 3.12.4

---

[Instructions]
0. Open two command prompt windows in the target folder. That is, the folder(s) with socketTest.py and clientTest.py inside.

1. Run socketTest.py using the following command prompt inputs.
>python socketTest.py

2. Run clientTest.py from a separate command prompt window using the following command prompt inputs.
>python clientTest.py

3. The clientTest.py command prompt window will ask for 3 inputs, first 1 numbers and then the operation. Input 2 numbers, and one of 4 supported operands (+, -, /, or *). If non-numerical or non-operand values are input, it will return an error and prompt you to input the values again.
>Enter number 1: 23
>Enter number 2: 6
>Enter operation: *

4. socketTest.py window will show the operation being performed as well as the output, then close.
clientTest.py will

---

[References]

Reference #1 (Example socketTest.py server-side output):
>Bind successful...
>Listening...
>Connection accepted...
>Connected by ('ffff::ffff:ffff:ffff:ffff', 51210, 0, 7)
>23.0  *  6.0  =  138.0

Note: The contents displayed in 'ffff::ffff:ffff:ffff:ffff' will vary based on the host machine used.

Reference #2 (Example clientTest.py server-side output):
>Enter number 1: LeBron
>Invalid input. Please enter a number.
>Enter number 1: 23
>Enter number 2: James
>Invalid input. Please enter a number.
>Enter number 2: 6
>Enter operation: 65
>Invalid input. Please enter an operand without spaces. (+, -, /, or *)
>Enter operation: *
>Received '138.0'

---

[Version Info]

Version: 1.0

This code was created by Drew Gallagher for a Beacon Hill coding test on 2024/06/27, and was tested on Microsoft Windows 10 Home.
Start time: 2:10PM, US EST
End time: 3:45PM, US EST

Please contact me at dgallagher7@student.cscc.edu if you have any questions.

---
