# tensorflow_tutorial
<h1>A brief introduction to tensorflow<h1>

<h2>Step 1: background on tensorflow</h2>
<ul>
  <li>Tensor: an array or matrix of values</li>
  <li>Method of defining tensors and operations on tensors</li>
  <li>Each operation of two tensors returns another tensor</li>
  <li>Tensorflow defines many useful operations out of the box (such as softmax), making it easy to create neural nets</li>
  <li>Tensorflow lets you define tensors and operations in python, and then runs them very efficiently in C, only returning to python after all computation is finished</li>
</ul>

<h2>Step 2: installation</h2>
<ul>
  <li>Windows: install natively with pip or use conda</li>
  <li>Linux and Mac: install with pip or with virtualenv</li>
  <li>If using conda, follow conda installation wizard</li>
  <li>With pip, simply run pip3 install --upgrade tensorflow</li>
</ul>

<h2>Step 3: playing with tf</h2>
<ul>
  <li>open up an interactive console and start python</li>
  <li>let's simply compute the dot product of two tensors X, Y using tf</li>
  <li>to create a tensor X, use tf.placeholder()</li>
  <li>"X*Y" is a shorthand for matrix multiplication; this will multiply our tensors</li>
  <li>to actually begin computation, define an interactive session and use it to evaluate our tensors</li>
 </ul>

Code:
>>>X = tf.placeholder(tf.float32,[3], name='X')
>>>Y = tf.placeholder(tf.float32,[3], name='Y')
>>>mult = X * tf.transpose(Y)
>>>sess = tf.InteractiveSession()
>>>sess.run(mult, feed_dict={X:[1,2,3], Y:[1,2,3]})

<h3>Step 4: your first neural network</h3>
Follow the instructions at https://www.tensorflow.org/versions/r1.1/get_started/mnist/beginners
