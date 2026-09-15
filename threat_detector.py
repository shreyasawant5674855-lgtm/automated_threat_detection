import pandas as pd
import joblib


def detect_threat(model, bytes_value, packets_value):
    data = pd.DataFrame(
        [[bytes_value, packets_value]],
        columns=["bytes", "packets"]
    )

    prediction = model.predict(data)

    if prediction[0] == 1:
        return "Threat Detected"
    else:
        return "Normal Activity"