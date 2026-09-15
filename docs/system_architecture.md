# System Architecture Design

## Overview

The Automated Threat Detection System uses an AI-based Random Forest model to analyze network traffic and identify potential threats.

## System Architecture

The system follows this flow:

**Network Traffic → Data Preprocessing → AI Model → Threat Detection → Alert/Notification**

### Main Components

1. **Network Traffic Data**

   * Collects network traffic information such as bytes and packets.

2. **Data Preprocessing**

   * Prepares and processes the collected network data for the AI model.

3. **AI Model**

   * Uses a Random Forest Classifier to classify network activity as Normal or Attack.

4. **Threat Detection System**

   * Processes incoming traffic and predicts whether it is a threat.

5. **Alert System**

   * Generates an alert when suspicious network activity is detected.

6. **Feedback Loop**

   * Adds new threat data and helps update the model for future detection.

## System Flow

```text
Network Traffic
       ↓
Data Collection
       ↓
Data Preprocessing
       ↓
Random Forest Model
       ↓
Threat Detection
       ↓
Normal or Threat
       ↓
Alert / Continue Monitoring
       ↓
Feedback Loop
       ↓
Model Improvement
```
