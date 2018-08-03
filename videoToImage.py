import cv2
import sys


def videoToImage(skip_second, frames, source, destination):

    '''We will first get video'''
    video = cv2.VideoCapture(source)

    '''Total number of frames in video'''
    number_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    '''Frames per second'''
    fps = int(video.get(cv2.CAP_PROP_FPS))

    '''We skip few seconds of video , since it contains opeing sequence and menu'''
    xth_frame = int((number_frames - skip_second * fps)/frames)

    frame_count = 0
    img_title = 0
    success,image = video.read()

    while success :
        '''We read image and check if video has ended or not'''
        success, image = video.read()

        if frame_count > fps * skip_second:

            '''break if video has ended'''
            if not success:
                break

            '''store every xth_frame image'''
            if frame_count % xth_frame == 0:
                '''resizing image : 64x64'''
                image = cv2.resize(image, (64, 64))

                '''converting image to gray-scale'''
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                '''Writing image to destination'''
                cv2.imwrite(destination + str(img_title) + '.png', image)
                img_title += 1
                print(img_title)

            '''break the loop if we get given number of frames'''
            if frames == img_title:
                break

        frame_count += 1

'''
    We will skip 60 seconds
    Number of images  = 5000
    Providing video as command line argument 1
    Destination of storage is given by command line argument 2
'''

videoToImage(60, 5000, sys.argv[1], sys.argv[2])
