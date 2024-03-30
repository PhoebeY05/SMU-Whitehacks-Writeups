# Description
"Oh noooo I forgot my credentials to the server! I'm pretty sure I wrote it somewhere the source code but I can't figure out where!"

[login.c](https://github.com/PhoebeY05/SMU-Whitehacks-Writeups/blob/main/Pwn/login/login.c)
[login](https://github.com/PhoebeY05/SMU-Whitehacks-Writeups/blob/main/Pwn/login/login)
[Makefile](https://github.com/PhoebeY05/SMU-Whitehacks-Writeups/blob/main/Pwn/login/Makefile)
# Steps
Disclaimer: Only login.c was used in my solution
1. From login.c, we can see that the program compares the input at login with "Weje\n" to move on
```c
if (strcmp(buffer, "Weje\n") == 0){ //Comparing strings
  printf("%s", "Password: "); //Prompting for password
  fgets(buffer, sizeof(buffer), stdin; //Getting input
  ...
```
2. Afterwards, the program compares "P@SSW0RD\n" to the password input to output the flag
```c
if (strcmp(buffer, "P@SSW0RD\n") == 0){
  printf("%s\n", "Login passed! Here is your flag.");
  print_flag();
} 
```
3. Hence, by inputting Weje & P@SSW0RD in the server when prompted, we can obtain the flag
