import sys
sys.path.append('.')
import imagesToData as ia
import pickle

'''Getting scaled data from image and assigning Mario 1 and Wario 0 '''
x,y = ia.dataRetriever()
print("Data Retrieved")

'''
    Splitting data into training and testing data set
    testing data set is 20% of total dataset
'''
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
print("Divided data into train dataset and test dataset")

'''
    Scaling Features using Z-Score method
    fit_transform() : evaluate mean
    transform() : use mean evaluated by mean
'''
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
print("Features Scaled")

'''
    Fitting Logistic Regression to the Training Set
    Shuffling data to reduce variance and to make sure model overfit less thus setting random_state (seed)
'''
from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression(random_state = 0)
log_reg.fit(x_train, y_train)
print("Model Trained")

'''Predicting the Test set results'''
y_pred = log_reg.predict(x_test)


'''
    Making confusion matrix
    Confusion matrix stores correct prediction and incorrect prediction
    that our model made on the test
'''
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

'''Calculating Accuracy'''
true_pos = cm[1][1]
true_neg = cm[0][0]
false_pos = cm[0][1]
false_neg = cm[1][0]

accuracy = 100*(true_pos+true_neg)/(len(x_test))
print("{}%".format(accuracy))

'''Dumping model in pickle file'''
pickle_file = 'LogRegPickle.pkl'
log_reg_pkl = open(pickle_file,'wb')
pickle.dump(log_reg, log_reg_pkl)
log_reg_pkl.close()
