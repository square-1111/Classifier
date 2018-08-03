import pickle
import sys
import cv2

log_reg_pkl = open('LogRegPickle.pkl','rb')
log_reg = pickle.load(log_reg_pkl)
print(log_reg)

x_image = []
image = cv2.imread(sys.argv[1], 0)
image = cv2.resize(image, (64, 64))
x_image.append(image.flatten())

y_predict = log_reg.predict(x_image)

print("Given image is classified as:", end= ' ')
if y_predict :
    print("Mario")
else:
    print("Wario")
