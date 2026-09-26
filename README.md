# Bounded Fermi–Dirac Integral: Computational Supplement

Computational materials for Paul Zheng's research article on bounded Fermi–Dirac integrals. This repository contains Python source code, a Jupyter notebook, numerical output tables, and figure files. The article remains the source for mathematical definitions, hypotheses, proofs, and interpretation of the results.

## Repository contents

| Path | Contents |
| --- | --- |
| `bounded_fermi_corrected.py` | Main Python source file for the computational supplement. |
| `bounded_fermi_corrected.ipynb` | Jupyter notebook associated with the computations. |
| `manuscript_figures.py` | Python source file for manuscript figures. |
| `requirements.txt` | Python dependencies listed for this supplement. |
| `data/` | CSV outputs and `manifest.json`. |
| `figures/` | Figure files supplied as PDF, PNG, and SVG. |
| `standalone_execution.log` | Saved execution log. |

File names identify the supplied materials; consult the source files for the exact computations, command-line options, and generated outputs. The `data/` and `figures/` directories contain existing results, so readers can inspect them without first rerunning the notebook.

## Setup

Clone the repository and enter its root directory:

```powershell
git clone https://github.com/pzheng3/BoundedFermiDiracIntegral.git
cd BoundedFermiDiracIntegral
```

On Windows PowerShell, create a virtual environment and install the listed dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

If you use a different operating system, create and activate a Python virtual environment with your system's Python interpreter, then install `requirements.txt`. The exact Python and package versions used for the supplied outputs should be recorded separately if strict reproduction is required.

## Running the materials

Open `bounded_fermi_corrected.ipynb` with a Jupyter-compatible application to inspect or rerun its cells. Run cells from top to bottom using an environment with the required dependencies installed. The repository also provides `bounded_fermi_corrected.py` and `manuscript_figures.py` as standalone source files. Before executing them, inspect their main blocks and output paths: this README does not assume that running a file without arguments will regenerate every supplied result or that it is safe to overwrite existing outputs.

The saved `standalone_execution.log` and `data/manifest.json` may help identify how the included outputs were produced. Exact figure-to-command mappings and validated reproduction times have not yet been specified here.

## Selected results

| Topic | Included files |
| --- | --- |
| Forward evaluation | `data/forward_grid.csv`; `figures/1_Forward_Selvaggi_Fits.pdf`; `figures/2_Forward_Poisson_Fits.pdf` |
| Inverse evaluation | `data/inverse_grid.csv`; `figures/5_Inverse_Selvaggi_Fits.pdf`; `figures/8_Inverse_Poisson_Error.pdf` |
| Poisson endpoint checks | `data/poisson_endpoint_comparison.csv`; `data/poisson_endpoint_grid.csv`; `data/poisson_precision_audit.csv` |
| Generalized orders | `data/hurwitz_orders.csv`; `data/hurwitz_inverse_orders.csv`; `figures/17_Hurwitz_Generalized_Orders.pdf` |

These examples describe the existing file collection; they do not assert that every illustrated figure appears in the final article. The `figures/` directory contains additional versions and diagnostic plots, including PNG and SVG counterparts.

## Reproducibility and citation

For a publication, cite a fixed software release rather than relying only on the evolving default branch. Once the paper-associated version has been tested, create a GitHub release, archive it, and add its version-specific DOI and the final article citation here.

Article citation: To be added after publication or preprint posting.

Archived software release and DOI: To be added after release.

License: Check the repository for a `LICENSE` file. No license is asserted by this README.
