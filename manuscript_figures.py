"""Generate the two manuscript-only organizational figures.

These figures do not replace the executed numerical supplement. They use the
same bounded integral definition and the saved Poisson precision-audit data to
make the paper's Section 3 and Section 4 claims visually explicit, while
matching the visual grammar of the existing supplement figures.
"""
from pathlib import Path
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.special import expit

ROOT = Path(__file__).resolve().parent
FIG = ROOT / "figures"
DATA = ROOT / "data"
FIG.mkdir(exist_ok=True)
DATA.mkdir(exist_ok=True)

plt.rcParams.update({
    'figure.figsize': (3.5, 3.0),
    'figure.dpi': 120,
    'savefig.dpi': 300,
    'font.size': 9,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'font.family': 'serif',
    'mathtext.fontset': 'dejavuserif',
    'text.usetex': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'svg.fonttype': 'path',
    'lines.linewidth': 1.2,
    'lines.markersize': 4,
})

# Match the grayscale/marker grammar of the executed supplement.
styles = {
    10: dict(ls='--', marker='^', color='black'),
    20: dict(ls=':', marker='s', color='dimgray'),
    30: dict(ls='-.', marker='o', color='darkgray'),
    50: dict(ls='-', marker='D', color='0.35'),
    100: dict(ls=(0, (5, 2, 1, 2)), marker='v', color='0.55'),
}

def style(key, n):
    st = styles[key].copy()
    st['markevery'] = max(1, int(n * 0.12))
    st['markerfacecolor'] = 'white'
    return st


def labels(ax, x=r'$\mu$', y=r'$F_{1/2}(\mu;1,a)$'):
    ax.text(1.02, -.1, x, transform=ax.transAxes, ha='left', va='bottom', fontsize=10)
    ax.text(-.1, 1.02, y, transform=ax.transAxes, ha='left', va='bottom', fontsize=10)
    ax.grid(True, ls=':', alpha=.6)


def save(fig, stem):
    for ext in ('pdf', 'svg', 'png'):
        fig.savefig(FIG / f"{stem}.{ext}", format=ext, dpi=300,
                    bbox_inches='tight', pad_inches=.04)
    plt.close(fig)


def finite_endpoint_family():
    # High-order Gauss-Legendre quadrature for a smooth presentation plot.
    a_values = [10, 20, 30, 50, 100]
    mu_grid = np.linspace(-5.0, 105.0, 321)
    nodes, weights = np.polynomial.legendre.leggauss(500)
    rows = []

    fig, ax = plt.subplots()
    for a in a_values:
        x = 0.5 * a * (nodes + 1.0)
        w = 0.5 * a * weights
        vals = np.array([np.sum(w * np.sqrt(x) * expit(mu - x)) for mu in mu_grid])
        ax.plot(mu_grid, vals, label=rf'$a={a}$', **style(a, len(mu_grid)))
        rows.extend({"a": a, "mu": float(mu), "F_half": float(val)}
                    for mu, val in zip(mu_grid, vals))

    labels(ax, x=r'$\mu$', y=r'$F_{1/2}(\mu;1,a)$')
    ax.legend(frameon=False, fontsize=7, loc='upper left')
    save(fig, '21_Bounded_Cutoff_Family')

    with (DATA / 'cutoff_family.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['a', 'mu', 'F_half'])
        writer.writeheader()
        writer.writerows(rows)


def poisson_convergence_figure():
    p = DATA / 'poisson_precision_audit.csv'
    arr = np.genfromtxt(p, delimiter=',', names=True)
    N = arr['N']

    fig, ax = plt.subplots()
    ax.loglog(N, arr['double_error'], 'k--o', mfc='white', label='Binary64 moments')
    ax.loglog(N, arr['high_precision_truncation_error'], color='dimgray', ls='-', marker='s',
              mfc='white', label='80-digit residual')
    ax.axhline(np.finfo(float).eps, color='0.55', ls=':', lw=1,
               label=r'$\epsilon_{\mathrm{mach}}$')
    labels(ax, x=r'$N$', y='Error')
    ax.legend(frameon=False, fontsize=7, loc='lower left')
    save(fig, '22_Poisson_Convergence_Bound')


if __name__ == '__main__':
    finite_endpoint_family()
    poisson_convergence_figure()
    print('Wrote manuscript figures 21 and 22 plus data/cutoff_family.csv')
