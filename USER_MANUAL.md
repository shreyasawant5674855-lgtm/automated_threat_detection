# User Manual
## Automated Threat Detection System

### 1. Introduction

The Automated Threat Detection System is a machine-learning-based system that analyzes network traffic using bytes and packets and classifies the activity as Normal Activity or Threat Detected.

### 2. System Requirements

- Web browser
- Internet connection for the deployed application
- Access to the Automated Threat Detection dashboard

### 3. How to Use the System

1. Open the Threat Monitoring Dashboard.
2. Enter the number of bytes in the Bytes field.
3. Enter the number of packets in the Packets field.
4. Click the "Check Traffic" button.
5. The system sends the input to the backend API.
6. The Random Forest model analyzes the input.
7. The result is displayed on the dashboard.

### 4. Understanding the Result

The system displays one of the following results:

- Normal Activity
- Threat Detected

### 5. Input Validation

The system checks that:

- Both Bytes and Packets are entered.
- The values are numeric.
- Negative values are not accepted.

If required information is missing, the dashboard displays an appropriate validation message.

### 6. Troubleshooting

If the system does not return a result:

- Check that both input fields contain valid values.
- Check your internet connection.
- Check whether the backend/deployed API is available.

### 7. Conclusion

The user manual provides the basic steps required to use the Automated Threat Detection System and understand its detection results.