# Bounded Fermi–Dirac Integral: Computational Supplement

This repository contains the Python source code and Jupyter notebooks supporting the numerical experiments, validation calculations, and figures in the accompanying research article on bounded Fermi–Dirac integrals.

## Contents

| Path | Description |
|---|---|
| `src/` | Core Python implementations of the bounded Fermi–Dirac integral and related formulas |
| `scripts/` | Scripts used to reproduce numerical experiments and manuscript figures |
| `notebooks/` | Jupyter notebooks for interactive exploration and validation |
| `figures/` | Reproduced figures and figure-generation outputs, if included |
| `requirements.txt` | Python package dependencies |

## Requirements

Tested with:

- Python `[VERSION]`
- NumPy `[VERSION]`
- SciPy `[VERSION]`
- Matplotlib `[VERSION]`
- mpmath `[VERSION]`
- JupyterLab or Jupyter Notebook, if running the notebooks

## Installation

Clone the repository:

```bash
git clone [https://github.com/pzheng3/BoundedFermiDiracIntegral.git](https://github.com/pzheng3/BoundedFermiDiracIntegral.git)
cd BoundedFermiDiracIntegral
```

Create and activate a virtual environment.

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Reproducing the computations

Run the scripts from the repository root.

```bash
python scripts/[SCRIPT_NAME].py
```

For example, replace `[SCRIPT_NAME].py` with the actual program that produces the forward evaluation, inverse calculation, or Poisson-trace comparison reported in the article.

To open the notebooks:

```bash
jupyter notebook
```

Then open the relevant file in `notebooks/`.

## Reproducibility notes

- The scripts use the numerical parameters, tolerances, and truncation rules stated in the accompanying article.
- If a computation uses arbitrary-precision arithmetic, set the precision as documented in the corresponding script or notebook.
- Reproduction time depends on the selected parameter ranges and numerical precision.
- The repository version associated with the submitted article will be preserved as a tagged release and archived with a DOI.

## Associated article

[Author name(s)], “[Article title],” [Journal name], [year].

Preprint or article link: `[URL]`

Software archive DOI: `[DOI after Zenodo archival]`

## Citation

If you use this code, please cite the associated article and the archived software release:

```text
[Author name(s)]. Bounded Fermi–Dirac Integral: Computational Supplement.
Version [VERSION]. Zenodo. [DOI].
```

## License

This code is distributed under the `[LICENSE NAME]` license. See `LICENSE` for details.

## Contact

For questions about the computational supplement, please contact:

Paul Zheng  
[EMAIL ADDRESS]