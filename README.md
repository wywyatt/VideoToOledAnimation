Howdy! This program allows people to take animations or movie clips, and convert them to proffie/cfx OLED animations.
It currently runs on python 3.12.3 --on windows this is the same one in the microsoft store. To run the program, just install python, and double click the script. :) Message me if you have any problems, I'm in the r/lightsabers discord, @__wyatt

CONFIGURING:
 - The current user input options allow selection of dithering. Dithering allows for false-shading on low quality images that require gradients to be perceivable. The current dithering method uses floyd-steinberg, and you can also choose no dithering if you'd like no shading. A good example of when to use no shading is after making a plain unshaded text animation video, and wanting to render that out as a proffie image.
You should use dithering for the majority of movie clips however. 
Select either Yes to choose floyd-steinberg, or No for solid colors.

 - The second option is the zoom/crop option. Current choices are stretch, zoom, or none. Stretch will stretch your video hoizontally to fit the 128 pixel width, leaving the top and bottom border the same, but zoom will crop into your video, zooming in until the width of the video fits into the 128 long ratio. This typically cuts off a minor portion of the top and bottom. Usually, I default to zoom, but if the clip has important information in the top or bottom, I choose stretch. None is typical for text or premade animation videos that are already the right scale.

 - Lastly, Gif preview. This will generate a gif in the same output folder as where the script is placed, and allow you to test how it turned out! This means you can veiw from your computer if you chose a good crop method instead of having to test it on a proffie. You can also verify this using the generated bmp, but those are inverted, so that can be difficult.

Supported video formats are AVI, MP4, MKV, MOV, MPEG, WMV, FLV, ASF. There is also more, but that's the main gist of it.
There is a time limit to the videos, I'm not sure what it is. I think around 2 minutes long and your proffie will run out of memory.


Feel free to message me in the r/lightsabers discord, @__wyatt
