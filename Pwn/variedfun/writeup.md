# Description
It is time to learn about Buffer Overflow.  Overwrite target to get the flag

[variedfun.c](https://github.com/PhoebeY05/SMU-Whitehacks-Writeups/blob/main/Pwn/variedfun/variedfun.c)
# Steps
1. From variedfun.c, we can infer that we need to input more than 64 characters to change `target`.
```c
volatile int target; // this guy here is one you want to change
char buffer[64] = {0x00}; // this guy here can fit 64 characters

target = 0;

printf("Target is currently set to %d, overflow buffer and change 'target'!\n", target);
printf("Gimme input: ");
gets(buffer); // gets is an insecure function that allows you to input as many characters as you want to buffer.
```
2. From the code, we can also see that we need to change `target` to get the flag.
```c
if (target != 0) { // target originally set to 0
  printf("You have changed the 'target' variable!\n");
  win(); // Outputs flag
} else {
  printf("Nope, target is still %d\n", target);
}
```
3. In the server, input more than 64 characters to get the flag.
  - To get more than 64 characters (e.g. 100) quickly, open another tab in the terminal and input the `python` before inputting `'A' * 100` to get 100 As.
    
