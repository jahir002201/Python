import tensorflow as tf

# Define tensors
tensor1 = tf.constant([[1, 2], [3, 4]])
tensor2 = tf.constant([[5, 6], [7, 8]])

# Tensor addition
tensor_sum = tf.add(tensor1, tensor2)

# Tensor multiplication
tensor_product = tf.matmul(tensor1, tensor2)

print("Tensor Addition:\n", tensor_sum.numpy())
print("Tensor Multiplication:\n", tensor_product.numpy())
