import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


def load_data(filepath):
    df = pd.read_csv(filepath, delim_whitespace=True, header=None, names=['ID', 'RA', 'DEC', 'ZSPEC', 'M200Y', 'M200', 'NMEMBER', 'R200'])
    # difference between masses
    df['SHIFT_G_HALO_MASS'] = df['M200'] - df['M200Y']
    return df

# Function to estimate the dispersion and bias
def calc_disp_bias(group):
    disp = np.std(group['SHIFT_G_HALO_MASS'])
    bias = np.mean(group['SHIFT_G_HALO_MASS'])
    err = np.sqrt(disp ** 2 + bias ** 2)
    return disp, bias, err

# Main
def main():
    df = load_data('final_catalog_of_clusters')

    # Defining the stacks limits
    bins = [11.6, 12.0, 12.25, 12.5, 13.0, 13.5, 14.0, 14.3, 15.3]
    labels = ['11.6_12.0', '12.0_12.25', '12.25_12.5', '12.5_13.0', '13.0_13.5', '13.5_14.0', '14.0_14.3', '14.3_15.3']
    df['BIN'] = pd.cut(df['M200Y'], bins=bins, labels=labels, include_lowest=True)


    with open('disp_bias_halo_mass.txt', 'w+') as arq:
        Bias = []
        Desvio = []
        x = []

        for label in labels:
            group = df[df['BIN'] == label]
            disp, bias, err = calc_disp_bias(group)
            Desvio.append(disp)
            Bias.append(bias)
            x.append(np.mean(group['M200Y']))
            arq.write(f'{label} {err}\n')

        # Plot
        plt.figure(figsize=(10, 7))
        cm = sns.color_palette("viridis", as_cmap=True)
        a = sns.kdeplot(x='M200Y', y='SHIFT_G_HALO_MASS', data=df, cmap=cm, shade=True, shade_lowest=False, levels=20, bw_method=0.17)
        # sns.scatterplot(x='M200Y', y='SHIFT_G_HALO_MASS', data=df, s=3, color="mediumblue")
        plt.errorbar(x, Bias, yerr=Desvio, xerr=None, capsize=1, capthick=1, ls="-", lw=0.81, c='red', elinewidth=0.8,
                     label=r'Std per $\Delta\,\log\,M_{\rm halo}$')
        plt.axhline(y=0, color="black", linestyle="-", lw=0.4)
        plt.scatter(x, Bias, s=35, c='red', label=r'Bias per $\Delta\,\log\,M_{\rm halo}$')
        plt.legend(fontsize=10)
        plt.xlabel(r'$\log\, M_h$ (Yang)')
        plt.ylabel(r'$\log$ [$M_h$ (Gapper) / $M_h$ (Yang)] dex')
        plt.xlim(11.4, 15.4)
        plt.tight_layout()
        plt.savefig('Plot_gapper_yang_halomass.pdf', dpi=200)
        plt.show()
        plt.close()

if __name__ == "__main__":
    main()
