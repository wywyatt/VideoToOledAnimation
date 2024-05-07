#   Video to 128x32 Oled Animation!
#
#   I made this program to add some nice effects like dithering to short clips, for use on a proffie oled
#   Should be pretty simple, most of it was haggled together using existing snippets of code in stack overflow comments :p and chatgpt of course
#
#   - WyWyatt
#      5/7/24
#
#   stack overflow credit to: user13074756, Jeru Luke, and Mark Setchell


from PIL import Image
import os
import cv2

def main():
    video_path = input("Please input video path\nEX: D:/oledimages/video/video.mp4\n")
    current_directory = os.getcwd()
    folder_name = "oledanimation_frames"
    image_path = os.path.join(current_directory, folder_name)
    video = cv2.VideoCapture(video_path)
    
    palIm = Image.new('P', (1,1))
    palette = [255, 255, 255 ] + [0, 0 ,0] * 255
    palIm.putpalette(palette)
    
    if not os.path.exists(image_path):
        # If it doesn't exist, create the folder
        os.makedirs(image_path)
        print(f"Image folder created successfully at '{image_path}'")
    else:
        print(f"Image folder exists at '{image_path}', it will be written over.")
    

    # Check if the video file was opened successfully
    if not video.isOpened():
        print("Error: Unable to open video file")
        exit()
    else:
        print("Video Opened! Beginning process. Frames will be in " + str(image_path))

    # Get some properties of the video
    curr_frame = 0
    
    while True:
        ret, frame = video.read()

        if not ret:
            break

        name = os.path.join(image_path, str(curr_frame) + ".png")

        resized_image = cv2.resize(frame, (128, 32))

        cv2.imwrite(name, resized_image)

        # process frame using PIL
        img = Image.open(name).convert("RGB").quantize(colors=2, method=0, kmeans=2, palette=palIm, dither=Image.Dither.FLOYDSTEINBERG)
        img.save(name)
        
        curr_frame += 1

    video.release()

main()
