import random
import math

import matplotlib.pyplot as plt

def stream(length):
    """Generator function to simulate a data stream
    while incorporating regular patterns, seasonal elements, and random noise."""
    season_remaining = 0  # how many more data points in the current season?
    multipliers = [-2, -1.5, -1, 1, 1.5, 2]
    random.shuffle(multipliers)  # to improve realism in the simulation
    seasonal_variation_constant = 10
    noise = random.random() * 10  # random noise for a given data point
    regular_pattern = random.choice((math.sin, math.cos))
    prev = 0  # data stream starts at 0
    j = 0  #

    for i in range(length):
        if season_remaining == 0:  # new season started
            if j == len(multipliers):  # all multipliers have been used
                # shuffle and start again
                random.shuffle(multipliers)
                j = 0
            season_remaining = int(length * 0.2)
            multiplier = multipliers[j]
            j += 1  # new season: new multiplier
            seasonal_modifier = seasonal_variation_constant * multiplier
        noise = random.random() * 30
        # each data point is simulated by multiplying the previous point with the chosen regular pattern (sin or cos),
        # and then adding on noise and a seasonal modifier
        data_point = (prev * regular_pattern(i) + noise) + seasonal_modifier
        prev = data_point
        season_remaining -= 1
        yield i, data_point

# Parameters for the stream and rolling statistics
stream_length = 1000
window_size = int(stream_length * 0.05)
threshold = 2  # Number of standard deviations from the mean

# Initialize lists for data and rolling stats
temp = []
rolling_mean = []
rolling_std = []
anomalies = []

# Helper functions for calculating mean and standard deviation
def calculate_mean(data):
    return sum(data) / len(data) if data else 0

def calculate_std(data, mean):
    variance = sum((x - mean) ** 2 for x in data) / len(data) if data else 0
    return math.sqrt(variance)

# Plotting setup
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=0.7, label="Data Stream")
anomaly_line, = ax.plot([], [], 'ro', markersize=3, label="Anomalies")  # red dots for anomalies
ax.legend()
xlim_lower = -int(0.02*(stream_length))
flag = False
# Add text for displaying rolling mean
mean_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, color='blue')

for i, data_point in stream(stream_length):
    temp.append(data_point)
    ax.set_xlim(xlim_lower, int(1.02*(i+1)))  # update upper xlim as the stream grows
    if not flag:  # no negative data point has been encountered yet
        ax.set_ylim(int(min(temp)*0.75), int(max(temp)*1.25))
        if min(temp) < 0:
            flag = True
    else:
        ax.set_ylim(int(min(temp)*1.25), int(max(temp)*1.25))

    # Calculate rolling mean and standard deviation
    if i >= window_size:
        window_data = temp[-window_size:]
        mean = calculate_mean(window_data)
        std_dev = calculate_std(window_data, mean)
        rolling_mean.append(mean)
        rolling_std.append(std_dev)
        # Update text labels with current rolling mean
        mean_text.set_text(f'Rolling Mean: {mean:.2f}')

        # Check for anomalies
        if abs(data_point - mean) > threshold * std_dev:
            anomalies.append((i, data_point))
    else:
        # Use the full list for the initial mean and std calculation
        mean = calculate_mean(temp)
        std_dev = calculate_std(temp, mean)
        rolling_mean.append(mean)
        rolling_std.append(std_dev)

    line.set_xdata(range(len(temp)))
    line.set_ydata(temp)

    # Plot anomalies
    if anomalies:
        anomaly_x, anomaly_y = zip(*anomalies)
        anomaly_line.set_xdata(anomaly_x)
        anomaly_line.set_ydata(anomaly_y)

    plt.draw()
    plt.pause(0.1)

plt.show()
