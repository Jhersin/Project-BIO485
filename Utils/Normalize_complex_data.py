import numpy as np

def normalize_complex_data(data):
    """
    Center and normalize a complex-valued array.

    Parameters:
        data: np.ndarray (complex), shape (15, 320, 640)

    Returns:
        Centered and normalized data.
    """
    # Center the data
    real_mean = np.mean(data.real)
    imag_mean = np.mean(data.imag)
    centered_data = (data.real - real_mean) + 1j * (data.imag - imag_mean)

    # Normalize the magnitude
    magnitude = np.abs(centered_data)
    max_magnitude = np.max(magnitude)
    if max_magnitude == 0:
        return centered_data

    normalized_data = centered_data / max_magnitude
    return normalized_data