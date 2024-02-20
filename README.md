## Analysis of Distinct Halo Mass Measurements -  Bias and Dispersion

This script performs an analysis to quantify the bias and dispersion in halo mass measurements using two different estimation methods: the Gapper and Yang methods. The analysis is conducted across different halo mass ranges to understand how the bias and dispersion vary with halo mass.

### Overview

The script reads in a dataset containing halo mass estimates obtained from both the Gapper and Yang methods. It then proceeds to:

1. **Data Preparation**: Prepares the data by calculating the logarithm of the halo masses for better analysis and visualization. It also computes the difference (`shift_g_halo_mass`) between the log of halo masses estimated by the Gapper and Yang methods to analyze the bias.

2. **Statistical Analysis**: Divides the data into specified halo mass bins. For each bin, it calculates statistical measures to understand the bias and dispersion:
   - **Standard Deviation (`std`)**: Measures the spread or variation of the `shift_g_halo_mass` values within each mass bin.
   - **Mean (`mean`)**: Represents the average bias in `shift_g_halo_mass` for each mass bin, indicating whether one method tends to estimate higher or lower masses compared to the other.
   - **Error (`err`)**: Calculated as the square root of the sum of squares of the standard deviation and the mean for each mass bin, providing a measure of the total uncertainty associated with the bias and dispersion for each mass range.

3. **Visualization**: Generates a Kernel Density Estimation (KDE) plot to visualize the distribution of halo masses estimated by both methods, highlighting differences in their estimation across the range of halo masses.

4. **Output**: Saves the statistical measures (standard deviation, mean, and error) for each mass bin to a text file named `disp_bias_halo_mass.txt`. This file documents how the bias and dispersion vary across different halo mass ranges, providing insights into the performance and reliability of the Gapper and Yang methods for halo mass estimation.

