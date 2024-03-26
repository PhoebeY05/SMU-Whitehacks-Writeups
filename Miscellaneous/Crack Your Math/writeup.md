# Steps
1. Connect to the server provided using Python
```python
import telnetlib
HOST = "ctf2.whitehats.site"
PORT = 4001

tn = telnetlib.Telnet(HOST, PORT)
```
2. For every question (while loop), stop at the heading (Question ? / 123) and assign the equation (in text form) to a variable (`question`)
     - Remove spaces in the equation (`question`) to ensure easy evaluation using `numexpr`
```python
while True:
    print(tn.read_until(b"/ 123\n"))
    question = tn.read_until(b"\n").decode()
    question = remove(question)
```

3. Evaluate the equation and send it to the server => After this happens 123 times, the server will print out the flag
```python
result = numexpr.evaluate(question).item()
tn.write(str(result).encode())
```
