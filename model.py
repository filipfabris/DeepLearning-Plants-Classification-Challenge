import os
import tensorflow as tf
import numpy as np
import tensorflow.keras.layers as tfkl


IMG_SIZE = 224
def proc_input(X_input):
    X_input = tfkl.Resizing(IMG_SIZE, IMG_SIZE)(X_input)
    X_input = tf.cast(X_input, tf.float32)
    X_input = tf.keras.applications.efficientnet.preprocess_input(X_input)
    return X_input


class model:
    def __init__(self, path):
        self.model = tf.keras.models.load_model(os.path.join(path, "SubmissionModel"))

    def predict(self, X):
        X = X.numpy()
        X = proc_input(X)
        # Note: this is just an example.
        # Here the model.predict is called, followed by the argmax
        out = self.model.predict(X)

        cleaned_output = []
        for o in out:
            cleaned_output.append(o[0])


        # Convert the output to a single integer, 0 for healthy, 1 for unhealthy
        # out = np.argmax(out, axis=1)
        cleaned_output = np.around(cleaned_output).astype(int)
        output = tf.convert_to_tensor(cleaned_output)

        return output
