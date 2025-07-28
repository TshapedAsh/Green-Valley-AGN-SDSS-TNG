# 🌌 Quenching in the Green Valley: SDSS vs. IllustrisTNG & EAGLE

**A reproducible, open-science benchmark for AGN host galaxy quenching in cosmological simulations and SDSS observations.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 🚀 Project Overview

**Can state-of-the-art simulations actually match the real universe when it comes to AGN host galaxies in the "green valley"?**  
This repo hosts all code, processed data, and figures for the paper:

> **"Quenching in the Green Valley at Low Redshift: A Comparative Analysis of AGN Host Galaxies in SDSS, IllustrisTNG and EAGLE"**  
> Gaurav Gawade (MNRAS, 2025)

We pit 21,649 real AGN hosts from SDSS DR7 against simulated analogues in IllustrisTNG-100 and EAGLE.  
Spoiler: **the simulations don't agree with the universe, and it's not even close.** Want details? Dive into the manuscript!

---

## 🏆 Why Should You Care?

- **Massive sSFR mismatch:** IllustrisTNG "green-valley" galaxies are over-quenched by up to 5.3 dex (!), while EAGLE galaxies are under-quenched by ~1.1 dex.
- **Simulation overproduction:** TNG overpopulates the green valley by almost an order of magnitude.
- **No cherry-picking:** Everything—selection, statistics, figures—is fully reproducible.
- **All data and code are open.** If you want to test, tweak, or expand, this is your launchpad.

Read the full story and the caveats (we're honest!) in [`paper/paper_draft.pdf`](paper/paper_draft.pdf).

---

## 🗂 Repository Structure

Green-Valley-AGN-SDSS-TNG/
├── master_notebook.ipynb # Main Jupyter notebook: data, analysis, plots
├── environment.yml # Conda environment for full reproducibility
├── requirements.txt # Python package list (pip)
├── data/ # (User-downloaded) input catalogs from SDSS/TNG/EAGLE
├── outputs/
│ └── figures/ # All generated plots (PDF/PNG)
├── paper/
│ └── paper_draft.pdf # Full manuscript (read this!)
└── docs/ # (Optional) supplementary documentation


---

## 📊 Figures (from `outputs/figures/`)

> *Convert all .pdf figures to .png for embedding here—GitHub won't display PDFs inline!*

- `fig1_colour_mass.png` – Colour–mass plane & sSFR KDE  
  ![Colour–Mass Plane](outputs/figures/fig1_colour_mass.png)
- `fig2_ssfr_mass_2panel.png` – sSFR–mass relation
- `fig3_cdf.png` – Cumulative distributions: stellar mass & sSFR
- `fig4_gv_frac.png` – Green valley occupancy fraction  
  ![GV Occupancy](outputs/figures/fig4_gv_frac.png)
- `fig5_percentile_sweep.png` – Sensitivity of sSFR gap to colour cut
- `fig6_bootstrap_KS.png` – Bootstrap KS distributions
- `fig7_BPT_mock.png` – Mock BPT diagram for simulated analogues  
  ![Mock BPT](outputs/figures/fig7_BPT_mock.png)
- `figure_A1_BPT_Diagram_SDSS.png` – Appendix: SDSS BPT
- `figure_A2_TNG_EAGLE_GV_Definition.png` – Appendix: Green valley in TNG/EAGLE
- `figure_A3_mass_comparison.png` – Appendix: Stellar mass KDEs
- `figure_A4_ssfr_comparison.png` – Appendix: sSFR KDEs

---

## 💻 How to Run This Project

1. **Clone the repo and set up the environment:**
    ```
    git clone https://github.com/TshapedAsh/Green-Valley-AGN-SDSS-TNG.git
    cd Green-Valley-AGN-SDSS-TNG
    conda env create -f environment.yml
    conda activate green-valley-env
    ```
    or use pip:
    ```
    pip install -r requirements.txt
    ```

2. **Download required data:**
    - SDSS DR7: [MPA-JHU Value-Added Catalogues](https://wwwmpa.mpa-garching.mpg.de/SDSS/DR7/Data/)
    - IllustrisTNG100-1: [TNG Project](https://www.tng-project.org/data/downloads/TNG100-1/)
    - EAGLE Ref-L0100N1504: [EAGLE SQL interface](http://virgodb.dur.ac.uk:8080/Eagle/)

    Place downloaded files in the `data/` directory (file names are documented in the notebook).

3. **Run the notebook:**
    ```
    jupyter notebook master_notebook.ipynb
    ```
    - All figures and stats will be regenerated and saved to `outputs/figures/`.
    - Every analysis step is documented inline with the code.

---

## 📚 More Information

- **All main results, methodology, and caveats are explained in detail in [`paper/paper_draft.pdf`](paper/paper_draft.pdf).**
- For full transparency, see appendix and all code logic in the notebook.

---

## 📜 Citation

If you use this code, data, or findings, please cite:

@article{Gawade2025,
author = {Gaurav Gawade},
title = {Quenching in the Green Valley at Low Redshift: A Comparative Analysis of AGN Host Galaxies in SDSS, IllustrisTNG and EAGLE},
journal = {xyz},
year = {2025},
volume = {xxx},
pages = {yyy--zzz},
doi = {xxx} 
}


And our open data/software release:
Gawade, Gaurav. (2025). Green-Valley-AGN-SDSS-TNG [Data set]. Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX



(Replace Zenodo DOI after upload.)

---

## 📬 Contact

**Gaurav Gawade**  
[gauravgawade@proton.me](mailto:gauravgawade@proton.me)

---

## ⚖️ License

MIT License – Open for reuse, remix, and cosmic criticism.

---

## 🚦 Open Science Statement

All data, code, and outputs are public, reproducible, and transparent.  
We welcome honest criticism, new ideas, and community forks—help us make galaxy evolution science better!

**Read the full manuscript for the real scientific discussion, all caveats, and next steps—this README is just the "movie trailer" for your curiosity!**
