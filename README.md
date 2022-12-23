# BT-AI
A.I. trained on all the articles from Corry Beaver Tales as of 12/16/22  
Model Summary:  
Layer (type),                Output Shape,             Param #   
_________________________________________________________________
embedding_1 (Embedding),     (None, 200, 200),         4220000   
lstm_1 (LSTM),               (None, 200, 400),         961600    
lstm_2 (LSTM),               (None, 400),              1281600   
dense_1 (Dense),             (None, 400),              160400    
dense_2 (Dense),             (None, 21100),            8461100   
_________________________________________________________________
Total params: 15,084,700  
Trainable params: 15,084,700  
Non-trainable params: 0  
=================================================================
# How to setup:
1. Download and install Python. https://www.python.org/downloads/
2. Download and install Keras through PIP. https://pypi.org/project/keras/
3. (Optional) For training, download and install h5py through PIP. https://pypi.org/project/h5py/
# How to use:
In cmd or powershell run: python BTCusGen.py  
The A.I. will generate each word one by one only if each is accepted, otherwise it will generate a new word in the rejected word's place.
