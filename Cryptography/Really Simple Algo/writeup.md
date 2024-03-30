# Description
Read this description Super Attentively and you may identify this Algorithm.
# Steps
1. As always, the first step is to search online for information => Google search "How to decrypt rsa with p, q, e and ct"
   - Go to the first result: https://crypto.stackexchange.com/questions/19444/rsa-given-q-p-and-e => use the python script with the challenge parameters (chall.txt) in the answer to get n and plaintext
     ```python
     def egcd(a, b):
         x,y, u,v = 0,1, 1,0
         while a != 0:
             q, r = b//a, b%a
             m, n = x-u*q, y-v*q
             b,a, x,y, u,v = a,r, u,v, m,n
             gcd = b
         return gcd, x, y
     
     def main():
     
         p = 78865424389377580794175840656878497522070744823516059929763310335130657053543
         q = 61712276178318104198336108158961626115735728990809882884697212881595682247381
         e = 65537
         ct = 3437020306843672887032634854973978032984503348466065504155397633240945809923068309405041104502857310573065954098228505593605737851805577310690096298267989
         # compute n
         n = p * q
     
         # Compute phi(n)
         phi = (p - 1) * (q - 1)
     
         # Compute modular inverse of e
         gcd, a, b = egcd(e, phi)
         d = a
     
         print( "n:  " + str(d) );
     
         # Decrypt ciphertext
         pt = pow(ct, d, n)
         print( "pt: " + str(pt) )
     
     if __name__ == "__main__":
         main()
     ```
     - You should get the below output
     ```
     n:  -1778001319235732972210427202684463813787485214456624814359042112783495366956711110643813810257885313964453042485023838747547137695856088866256151612423887
     pt: 2587281142716183579091294436010242006519012858701392238716794749970180637205476221
     ```
2. If you are like me and unable to decrypt the numerical version of the plaintext, go to https://github.com/RsaCtfTool/RsaCtfTool and choose the installation step that fits your operating system.
   ![image](https://github.com/PhoebeY05/SMU-Whitehacks-Writeups/assets/115935747/bafbd2c4-d3a7-4e24-90fc-9cd69928e446)
     - Use the **n** returned from above step and **e** from chall.txt as parameter for rsactftool
     - In the folder RsaCtfTool, open the terminal and input the following:
         ```bash
         ./RsaCtfTool.py -n -1778001319235732972210427202684463813787485214456624814359042112783495366956711110643813810257885313964453042485023838747547137695856088866256151612423887 -e 65537 --decrypt 3437020306843672887032634854973978032984503348466065504155397633240945809923068309405041104502857310573065954098228505593605737851805577310690096298267989
         ```

