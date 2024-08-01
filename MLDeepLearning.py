import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np 

# Define model
model = Sequential([
    Dense(10, activation='relu', input_shape=(4,)),
    Dense(3, activation='softmax')
])

# Compile model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Example data
X_train = np.random.random((100, 4))
y_train = np.random.randint(3, size=(100,))

# Train model
model.fit(X_train, y_train, epochs=5)
