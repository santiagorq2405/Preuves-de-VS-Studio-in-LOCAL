import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def generate_normal_sample(mu, sigma, n):
    """
    Generate a sample of size n from a normal distribution.
    
    Parameters:
    mu (float): Mean of the normal distribution
    sigma (float): Standard deviation of the normal distribution
    n (int): Sample size
    
    Returns:
    numpy.ndarray: Sample from normal distribution
    """
    return np.random.normal(mu, sigma, n)

# Generate sample with specified parameters
mu = 0.0
sigma = 1.0
n = 100

sample = generate_normal_sample(mu, sigma, n)

# Create QQ plot
plt.figure(figsize=(8, 6))
stats.probplot(sample, dist="norm", plot=plt)
plt.title(f'QQ Plot - Normal Distribution\nμ={mu}, σ={sigma}, n={n}')
plt.grid(True, alpha=0.3)

# Save the plot
plt.savefig('qqplot.png', dpi=300, bbox_inches='tight')
plt.show()

print(f"Sample statistics:")
print(f"Mean: {np.mean(sample):.4f}")
print(f"Standard deviation: {np.std(sample, ddof=1):.4f}")
print(f"Sample size: {len(sample)}")
print("QQ plot saved as 'qqplot.png'")
