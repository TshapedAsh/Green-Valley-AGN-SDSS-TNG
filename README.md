AGN Classifier with BPT Diagrams
A Python project to query, analyze, and classify galaxies from the Sloan Digital Sky Survey (SDSS) to determine their primary ionization source. This tool identifies galaxies as either star-forming or as hosting an Active Galactic Nucleus (AGN) based on their emission-line ratios, plotting them on a Baldwin, Phillips & Terlevich (BPT) diagram.

This is a placeholder image. The bpt_classifier.py script will generate the actual plot.

🔬 Scientific Context
Galaxies can be broadly categorized by the primary source of their ionizing radiation. In most galaxies, this is the intense ultraviolet light from massive, young, hot stars (H II regions). However, some galaxies host a supermassive black hole at their center that is actively accreting matter. This process creates an Active Galactic Nucleus (AGN), an incredibly luminous region that can outshine the entire host galaxy.

The BPT diagram is a powerful diagnostic tool that uses the ratios of prominent optical emission lines to distinguish between these two mechanisms. The most common BPT diagram plots:

Y-axis: log 
10
​
 ([O III]λ5007/Hβ)

X-axis: log 
10
​
 ([N II]λ6584/Hα)

The position of a galaxy on this diagram reveals the hardness of its ionizing radiation spectrum.

Star-forming galaxies cluster in a tight sequence on the lower-left.

AGN have harder ionization spectra and occupy the upper-right region.

Composite galaxies, which have contributions from both star formation and an AGN, lie in between.

This project uses two key demarcation lines to separate these classes:

Kauffmann et al. (2003): An empirical line that separates pure star-forming galaxies from composite systems.

Kewley et al. (2001): A theoretical "maximum starburst" line that separates composite galaxies from "pure" AGN.

🛠️ How It Works
Query SDSS: The script sends an SQL query to the SDSS CasJobs server to retrieve emission line flux data for a sample of ~50,000 galaxies from Data Release 8 (DR8).

Process Data: It uses pandas to manage the data. It calculates the required line ratios and their logarithms.

Classify Galaxies: It applies the Kauffmann and Kewley demarcation lines to classify each galaxy into one of four categories: Star-forming, Composite, AGN, or Ambiguous/Other.

Visualize: It uses matplotlib and seaborn to generate a high-quality 2D density plot (a kernel density estimate) of the galaxy distribution on the BPT diagram, with the demarcation lines clearly drawn.

🚀 How to Run
Clone the repository:

git clone <your-repo-url>
cd <your-repo-directory>

Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the dependencies:

pip install -r requirements.txt

Run the script:

python bpt_classifier.py

The script will print its progress to the console and save the final plot as BPT_Diagram.png.

🔮 Future Work
This project provides a solid foundation. Here are some ideas to expand it:

Incorporate other BPT diagrams: Implement the diagrams using [S II] and [O I] to create a more robust classification scheme.

Machine Learning: Train a classifier (e.g., a Support Vector Machine or a simple Neural Network) on the BPT data to automate the classification.

Redshift Evolution: Modify the query to select galaxies in different redshift bins and see how the BPT diagram changes over cosmic time.

Host Galaxy Properties: Correlate the BPT classification with other galaxy properties available from SDSS, such as stellar mass, color, or morphology.
