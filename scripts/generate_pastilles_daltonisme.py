"""Genere le visuel pastilles vision normale vs deuteranopie."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
ASSETS = PROJECT / "_assets"
ASSETS.mkdir(exist_ok=True)


def srgb_to_linear(c):
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(c):
    return np.where(c <= 0.0031308, c * 12.92, 1.055 * c ** (1 / 2.4) - 0.055)


def simulate_deuteranopia(rgb):
    """Simulation de deuteranopie (Brettel 1997)."""
    lin = srgb_to_linear(np.array(rgb))
    # Matrice de simulation deuteranopie
    M = np.array([
        [0.625, 0.375, 0.0],
        [0.700, 0.300, 0.0],
        [0.000, 0.300, 0.700],
    ])
    out = M @ lin
    out = np.clip(out, 0, 1)
    return tuple(linear_to_srgb(out))


statuts = [
    ("En retard", (0.90, 0.20, 0.15)),
    ("En cours",  (1.00, 0.65, 0.00)),
    ("Termine",   (0.15, 0.68, 0.25)),
]

from matplotlib import font_manager
font_manager.fontManager.addfont(str(Path.home() / "Library/Fonts/Marianne-Regular.ttf"))
font_manager.fontManager.addfont(str(Path.home() / "Library/Fonts/Marianne-Bold.ttf"))
plt.rcParams["font.family"] = ["Marianne", "Arial", "sans-serif"]

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(9, 2.5))

# Colonnes 1 et 2 : pastilles sans légende
for ax, title, transform in [
    (ax1, "Vision normale", lambda c: c),
    (ax2, "Vision daltonienne", simulate_deuteranopia),
]:
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-0.5, len(statuts) - 0.5)
    ax.set_aspect("equal")
    ax.set_title(title, fontsize=14, fontweight="bold", pad=8)
    ax.axis("off")

    for i, (_, color) in enumerate(statuts):
        y = len(statuts) - 1 - i
        sim_color = transform(color)
        circle = plt.Circle((1.0, y), 0.35, color=sim_color, ec="black", lw=0.8)
        ax.add_patch(circle)

# Colonne 3 : pastilles avec légende textuelle
ax3.set_xlim(-0.5, 5.0)
ax3.set_ylim(-0.5, len(statuts) - 0.5)
ax3.set_aspect("equal")
ax3.set_title("Couleur + légende", fontsize=14, fontweight="bold", pad=8,
              color="black")
ax3.axis("off")

for i, (label, color) in enumerate(statuts):
    y = len(statuts) - 1 - i
    circle = plt.Circle((1.0, y), 0.35, color=color, ec="black", lw=0.8)
    ax3.add_patch(circle)
    ax3.text(1.7, y, label, va="center", ha="left", fontsize=14,
             fontweight="bold")

fig.tight_layout()

output = ASSETS / "pastilles-daltonisme.png"
fig.savefig(output, dpi=200, bbox_inches="tight", facecolor="white")
plt.close(fig)
print(f"-> {output.name}")
