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


def dataRetriever(selector):
    '''
        Assigning 1 to Mario and 0 to Wario
        selector lets you select data set
        1 : training data set
        0 : testing data set
    '''

    if(selector == 1):
        x_train = []
        y_train = []
        #Mario
        for img in glob.glob('resources/Images/Train/Mario/*.png'):
            image = process_image(img)
            x_train.append(image)
            y_train.append(1)

        #Wario
        for img in glob.glob('resources/Images/Train/Wario/*.png'):
            image = process_image(img)
            x_train.append(image)
            y_train.append(0)
        return x_train, y_train

    if(selector == 0):
        x_test = []
        y_test = []
        # Mario
        for img in glob.glob('resources/Images/Test/Mario/*.png'):
            image = process_image(img)
            x_test.append(image)
            y_test.append(1)

        # Wario
        for img in glob.glob('resources/Images/Test/Wario/*.png'):
            image = process_image(img)
            x_test.append(image)
            y_test.append(0)
        return x_test, y_test