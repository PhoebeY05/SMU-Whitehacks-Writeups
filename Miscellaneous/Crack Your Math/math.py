import telnetlib
import numexpr
HOST = "ctf2.whitehats.site"
PORT = 4001

tn = telnetlib.Telnet(HOST, PORT)
def remove(string):
    return string.replace(" ", "")
    
while True:
    tn.read_until(b"/ 123\n")
    question = tn.read_until(b"\n").decode()
    question = remove(question)
    result = numexpr.evaluate(question).item()
    print(result)
    tn.write(str(result).encode())
