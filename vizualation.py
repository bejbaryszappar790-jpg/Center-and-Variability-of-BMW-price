import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load dataset
df = pd.read_csv('bmw.csv')

# Calculate central metrics for plotting
mean_val = df['price'].mean()
median_val = df['price'].median()

# Initialize Figure
plt.figure(figsize=(14, 6))

# Plot 1: Histogram & KDE
plt.subplot(1, 2, 1)
sns.histplot(data=df, x='price', kde=True, bins=50, color='skyblue')
plt.axvline(mean_val, color='red', linestyle='--', label=f'Mean: {mean_val:.2f}')
plt.axvline(median_val, color='green', linestyle='-', label=f'Median: {median_val:.2f}')
plt.title('Distribution & Central Tendency (BMW Price)')
plt.xlabel('Price (£)')
plt.ylabel('Count')
plt.legend()

# Plot 2: Boxplot for IQR and Outliers
plt.subplot(1, 2, 2)
sns.boxplot(data=df, x='price', color='gray')
plt.title('Boxplot: IQR and Outliers')
plt.xlabel('Price (£)')

# Save and Show
plt.tight_layout()
plt.savefig('bmw_price_analysis.png', dpi=300)
plt.show()