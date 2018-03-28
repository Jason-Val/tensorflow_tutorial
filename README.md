<h1>A brief introduction to tensorflow<h1>
<p>Download tensorflow at https://www.tensorflow.org/install/</p>
<p>If using conda, download at https://conda.io/docs/user-guide/install/download.html</p>
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
<p>>>>X = tf.placeholder(tf.float32,[3], name='X')</p>
<p>>>>Y = tf.placeholder(tf.float32,[3], name='Y')</p>
<p>>>>mult = X * tf.transpose(Y)</p>
<p>>>>sess = tf.InteractiveSession()</p>
<p>>>>sess.run(mult, feed_dict={X:[1,2,3], Y:[1,2,3]})</p>

<h3>Step 4: your first neural network</h3>
<p>Follow the instructions at https://www.tensorflow.org/versions/r1.1/get_started/mnist/beginners</p>
<p>These instructions are for an outdated version of tensorflow, but still work. I choose this tutorial because it is very simple, and exposes the math behind the neural network. More recent tutorials focus on data manipulation/feature extraction and use of the high level estimators API.</p>
<p>Those wishing more experience with ML and tensorflow should follow the more recent tutorial, available here: https://www.tensorflow.org/get_started/get_started_for_beginners</p>
