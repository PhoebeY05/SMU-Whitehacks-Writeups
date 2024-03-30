# Description
|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|
5 I recently intercepted some network traffic and I need some help analysing the traffic for any juicy information that can be important. Will you help me? 8
|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85|58|85| 

[Simple_Networking.pcapng](https://github.com/PhoebeY05/SMU-Whitehacks-Writeups/blob/main/Forensics/Simple%20Networking/Simple_Networking.pcapng)
# Steps
1. Follow a random TCP stream => observe that there is a number (e.g. 10)


https://github.com/PhoebeY05/SMU-Whitehacks-Writeups/assets/115935747/45d2b6d0-7577-4492-bd0d-93c0c62b6d05


2. Start from 0 and check every TCP stream => realise that an encrypted version of the flag is at 2
  

https://github.com/PhoebeY05/SMU-Whitehacks-Writeups/assets/115935747/05549f09-6f30-400a-a11b-d66657475016

3. Copy encrypted flag to CyberChef and use the magic wand to decrypt the flag


https://github.com/PhoebeY05/SMU-Whitehacks-Writeups/assets/115935747/118a8436-73dc-477b-bcbb-283cdc3150e7

