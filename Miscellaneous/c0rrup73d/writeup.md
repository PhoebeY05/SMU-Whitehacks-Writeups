# Description
50... my fr13nd 64v3 m3 7h15 f1l3 bu7 175 0bv10u5ly c0rrup73d 4nd 1 c4n'7 533 wh47'5 1n51d3. c4n y0u h3lp m3?

`c0rrup73d.png`
# Steps
1. Open c0rrup73d.png in a hex editor (https://hexed.it/)
    - Comparing its header with normal PNG headers (found in https://www.garykessler.net/library/file_sigs.html), we can see that it's first two bytes are incorrect (supposed to be 89 50 instead of 01 01)
    - Replace the first two bytes with the correct byte and download the fixed image (test.png)
2. After opening test.png, we realise that it is still not clear what the flag is => put the image in Google Lens
    - It might not be that obious at first but after minimising the search area (as shown below), we can see that it is similar to the Dancing Men Cipher
      |Original|Minimised|
      | -------------- | -------------- |
      | ![image](https://github.com/PhoebeY05/SMU-Whitehacks-Writeups/assets/115935747/a9058b1d-10dd-4854-8289-00025afced79) | ![image](https://github.com/PhoebeY05/SMU-Whitehacks-Writeups/assets/115935747/7fa488f2-81e9-4528-8664-9c33d1dac68f)  |
3. Use https://www.dcode.fr/dancing-men-cipher to decrypt the flag
    - Match the symbols in the image to the ones in the website and press 'decrypt' after inputting all the symbols to get the flag
