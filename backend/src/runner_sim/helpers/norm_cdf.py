import math

# Derived from scipy.stats.norm.cdf
def norm_cdf(x, mean=0, std_dev=1):
    """
    Compute the cumulative distribution function for a normal distribution.

    Parameters:
    x (float): The value to evaluate the CDF at.
    mean (float): The mean of the normal distribution (default 0).
    std_dev (float): The standard deviation of the normal distribution (default 1).

    Returns:
    float: The CDF value for the normal distribution.
    """
    # Standardize x
    z = (x - mean) / std_dev
    # Use the error function to calculate the CDF
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))