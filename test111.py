left = Sequential()
left.add(LSTM(...)

right = Sequential()
right.add(LSTM(..., go_backwards=True))

model = Sequential()
model.add(Merge([left, right], mode='sum'))

model.add(Dense(nb_classes))
model.add(Activation('softmax'))
