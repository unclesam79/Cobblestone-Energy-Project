# Project Submission for Cobblestone Energy

*Submitted as part of a job application to Cobblestone Energy.*

---

## Project Description

### Project Title: Efficient Data Stream Anomaly Detection

**Objective:** Develop a Python script capable of detecting anomalies in a continuous data stream. This simulated stream represents real-time sequences of floating-point numbers, such as financial transactions or system metrics. The goal is to identify unusual patterns, such as exceptionally high values or deviations from the norm.

---

### Project Objectives

1. **Algorithm Selection**:  
   Identify and implement a suitable algorithm for anomaly detection that adapts to concept drift and seasonal variations.

2. **Data Stream Simulation**:  
   Design a function to emulate a data stream, incorporating regular patterns, seasonal elements, and random noise.

3. **Anomaly Detection**:  
   Develop a real-time mechanism to accurately flag anomalies as the data is streamed.

4. **Optimization**:  
   Ensure the algorithm is optimized for both speed and efficiency.

5. **Visualization**:  
   Create a straightforward real-time visualization tool to display both the data stream and any detected anomalies.

---

### Project Requirements

- **Implementation Language**: Python 3.x
- **Documentation**: Code should be thoroughly documented, with comments to explain key sections.
- **Algorithm Explanation**: Include a concise explanation of the chosen algorithm and its effectiveness.
- **Error Handling**: Ensure robust error handling and data validation.
- **External Libraries**: Limit the use of external libraries. If necessary, include a `requirements.txt` file.

---

## Explanation of my Algorithm

The anomaly detection algorithm I implemented is based on a **rolling mean and standard deviation** to monitor deviations in real-time data streams. Key features of the algorithm include:

- **Real-Time Adaptation**: By calculating the rolling mean and standard deviation over a fixed-size window of recent data points, the algorithm adjusts to local trends and seasonal patterns, effectively handling concept drift.
- **Anomaly Flagging**: Anomalies are flagged when a data point deviates beyond a set threshold (e.g., 2 standard deviations) from the rolling mean, which highlights outliers such as sudden spikes or drops.
- **Efficiency**: This threshold-based approach is computationally efficient and well-suited for streaming environments, as it quickly identifies outliers without extensive processing.
- **Dynamic Adjustment**: The rolling window allows the detection mechanism to adapt dynamically to shifting data distributions.

While straightforward, this method effectively flags anomalies in scenarios where they represent significant deviations from recent norms. 

---
