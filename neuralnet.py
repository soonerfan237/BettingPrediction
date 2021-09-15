import tensorflow as tf
import get_inputs
import numpy as np

def NeuralNet(input_file):
    print("STARTING NeuralNet")
    betting_lines = get_inputs.get_bettinglines(input_file)
    x_train_list = []
    y_train_list = []

    for row in betting_lines:
        y_train_list.append(row["hometeambeatspread"])
        x_train_list.append(np.array([[1, 1]], np.int32))

    y_train = np.array(y_train_list)
    x_train = np.array(x_train_list)

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(1, 2)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10)
    ])
    print("model")

    predictions = model(x_train[:1]).numpy()
    print("predictions")
    predictions
    tf.nn.softmax(predictions).numpy()
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    loss_fn(y_train[:1], predictions).numpy()
    model.compile(optimizer='adam',
                  loss=loss_fn,
                  metrics=['accuracy'])
    print("compile")

    model.fit(x_train, y_train, epochs=5)

    print("done")