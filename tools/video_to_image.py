
import os
import cv2 as cv


def viedo_to_image(video_path, path, catalog, start_name=0,interval=50):
    capture = cv.VideoCapture(video_path)
    if (capture.isOpened() == False):
        print("Error opening the video file")
    else:
    	# Get frame rate information
        # You can replace 5 with CAP_PROP_FPS as well, they are enumerations
        fps = capture.get(5)
        print('Frames per second : ', fps,'FPS')

        # Get frame count
        # You can replace 7 with CAP_PROP_FRAME_COUNT as well, they are enumerations
        frame_count = capture.get(7)
        print('Frame count : ', frame_count)
        
        if not os.path.exists(path):
            os.makedirs(path)
            print(path,' creat success!!')

    frame_n = 0
    frame_save = 0
    while(capture.isOpened()):
            # vid_capture.read() methods returns a tuple, first element is a bool 
        # and the second is frame
        ret, frame = capture.read()
        if ret == True:
            frame_n+=1
            if frame_n % interval == 0:
                image_name = format(catalog, '03d')+'-'+format(start_name+frame_save, '06d')+'.png'
                image_path = os.path.join(path,image_name)
                cv.imwrite(image_path, frame)
                print(image_path, " save successs!!")
                frame_save+=1
            
        else:
            break
    capture.release()

def main():
    viedo_to_image('C:\\Users\\lenovo\\Desktop\\20230508100718.mp4','C:\\Users\\lenovo\\Desktop\\1',0,0)

if __name__ == '__main__':
    main()