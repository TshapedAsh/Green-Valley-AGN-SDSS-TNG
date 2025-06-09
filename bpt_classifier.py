import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# --- Configuration & Scientific Constants ---

# URL for the SDSS CasJobs API
SDSS_API_URL = "https://skyserver.sdss.org/casjobs/RestAPI/contexts/dr8/query"

# SQL Query to get emission line fluxes for the BPT diagram
# We select galaxies from the MPA-JHU catalog (based on SDSS DR8)
# which provides robust emission line measurements.
# We apply a signal-to-noise (S/N) cut of > 3 on all relevant lines
# to ensure we are working with reliable data.
SDSS_QUERY = """
SELECT
    p.specobjid,
    p.h_alpha_flux, p.h_beta_flux,
    p.oiii_5007_flux, p.nii_6584_flux,
    p.h_alpha_flux_err, p.h_beta_flux_err,
    p.oiii_5007_flux_err, p.nii_6584_flux_err
FROM
    galSpecLine as p
WHERE
    p.h_alpha_flux > 3 * p.h_alpha_flux_err AND
    p.h_beta_flux > 3 * p.h_beta_flux_err AND
    p.oiii_5007_flux > 3 * p.oiii_5007_flux_err AND
    p.nii_6584_flux > 3 * p.nii_6584_flux_err
"""

# --- BPT Demarcation Line Functions ---

def kauffmann_2003(log_nii_ha):
    """
    The Kauffmann et al. (2003) demarcation line.
    Separates pure star-forming galaxies from composite galaxies.
    Galaxies below this line are considered star-forming.
    """
    return 0.61 / (log_nii_ha - 0.05) + 1.3

def kewley_2001(log_nii_ha):
    """
    The Kewley et al. (2001) 'maximum starburst' line.
    Separates composite galaxies from true AGN.
    Galaxies above this line are considered AGN.
    """
    return 0.61 / (log_nii_ha - 0.47) + 1.19

# --- Main Application Logic ---

def fetch_sdss_data(query, url):
    """
    Fetches data from the SDSS server using the provided SQL query.
    
    Args:
        query (str): The SQL query to execute.
        url (str): The API endpoint URL.
        
    Returns:
        pandas.DataFrame: A DataFrame containing the query results.
    """
    print("🛰️  Querying SDSS database... This may take a moment.")
    params = {'query': query, 'format': 'csv'}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        print("✅ Data received successfully.")
        # The first line of the response is the column headers, and the second is the data types.
        # We skip the second line (data types) to correctly read the CSV.
        csv_data = response.text.splitlines()
        csv_io = StringIO("\n".join([csv_data[0]] + csv_data[2:]))
        df = pd.read_csv(csv_io)
        return df
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data: {e}")
        return None

def process_and_classify(df):
    """
    Processes the raw data to calculate BPT ratios and classifies galaxies.
    
    Args:
        df (pandas.DataFrame): The DataFrame with raw flux data.
        
    Returns:
        pandas.DataFrame: The DataFrame with new columns for BPT ratios and classification.
    """
    print("🔬 Calculating line ratios and classifying galaxies...")
    
    # Calculate the BPT diagram axes
    # np.log10 is used for the logarithmic scale typical of BPT diagrams.
    df['log_nii_ha'] = np.log10(df['nii_6584_flux'] / df['h_alpha_flux'])
    df['log_oiii_hb'] = np.log10(df['oiii_5007_flux'] / df['h_beta_flux'])
    
    # Classify galaxies based on their position relative to the demarcation lines
    kauffmann_line = kauffmann_2003(df['log_nii_ha'])
    kewley_line = kewley_2001(df['log_nii_ha'])
    
    # Conditions for classification
    is_star_forming = (df['log_oiii_hb'] < kauffmann_line) & (df['log_nii_ha'] < 0.05)
    is_agn = (df['log_oiii_hb'] > kewley_line)
    # Composites are between the two lines
    is_composite = (~is_star_forming) & (~is_agn)
    
    # Apply classification labels
    df['classification'] = 'Ambiguous'
    df.loc[is_star_forming, 'classification'] = 'Star-Forming'
    df.loc[is_composite, 'classification'] = 'Composite'
    df.loc[is_agn, 'classification'] = 'AGN'
    
    print("📊 Classification complete:")
    print(df['classification'].value_counts())
    
    return df

def create_bpt_plot(df):
    """
    Creates and saves a publication-quality BPT diagram.
    
    Args:
        df (pandas.DataFrame): The classified galaxy data.
    """
    print("🎨 Generating BPT diagram...")
    
    # Set plot style for a more professional look
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Use seaborn's kdeplot for a 2D density map of all points
    sns.kdeplot(
        x=df['log_nii_ha'], 
        y=df['log_oiii_hb'], 
        ax=ax, 
        cmap='viridis',
        fill=True,
        thresh=0.02, # Don't plot lowest-density regions
        alpha=0.8
    )

    # Plot the demarcation lines
    x_line = np.linspace(-2.5, 0.3, 200)
    ax.plot(x_line, kauffmann_2003(x_line), color='black', linestyle='--', linewidth=2, label='Kauffmann et al. (2003)')
    
    x_line2 = np.linspace(-2.5, 0.35, 200)
    ax.plot(x_line2, kewley_2001(x_line2), color='red', linestyle='-', linewidth=2, label='Kewley et al. (2001)')

    # Annotate the plot to label the different regions
    ax.text(-0.8, -0.9, 'Star-Forming', fontsize=14, color='navy')
    ax.text(0.1, -0.3, 'Composite', fontsize=14, color='green')
    ax.text(0.0, 1.0, 'AGN', fontsize=14, color='darkred')
    
    # Set plot labels and limits
    ax.set_xlabel(r'$\log_{10}([\mathrm{N\ II}] / \mathrm{H\alpha})$', fontsize=16)
    ax.set_ylabel(r'$\log_{10}([\mathrm{O\ III}] / \mathrm{H\beta})$', fontsize=16)
    ax.set_title('BPT Diagram for SDSS DR8 Galaxies', fontsize=18, pad=20)
    
    ax.set_xlim(-2.0, 1.0)
    ax.set_ylim(-1.5, 1.5)
    
    ax.legend(fontsize=12)
    plt.tight_layout()
    
    # Save the figure
    output_filename = 'BPT_Diagram.png'
    plt.savefig(output_filename, dpi=300)
    print(f"✅ Plot saved as {output_filename}")
    plt.show()

# --- Main execution block ---
if __name__ == "__main__":
    raw_data = fetch_sdss_data(SDSS_QUERY, SDSS_API_URL)
    
    if raw_data is not None and not raw_data.empty:
        classified_data = process_and_classify(raw_data)
        create_bpt_plot(classified_data)
    else:
        print("❌ Could not generate plot due to data fetching errors.")
