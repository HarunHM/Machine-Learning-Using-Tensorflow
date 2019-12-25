# Code starts here
import tensorflow as tf

# As we are told that numbers won't change 
# so it's safe to assume it as tensorflow constant
a = tf.constant(5,name="a")
b = tf.constant(15,name="b")

# Now we have to add a and b.
# tenorflow provides add function for same.
# https://www.tensorflow.org/api_docs/python/tf/add
c = tf.add(a,b,name="c")

# Tensor flow creates graph and doesn't run the graph till
# you run the graph in a session. 
# So if we try printing value of c at this point
# we will get the output as a tensor and not actual value of c
# This is because value of c is not computed till we demand 
# value of c, (and this is done by sess.run() )
print("Value of c before running tensor:",c)
# A new session is created using tf.Session() call.
sess = tf.Session()

# now we need to run graph we created
# c is passed as input to run as we need 
# to run graph till value of c is obtained.
output = sess.run(c)
print("Value of c after running graph:",output)

# Once we are done we need to close the session.
sess.close()

# code ends here
