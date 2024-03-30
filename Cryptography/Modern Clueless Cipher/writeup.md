# Description
After learning basic crypto cipher, I have encrypted the flag and provided you with the key as well. Decrypt it to get the flag.
BTW my keyboard keeps inputting f at regular intervals... 

[flag.txt](https://github.com/PhoebeY05/SMU-Whitehacks-Writeups/blob/main/Cryptography/Modern%20Clueless%20Cipher/flag.txt)

# Steps
1. We can search up the challenge name to check for any clues => Google Search "Modern Clueless Cipher"
    - The first result that pops up is a writeup in CTFHub: https://writeup.ctfhub.com/Challenge/2020/CSICTF/Crypto/tgGcJBgNzLkru7brJzXVDf.html
    - We can see that the challenge description is similar to the flag.txt given by our current challenge (proves we are on the right track)
2. Now, we can follow the steps of this writeup
    - Using https://www.rapidtables.com/convert/number/ascii-to-hex.html, we can convert "WH2024{" into hexadecimal bytes => 57 48 32 30 32 34 7B
      ![image](https://github.com/PhoebeY05/SMU-Whitehacks-Writeups/assets/115935747/a0c06749-25c7-46e9-be25-fc74aeac6d8e)
  
    - Next, we can use https://www.compscilib.com/calculate/binaryxor?variation=default set to hexadecimal (both input and output) to perform xor (**57 48 32 30 32 34 7B** from previous step and **1e 0b 77 79 71 71 32** from encypted message in flag.txt) => Output: **494345**49434549
      ![image](https://github.com/PhoebeY05/SMU-Whitehacks-Writeups/assets/115935747/0eed11d3-42e3-403e-ba71-50e5e0f63f5f)
    - Note: Difference between current challenge and writeup we are referring to = current challenge's key is the _repetitive 3 bytes_ instead of the _unit digit_ of the bytearray => 2 possible ways to continue:
  
      a) Assign key given in flag.txt to key variable in writeup
      
      b) Change `3` in writeup solution to `4` and `12123` to `935935`
3. I decided to go with b) as it conformed to the writeup solution better, lowering the possibility of any hiccups later on
4. Run the edited python script (mcc.py) to get the flag => WH2024{repeated_key_xor}
