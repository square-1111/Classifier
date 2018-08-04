import glob
import cv2

'''
    Reading image converting it to greyscale and thus flattening the array
    :returns numpy.array
'''
def process_image(img):
    '''Reading image using opencv and selecting grayscale colortype (flag = 0)'''
    image = cv2.imread(img, 0)
    image = image.flatten()
    return image


def dataRetriever():
    '''
        Assigning 1 to Mario and 0 to Wario
    '''
    x = []
    y = []
    #Mario
    for img in glob.glob('resources/Images/Mario/*.png'):
        image = process_image(img)
        x.append(image)
        y.append(1)

    #Wario
    for img in glob.glob('resources/Images/Wario/*.png'):
        image = process_image(img)
        x.append(image)
        y.append(0)
    return x, y
