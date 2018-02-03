# This file loads the data from training_data.txt and test_data.txt and the
# dumps them using pickle

import numpy as np
import pickle

labels = np.genfromtxt("training_data.txt", dtype = str, max_rows = 1)
word_labels = labels[1:]

raw_training_data = np.genfromtxt("training_data.txt", skip_header = 1)
x_train = raw_training_data[:, 1:]
y_train = raw_training_data[:, 0]

x_test = np.genfromtxt("test_data.txt", skip_header = 1)

# Dump the data
pickle.dump(word_labels, open("word_labels.p", 'wb'))
pickle.dump(x_train, open("x_train.p", "wb"))
pickle.dump(y_train, open("y_train.p", "wb"))
pickle.dump(x_test, open("x_test.p", "wb"))
