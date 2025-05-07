import statistics

data = [1, 2, 3, 4, 5, 5]
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
stdev = statistics.stdev(data)

print(f"Statistics - Mean: {mean}, Median: {median}, Mode: {mode}, Standard Deviation: {stdev}")



import numpy as np

array = np.array([1, 2, 3, 4, 5])
mean_np = np.mean(array)
std_np = np.std(array)
sum_np = np.sum(array)

print(f"Numpy - Mean: {mean_np}, Standard Deviation: {std_np}, Sum: {sum_np}")



import math

sqrt_val = math.sqrt(25)
power_val = math.pow(2, 3)
log_val = math.log(10)

print(f"Math - Square Root: {sqrt_val}, Power: {power_val}, Log: {log_val}")



from scipy import stats

data_sp = [1, 2, 3, 4, 5]
mean_sp = stats.tmean(data_sp)
median_sp = np.median(data_sp)
mode_sp = stats.mode(data_sp)
stdev_sp = stats.tstd(data_sp)

print(f"SciPy Stats - Mean: {mean_sp}, Median: {median_sp}, Mode: {mode_sp}, Standard Deviation: {stdev_sp}")
