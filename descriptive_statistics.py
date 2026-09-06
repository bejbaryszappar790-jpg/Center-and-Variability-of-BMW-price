import numpy as np
import pandas as pd

# 1. Load the Dataset
df = pd.read_csv('bmw.csv')
price_data = df['price']

# 2. Sample Size (N)
n = len(price_data)

# 3. Mean Calculation
# Formula: sum(x) / N
mean_price = sum(price_data) / n

# 4. Median Calculation
# Formula: Middle value of sorted data
sorted_price = sorted(price_data)
if n % 2 == 0:
    median_price = (sorted_price[n//2 - 1] + sorted_price[n//2]) / 2
else:
    median_price = sorted_price[n//2]

# 5. Variance Calculation
# Formula: sum((x - mean)^2) / (N - 1)
squared_diff_sum = sum((x - mean_price) ** 2 for x in price_data)
variance_price = squared_diff_sum / (n - 1)

# 6. Standard Deviation Calculation
# Formula: square root of variance
std_price = variance_price ** 0.5

# 7. Range Calculation
# Formula: Max - Min
range_price = max(price_data) - min(price_data)

# 8. Interquartile Range (IQR) Calculation
# Formula: Q3 - Q1
q1 = np.percentile(price_data, 25)
q3 = np.percentile(price_data, 75)
iqr_price = q3 - q1

# Output the Results
print(f"Sample Size (N): {n}")
print(f"Mean: £{mean_price:.2f}")
print(f"Median: £{median_price:.2f}")
print(f"Variance: {variance_price:.2f}")
print(f"Standard Deviation: £{std_price:.2f}")
print(f"Range: £{range_price:.2f}")
print(f"IQR: £{iqr_price:.2f}")