# Description
Can you bypass this super easy authentication that was created by me? Guest Login are available via :

Username: guest

Password: guest

Connect at http://localhost:15011/

# Steps
1. Login with the credentials given
2. Check the cookies in Google Developer Tools -> Applications
     - Realise that the username is used for authentication
<img width="1470" alt="guest" src="https://github.com/PhoebeY05/SMU-Whitehacks-Writeups/assets/115935747/794c4189-233d-46fa-9ce1-ba4b43f2e6b6">
3. Continue on to the next page => Requires administrator rights
     - Can infer that we need to change username to administrator
<img width="1470" alt="admin" src="https://github.com/PhoebeY05/SMU-Whitehacks-Writeups/assets/115935747/3ee35783-6c84-45fd-ab87-2cd511043b24">
4. Change cookie in Application tab and continue on to next page to get the flag

https://github.com/PhoebeY05/SMU-Whitehacks-Writeups/assets/115935747/abefda09-6423-4e34-a100-4749e92b26dd

