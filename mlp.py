import numpy as np
import os
import dtdata as dt
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import RMSprop, Adam



# fix random seed for reproducibility
np.random.seed(90210)

num_classes = 5
batch_size = 512
epochs = 2000

input_size = 512

subset = -1 # -1 to use the entire data set

path =r'/home/suroot/Documents/train/daytrader/ema-crossover' # path to data
(data, labels_classed) = dt.cacheLoadData(path, num_classes, input_size)
x_train, x_test, y_train, y_test = train_test_split(data, labels_classed, test_size=0.1)

model = Sequential()
model.add(Dense(128, activation='relu', input_dim=input_size))
model.add(Dropout(0.4))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer=Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False),
              metrics=['accuracy'])

history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=2,
                    validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])              