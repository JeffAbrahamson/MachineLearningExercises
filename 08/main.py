import time
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
import cv2
from network import Network

# Here we instantiate a network with 10 neurones of 64 element
NET = Network(10, 64)

# We load the data
dataset = datasets.load_digits()
data = dataset['data']
target = dataset['target']

# We split it to ensure the train and test sets are 
# well separated
x_train, x_test, y_train, y_test = train_test_split(
            data, target,
            test_size=0.3)
# We then fit the data on our network
# The show_weigth argument tell if you wan't to
# display the neurons memory state
NET.fit(x_train, y_train, show_weigth=True)
time.sleep(3)
# We use the test set to test our network
results = NET.test(x_test, y_test)

# We then display the results
print(f'Using nothing but the dataset and train test split from sklearn')
print(f'This neural network achieve a {results[0]*100:.2f} % correctness')
print(f'with {results[1]} values correctly predicted out of {len(x_test)} values')
