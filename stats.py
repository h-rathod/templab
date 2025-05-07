import statistics

def calculate_stats(data):
    mean = statistics.mean(data)
    median = statistics.median(data)
    mode = statistics.mode(data)
    data_range = max(data) - min(data)
    variance = statistics.variance(data)
    std_dev = statistics.stdev(data)
    
    return {
        'mean': mean,
        'median': median,
        'mode': mode,
        'range': data_range,
        'variance': variance,
        'standard_deviation': std_dev
    }

# Example usage
sample_data = [1, 2, 2, 3, 4, 5, 5, 5, 6]
stats = calculate_stats(sample_data)
print(stats)
