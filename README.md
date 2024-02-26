# Comparative Performance and Reliability Between Two Distinct Measurements for a Same Parameter

## Analysis of Distinct Halo Mass Measurements: Bias and Dispersion

This repository contains a Python script designed to perform a analysis of the bias and dispersion in halo mass measurements obtained via two distinct estimation methods: the Gapper and Yang methods. The analysis aims to understand how these biases and dispersions vary across different halo mass ranges, offering insights into the comparative performance and reliability of these two methods.

### Getting Started

#### Prerequisites

Before running the script, ensure you have the following prerequisites installed:

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn

These can be installed using pip (Python's package installer) if you don't already have them. Run the following command to install all required packages:

```bash
pip install pandas numpy matplotlib seaborn
```

### Input Data Format

The script expects an input file described as follows:
- The file should be a whitespace-delimited text file without headers. (But if you have a file delimited by commas or any other delimiter, you can adjust the `pd.read_csv` method in the script to read your file appropriately by using the `sep` parameter.)
- My file contain eight columns in the following order:
  1. **ID**: A unique identifier for each halo.
  2. **RA**: Right Ascension of the halo.
  3. **DEC**: Declination of the halo.
  4. **ZSPEC**: Spectroscopic redshift of the halo.
  5. **M200Y**: Halo mass estimate using the Yang method.
  6. **M200**: Halo mass estimate using the Gapper method.
  7. **NMEMBER**: Number of members in the halo.
  8. **R200**: Radius within which the mean density is 200 times the critical density.
- **Note**: In Python, column indices start at 0. This means when referencing columns programmatically, you will use indices 0 through 7 for the columns listed above.

### Running the Script

To run the script, follow these steps:

1. **Prepare your dataset** according to the guidelines provided in the [Input Data Format](#input-data-format). Ensure your dataset is saved as a text file, for example, `final_catalog_of_clusters.txt`.
2. **Download the script** from this repository. Ensure Python is installed on your system.
3. **Open your terminal or command prompt**. Navigate to the directory where the script is located.
4. **Execute the script** by running the following command in your terminal or command prompt, making sure to replace `path_to_script.py` with the actual path to the script file and `path_to_your_dataset/final_catalog_of_clusters.txt` with the path to your dataset file:

   ```bash
   python path_to_script.py path_to_your_dataset/final_catalog_of_clusters.txt
   ```

### What the Script Does

1. Data Preparation: Calculates the logarithm of halo masses for better analysis and visualization and computes the difference (SHIFT_G_HALO_MASS) between the log of halo masses estimated by the Gapper and Yang methods.
2. Statistical Analysis: The dataset is divided into specified halo mass bins. For each bin, the script calculates the standard deviation, mean value, and error to quantify the bias and dispersion.
3. Visualization: Generates a Kernel Density Estimation (KDE) plot to visualize the distribution of halo masses estimated by both methods.
4. Output: Saves the statistical measures for each mass bin to a text file named disp_bias_halo_mass.txt.

### Output Format

The output text file disp_bias_halo_mass.txt will contain the following information for each halo mass bin:

- Bin label
- Combined error measure that takes into account both the dispersion (or standard deviation) and the bias (or mean) of the dataset (this combined metric can be useful for assessing the reliability of results in a statistical analysis, as it takes into account both the data's dispersion and any systematic tendency (bias) that may be present).

### Visualization

The generated plot (Plot_gapper_yang_halomass.pdf) visualizes the bias and dispersion of halo mass estimates. It shows the distribution of the differences in halo mass estimates across the range of halo masses, highlighting the performance of the Gapper and Yang methods.

