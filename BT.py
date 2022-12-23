#import os
#os.environ["TF_MIN_GPU_MULTIPROCESSOR_COUNT"] = "1"

import BTClean

import warnings
warnings.filterwarnings('ignore')

from numpy import array
from pickle import dump, load
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.models import Sequential, load_model
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Embedding

# load doc into memory
def load_doc(filename):
 # open the file as read only
 file = open(filename, 'rb')
 # read all text
 text = file.read()
 # close the file
 file.close()
 return text.decode()

# load
in_filename = 'CBT.txt'
doc = load_doc(in_filename)
lines = doc.split('\n')

try:
 tokenizer = load(open('tokenizer.pkl', 'rb'))
except FileNotFoundError:
 # integer encode sequences of words
 tokenizer = Tokenizer()
 tokenizer.fit_on_texts(lines)
 # save the tokenizer
 dump(tokenizer, open('tokenizer.pkl', 'wb'))
sequences = tokenizer.texts_to_sequences(lines)
# vocabulary size
vocab_size = len(tokenizer.word_index) + 1

# separate into input and output
sequences = array(sequences)
X, y = sequences[:,:-1], sequences[:,-1]
y = to_categorical(y, num_classes=vocab_size)
seq_length = X.shape[1]

neurons = 400

try:
 model = load_model('model.h5')
except OSError:
 # define model
 model = Sequential()
 model.add(Embedding(vocab_size, BTClean.vocab_size, input_length=seq_length))
 model.add(LSTM(neurons, return_sequences=True))
 model.add(LSTM(neurons))
 model.add(Dense(neurons, activation='relu'))
 model.add(Dense(vocab_size, activation='softmax'))
 print(model.summary())
 # compile model
 model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
while True:
 try:
  # fit model
  model.fit(X, y, batch_size=1280, epochs=1)
 except KeyboardInterrupt:
  break
 # save the model to file
 model.save('model.h5')
