import pandas as pd


def detect_threat(model, bytes_value, packets_value):

    # Validate input values
    try:
        bytes_value = float(bytes_value)
        packets_value = float(packets_value)
    except (ValueError, TypeError):
        raise ValueError("Bytes and packets must be numeric values.")

    # Prevent invalid negative values
    if bytes_value < 0 or packets_value < 0:
        raise ValueError("Bytes and packets cannot be negative.")

    # Prevent extremely large values
    if bytes_value > 100000000 or packets_value > 10000000:
        raise ValueError("Input values are too large.")

    # Prepare network traffic data
    data = pd.DataFrame(
        [[bytes_value, packets_value]],
        columns=["bytes", "packets"]
    )

    # Predict threat
    prediction = model.predict(data)

    if prediction[0] == 1:
        return "Threat Detected"
    else:
        return "Normal Activity"