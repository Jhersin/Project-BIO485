import numpy as np



def gen_mask(kspace, num_lines=0, num_central_lines=0):
    """
    Generate a horizontally oriented k-space mask with equally spaced sampling and additional central lines.
    Handles cases where either num_lines or num_central_lines is zero.

    Parameters:
    - kspace: numpy array, the input k-space data
    - num_lines: int, the number of k-space lines to sample outside the center
    - num_central_lines: int, the number of contiguous central k-space lines to include

    Returns:
    - mask: numpy array, the generated mask
    """
    # Get the number of rows in the k-space
    num_rows = kspace.shape[2]

    # Initialize the mask with all zeros
    mask = np.zeros(num_rows, dtype=bool)

    # Add central lines if num_central_lines > 0
    if num_central_lines > 0:
        center_start = (num_rows - num_central_lines) // 2
        center_end = center_start + num_central_lines
        mask[center_start:center_end] = True

    # Add equally spaced lines if num_lines > 0
    if num_lines > 0:
        spacing = num_rows // num_lines
        equally_spaced_indices = np.arange(0, num_rows, spacing)
        mask[equally_spaced_indices] = True

    # Avoid overwriting central region (if both are present)
    if num_central_lines > 0 and num_lines > 0:
        mask[center_start:center_end] = True

    # Expand the mask to match k-space dimensions
    mask = np.tile(mask[:, np.newaxis], (15, 1, kspace.shape[1]))
    mask_rot = mask.transpose(0, 2, 1)
    return mask_rot