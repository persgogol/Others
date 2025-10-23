"""
Simple Moving Average (SMA) and Exponential Moving Average (EMA) calculator.

This script defines functions to compute SMA and EMA given a list of numerical data.
It can be used as a helper tool for analyzing time series such as cryptocurrency prices.
"""


def calculate_sma(data, window):
    """Calculate the Simple Moving Average (SMA) for the given data and window size.

    Args:
        data (list of float): The input time series data.
        window (int): The number of periods to average over.

    Returns:
        list of float: SMA values.

    Raises:
        ValueError: If window is not positive or data length is less than window.
    """
    if window <= 0:
        raise ValueError("Window size must be positive")
    if len(data) < window:
        raise ValueError("Data length must be at least equal to the window size")
    sma = []
    for i in range(window - 1, len(data)):
        window_slice = data[i - window + 1:i + 1]
        sma.append(sum(window_slice) / window)
    return sma


def calculate_ema(data, window):
    """Calculate the Exponential Moving Average (EMA) for the given data and window size.

    Args:
        data (list of float): The input time series data.
        window (int): The smoothing window.

    Returns:
        list of float: EMA values.

    Raises:
        ValueError: If window is not positive or data is empty.
    """
    if window <= 0:
        raise ValueError("Window size must be positive")
    if not data:
        raise ValueError("Data must not be empty")
    ema = []
    multiplier = 2 / (window + 1)
    # Start EMA with the SMA of the first window
    ema_current = sum(data[:window]) / window
    ema.append(ema_current)
    for price in data[window:]:
        ema_current = (price - ema_current) * multiplier + ema_current
        ema.append(ema_current)
    return ema


if __name__ == "__main__":
    # Example usage
    sample_prices = [100, 102, 101, 105, 110, 108, 112, 115, 117, 120]
    window_size = 3
    print(f"Sample prices: {sample_prices}")
    sma_values = calculate_sma(sample_prices, window_size)
    print(f"{window_size}-period SMA: {sma_values}")
    ema_values = calculate_ema(sample_prices, window_size)
    print(f"{window_size}-period EMA: {ema_values}")
