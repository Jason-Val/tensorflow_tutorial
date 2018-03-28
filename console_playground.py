# This file shows some basic interactions with how to interact with numpy as tensorflow
# It also briefly explains some of the linear algebra used by tensorflow

import numpy as np
import tensorflow as tf

# -------------The numpy demo:-------------

# Defining a simple array. Try checking A.shape!
# This array could define the input to a neural network.
# Each row represents the input for one sample. 
# The array together, two samples, is a batch.
A = np.array([[1,2,3], [4,5,6]])

# A simple array of weights. Its shape is (3,2)
W = np.array([[1,2],[2,3],[3,4]])

# One sample:
# This is roughly equivalent to feeding one sample through a layer
# of a network (except with out a bias or activation function).
# This represents an input of 3 values fed into a hidden layer H of 
# just 2 neurons.
# In the weight matrix, an element i, j represents the weight
# between A[i] and H[j]
H_1 = np.matmul(A[0], W)

# A second sample:
H_2 = np.matmul(A[1], W)

# A full batch calculation:
# Note that the output H_b[0] = H_1, and H_b[1] = H_2
H_b = np.matmul(A, W)


# -------------The tensorflow demo:-------------

# A placeholder variable is a tensor "waiting" for its value to be
# determined on runtime by a feed_dict. We define two arrays of length 3.
X = tf.placeholder(tf.float32,[3], name='X')
Y = tf.placeholder(tf.float32,[3], name='Y')

# We define a relation between X,Y; their dot product, which also outputs
# a tensor
mult = X * tf.transpose(Y)

#Finally, we create a session and use it to compute the dot product
sess = tf.InteractiveSession()
sess.run(mult, feed_dict={X:[1,2,3], Y:[1,2,3]})