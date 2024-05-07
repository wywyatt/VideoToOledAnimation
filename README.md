Howdy! This program allows people to take animations or movie clips, and convert them to proffie OLED animations.
It currently runs on python 3.12.3, and uses CV2, and PIL libraries.
Supported video formats are AVI, MP4, MKV, MOV, MPEG, WMV, FLV, ASF. There is also more, but that's the main gist of it.

The only preprocessing you'll have to do is getting rid of the letterboxing (top and bottom black trim bars on movie clips), and adjusting the time to the write clip section you want.

When running the program, you can either double click on it, or execute from terminal.
Copy and paste the video file path into the terminal, being sure there's no quatations surrounding it, and it matches the format of the example.

The dithering method uses floyd-steinberg, and you can also choose no dithering if you'd like no shading.

A good example of when to use no shading is after making a plain unshaded text animation in after effects, and wanting to render that out as a proffie image.
You should use dithering for the majority of movie clips however.

Feel free to message me in the r/lightsabers discord, @__wyatt
