import numpy as np
import matplotlib
matplotlib.use('Agg') # Prevents GUI windows from popping up
import matplotlib.pyplot as plt

P_TX, TX_H, RX_H, RX_AREA = 1.0, 3.0, 0.85, 1e-4
FOV = np.deg2rad(60); M_WIDE, M_FOCUS = 1, 10
BANDWIDTH, RESP = 20e6, 0.5
Q_E, K_B, T_K, R_L = 1.602e-19, 1.38e-23, 298, 1000
THERMAL_VAR = 4 * K_B * T_K * BANDWIDTH / R_L
X = np.linspace(-5, 5, 400)

def rx_power(x, tx_x=0.0, p_tx=P_TX, m=M_WIDE):
    d = np.sqrt((x - tx_x)**2 + (TX_H - RX_H)**2)
    c = np.clip((TX_H - RX_H) / d, 0, 1)
    psi = np.arccos(c)
    g = np.where((c > 0) & (psi <= FOV), ((m + 1) / (2 * np.pi * d**2)) * (c**m) * RX_AREA * c, 0.0)
    return p_tx * g

def snr_db(p):
    i = p * RESP; n = THERMAL_VAR + 2 * Q_E * i * BANDWIDTH
    return np.where(n > 0, 10 * np.log10(np.where(i > 0, i*i/n, 1e-12)), -np.inf)

def rate_mbps(s_db):
    lin = np.clip(10**(np.nan_to_num(s_db, neginf=-100)/10), 0, None)
    return BANDWIDTH * np.log2(1 + lin) / 1e6

def savefig(fig, name):
    fig.tight_layout(); fig.savefig(name, dpi=300, bbox_inches="tight"); plt.close(fig)
