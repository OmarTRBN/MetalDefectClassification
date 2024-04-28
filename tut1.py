import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
# x = tf.constant(4)
x = tf.zeros((3,3))
print(x)
print(1)

y=tf.range(9)
z=tf.reshape(y, (3,3))
print(y)
print(z)