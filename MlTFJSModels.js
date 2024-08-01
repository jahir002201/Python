const tf = require('@tensorflow/tfjs');

// Define the model
const model = tf.sequential();
model.add(tf.layers.dense({ units: 10, activation: 'relu', inputShape: [5] }));
model.add(tf.layers.dense({ units: 1, activation: 'linear' }));

// Compile the model
model.compile({ optimizer: 'adam', loss: 'meanSquaredError' });

// Example data
const X_train = tf.tensor2d([
  [0, 1, 2, 3, 4],
  [1, 2, 3, 4, 5],
  [2, 3, 4, 5, 6],
  [3, 4, 5, 6, 7]
], [4, 5]);

const y_train = tf.tensor2d([
  [1],
  [2],
  [3],
  [4]
], [4, 1]);

// Train the model
model.fit(X_train, y_train, {
  epochs: 10,
  batchSize: 1,
  callbacks: tf.callbacks.earlyStopping({ patience: 3 })
}).then(() => {
  // After training, make a prediction
  const testInput = tf.tensor2d([[4, 5, 6, 7, 8]], [1, 5]);
  const prediction = model.predict(testInput);
  prediction.print();  
});
