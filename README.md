# Cobblestone-Energy-Project
Project submitted as part of job application to Cobblestone Energy

Below is the project description I received:
Project Title:
Efficient Data Stream Anomaly Detection

Project Description:
Your task is to develop a Python script capable of detecting anomalies in a continuous data stream. This stream, simulating real-time sequences of floating-point numbers, could represent various metrics such as financial transactions or system metrics. Your focus will be on identifying unusual patterns, such as exceptionally high values or deviations from the norm.

Objectives:

Algorithm Selection: Identify and implement a suitable algorithm for anomaly detection, capable of adapting to concept drift and seasonal variations.
Data Stream Simulation: Design a function to emulate a data stream, incorporating regular patterns, seasonal elements, and random noise.
Anomaly Detection: Develop a real-time mechanism to accurately flag anomalies as the data is streamed.
Optimization: Ensure the algorithm is optimized for both speed and efficiency.
Visualization: Create a straightforward real-time visualization tool to display both the data stream and any detected anomalies.
Requirements:

The project must be implemented using Python 3.x.
Your code should be thoroughly documented, with comments to explain key sections.
Include a concise explanation of your chosen algorithm and its effectiveness.
Ensure robust error handling and data validation.
Limit the use of external libraries. If necessary, include a requirements.txt file.

Below is a brief explanation of the anomaly detection algorithm I implemented:
The anomaly detection algorithm uses a rolling mean and standard deviation to monitor deviations in real-time data streams. By calculating these metrics over a fixed-size window of recent data points, the algorithm adapts to local trends and seasonal patterns, effectively handling concept drift. Anomalies are flagged when a data point deviates beyond a set threshold (e.g., 2 standard deviations) from the rolling mean, highlighting outliers such as sudden spikes or drops.

This threshold-based approach is computationally efficient and well-suited for streaming environments, as it quickly identifies outliers without extensive processing. The reliance on a rolling window allows the detection mechanism to adjust dynamically, making it effective for data with shifting distributions.

While straightforward, this approach effectively flags anomalies in scenarios where they represent large deviations from recent norms.
