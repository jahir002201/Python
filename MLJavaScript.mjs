// TensorFlow.js Example: Simple Linear Regression

import * as tf from '@tensorflow/tfjs';

// Define a simple model
const model = tf.sequential();
model.add(tf.layers.dense({ units: 1, inputShape: [1] }));

// Compile the model
model.compile({
  optimizer: 'sgd',
  loss: 'meanSquaredError' 
});

// Example data
const xs = tf.tensor1d([1, 2, 3, 4]); 
const ys = tf.tensor1d([1, 3, 5, 7]); 

// Train the model
model.fit(xs, ys, { epochs: 10 }).then(() => {
  // Make predictions
  const prediction = model.predict(tf.tensor1d([5]));
  prediction.print(); 
});
