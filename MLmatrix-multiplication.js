const tf = require('@tensorflow/tfjs');

// Create tensors
const a = tf.tensor([[1, 2], [3, 4]]);
const b = tf.tensor([[5, 6], [7, 8]]);

// Perform matrix multiplication
const c = tf.matMul(a, b);

// Print the result
c.print();
