import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical

# Parameters
vocab_size = 20  # Number of unique amino acids
embedding_dim = 128
lstm_units = 256
sequence_length = 50
batch_size = 64
epochs = 10

# Randomly generating sequences for demonstration
X_train = np.random.randint(0, vocab_size, (1000, sequence_length))
y_train = np.random.randint(0, vocab_size, (1000, sequence_length))

# Convert target to categorical
y_train = to_categorical(y_train, num_classes=vocab_size)

# Model architecture
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=sequence_length),
    tf.keras.layers.LSTM(lstm_units, return_sequences=True),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(vocab_size, activation='softmax'))
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

# Training the model
model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)

# Saving the model
model.save('beta_peptide_generator.h5')

# Inference
def generate_peptide(model, seed_sequence, length=sequence_length):
    for _ in range(length - len(seed_sequence)):
        padded_sequence = pad_sequences([seed_sequence], maxlen=length, padding='pre', value=0)
        prediction = model.predict(np.array(padded_sequence))
        next_aa = np.argmax(prediction[:, -1, :], axis=-1)
        seed_sequence.append(int(next_aa))
    return seed_sequence

# Generate a new sequence
seed_sequence = [np.random.randint(0, vocab_size)]  # Start with a random amino acid
generated_sequence = generate_peptide(model, seed_sequence)
print("Generated peptide sequence:", generated_sequence)
