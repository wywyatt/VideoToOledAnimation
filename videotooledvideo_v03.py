#   Video to 128x32 Oled Animation!
#
#   I made this program to add some nice effects like dithering to short clips, for use on a proffie/cfx oled
#   Should be pretty simple, most of it was haggled together using existing snippets of code in stack overflow comments :p and chatgpt of course
#
#   - WyWyatt
#      5/7/24
#
#   stack overflow credit to: user13074756, Jeru Luke, and Mark Setchell

import os
import importlib.util
import subprocess
import shutil

try:
    import cv2
except ImportError:
    print("OpenCV is not installed. Installing...")
    subprocess.check_call(["pip", "install", "opencv-python"])
    print("OpenCV has been installed successfully.")

try:
    from PIL import Image
except ImportError:
    print("PIL is not installed. Installing...")
    subprocess.check_call(["pip", "install", "pillow"])
    print("PIL has been installed successfully.")

import cv2
from PIL import Image, ImageOps


def scale(scaleinput, frame):
    if scaleinput == "stretch":
        scalemethod = cv2.resize(frame, (128, 32))
        return scalemethod
    elif scaleinput == "zoom":
        scale_factor = 128 / int(frame.shape[1])
        scalemethod = cv2.resize(frame, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
        return scalemethod

def main():
    frames = []
    current_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    image_path = os.path.join(current_directory, "oledanimationTEMPFRAMES")
    video_path = input("Please input video path, ex: D:/oledimages/video/video.mp4: ")
    video = cv2.VideoCapture(video_path)
    
    palIm = Image.new('P', (1,1))
    palette = [0, 0, 0] + [255, 255, 255] * 255
    palIm.putpalette(palette)

    # Check if the video file was opened successfully
    while video.isOpened() == False:
        print("Error: Unable to open video file. Please check video formatting.")
        video_path = input("Please input video path, ex: D:/oledimages/video/video.mp4: ")
        video = cv2.VideoCapture(video_path)

    # ask user for shading preference
    if input("Shading? (Yes or No): ").lower() == "yes":
        ditherchoice = Image.Dither.FLOYDSTEINBERG
    else:
        ditherchoice = 0

    #get user input for scale choice
    scaleinput = input("Scale method? (stretch, zoom, or none): ").lower()

    # get gif choice
    gifchoice = input("Would you like a GIF preview? (yes or no): ").lower()
    
    print("Cooking images now..")
    
    #check if folder exists for temp_images,
    if not os.path.exists(image_path):
        # If it doesn't exist, create the folder
        os.makedirs(image_path)

    # Calculate letterboxing thickness
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    lbox_height = sum(not row.any() for row in gray) // 2
    height = frame.shape[0]
    width = frame.shape[1]
    # Initialize video writer
    output_video = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 24, (width, (height - lbox_height * 2)))
    # Process and write frames
    while ret:
        cropped_frame = frame[lbox_height:height-lbox_height, :]
        output_video.write(cropped_frame)
        ret, frame = video.read()

    output_video.release()
    video.release()
    
    
    output_video = cv2.VideoCapture(str(current_directory) + r"\output_video.mp4")
    curr_frame = 0
    while True:
        ret, frame = output_video.read()

        if not ret:
            break

        name = os.path.join(image_path, str(curr_frame).rjust(5, '0') + ".png")

        resized_image = scale(scaleinput, frame)

        cv2.imwrite(name, resized_image)

        # process frame using PIL
        img = Image.open(name).convert("L").quantize(colors=2, method=0, kmeans=2, palette=palIm, dither=ditherchoice)
        img = Image.open(name).convert("1")
        img.save(name)
        
        curr_frame += 1

    output_video.release()

    print("frames produced: " + str(curr_frame))

    if gifchoice == "yes":
        print("Making gif...")
        #check gif number
        n = 0
        while os.path.exists(os.path.join(current_directory, "gifpreview" + str(n) + ".gif")):
            n += 1
        #create gif list
        for filename in os.listdir(image_path):
            filepath = os.path.join(image_path, filename)
            frames.append(Image.open(filepath))
        #create gif using list
        frames[0].save(os.path.join(current_directory, "gifpreview" + str(n) + ".gif"), save_all=True, append_images=frames[1:], duration=42, loop=0)

    # Open all images and calculate total height
    images = [Image.open(os.path.join(image_path, f"{i}.png")) for i in range(curr_frame)]
    total_height = sum(img.height for img in images)

    # Create a blank image with total height
    combined_image = Image.new('1', (128, total_height))

    # Paste each image onto the combined image
    y_offset = 0
    for img in images:
        combined_image.paste(img, ((128 - img.width) // 2, y_offset))
        y_offset += img.height

    
    # check for what number image this is
    n = 0
    while os.path.exists("final_animation" + str(n) + ".bmp"):
        n += 1
    
    ImageOps.invert(combined_image).save("final_animation" + str(n) + ".bmp")
    #delete temp folder
    #shutil.rmtree(image_path)
    os.remove("output_video.mp4")
    
    print("\nDone! Your image is saved in the same folder as this script, and titled final_animation.bmp\nHave a good one :)")

try:
    main()
except Exception as e:
    print("An error occurred:", e)
    input("Press Enter to exit...")
