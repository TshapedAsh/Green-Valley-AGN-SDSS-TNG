# Green Valley: AGN, SDSS, TNG

This repository contains the code and materials for the paper "Where Are the Green-Valley AGN in Illustris-TNG? A Host-Galaxy Demographics Test with SDSS" (submitted to MNRAS).

## Overview
This project compares AGN host galaxies from SDSS observations and IllustrisTNG simulations, focusing on green-valley demographics, star-formation rates, and emission-line diagnostics. The main analysis is in the Jupyter notebook `master_Copy.ipynb`.

Key findings:
- A ~3 dex discrepancy in SFR between SDSS AGN and TNG green-valley hosts.
- TNG overproduces quenched green-valley galaxies without optical AGN signatures.

## Repository Structure
- `master_Copy.ipynb`: Main Jupyter notebook with data loading, processing, analysis, and figures.
- `data/`: Input catalogs (FITS/HDF5 files from SDSS/IllustrisTNG). **Note**: Large files are .gitignored; download from [SDSS DR7](https://www.sdss.org/dr7/) and [IllustrisTNG](https://www.tng-project.org/data/) public archives.
- `outputs/figures/`: Generated plots (run the notebook to populate).
- `paper/`: Paper draft PDF.
- `docs/`: Supplementary files (e.g., OCRed notebook output with figures).
- `requirements.txt`: Python dependencies.

## How to Run
1. Clone the repo: `git clone https://github.com/YOUR_USERNAME/AGN_Classifier_with_BPT-Diagrams.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Download required data files into `./data/` (e.g., `gal_info_dr7_v5_2.fit`, `aperture_masses.hdf5` from sources above).
4. Run the notebook: `jupyter notebook master_Copy.ipynb`

## Dependencies
- Python 3.11+
- See `requirements.txt` for pinned versions.

## Citation
If using this code, cite the paper (DOI forthcoming). For questions, contact [your email].

## License
MIT License (or specify your choice).


## Note: > 🔒 Note: This repository accompanies a paper currently under review at MNRAS. The DOI will be updated upon acceptance.
