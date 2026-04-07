# esgenie_app.py
# ESGenie 🌿 — Sustainable Portfolio Advisor

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# ── Page config ───────────────────────────────────────────────────────
st.set_page_config(
    page_title="ESGenie — Sustainable Portfolio Advisor",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Jost:wght@300;400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'Jost', sans-serif; }
.stApp { background-color: #f9faf5; color: #1c2e1c; }
h1,h2,h3,h4 { font-family:'Cormorant Garamond',serif !important; color:#1c3a1c !important; }
label, .stRadio label, .stSlider label, .stSelectbox label,
.stTextInput label, .stNumberInput label, .stCheckbox label {
    font-family:'Jost',sans-serif !important; font-weight:500 !important;
    color:#2a4a2a !important; font-size:0.88rem !important;
}
p, span, div { color:#1c2e1c; }

/* HERO */
.hero {
    background: linear-gradient(160deg, #1c3a1c 0%, #2d5a2d 45%, #3a7a4a 100%);
    border-radius: 18px; padding: 3rem 3.5rem 2.8rem; margin-bottom: 2rem;
    position: relative; overflow: hidden;
    box-shadow: 0 12px 40px rgba(28,58,28,0.22);
}
.hero::after {
    content:""; position:absolute; top:-40px; right:-40px;
    width:260px; height:260px;
    background:radial-gradient(circle,rgba(255,255,255,0.05) 0%,transparent 70%);
    border-radius:50%;
}
.hero-eyebrow {
    font-family:'Jost',sans-serif; font-size:0.72rem; font-weight:600;
    letter-spacing:2.5px; text-transform:uppercase; color:#74c494; margin-bottom:0.6rem;
}
.hero-title {
    font-family:'Cormorant Garamond',serif; font-size:3.8rem; font-weight:700;
    color:#e8f5e4; margin:0 0 0.3rem; line-height:1.05; letter-spacing:-1px;
}
.hero-sub {
    font-size:1.05rem; color:#a8d8b4; margin:0 0 1.4rem; font-weight:300;
    max-width:520px; line-height:1.6;
}
.hero-pills { display:flex; gap:0.5rem; flex-wrap:wrap; }
.hero-pill {
    background:rgba(255,255,255,0.1); border:1px solid rgba(255,255,255,0.18);
    color:#c8edd4; border-radius:30px; padding:0.22rem 0.9rem;
    font-size:0.72rem; font-weight:500;
}

/* HOW TO */
.howto-wrap {
    background:white; border:1px solid #d4e8d4; border-radius:16px;
    padding:2rem 2.2rem 1.8rem; margin-bottom:1.8rem;
    box-shadow:0 2px 18px rgba(28,58,28,0.06);
}
.howto-heading {
    font-family:'Cormorant Garamond',serif; font-size:1.55rem;
    font-weight:600; color:#1c3a1c; margin-bottom:0.2rem;
}
.howto-sub { font-size:0.85rem; color:#5a8a5a; margin-bottom:1.4rem; font-weight:300; }
.howto-grid { display:grid; grid-template-columns:repeat(5,1fr); gap:0.85rem; }
.howto-card {
    background:linear-gradient(160deg,#f2faf4 0%,#eaf5ec 100%);
    border:1px solid #c8e8cc; border-radius:12px; padding:1.1rem 0.9rem 1rem; text-align:center;
    transition:transform 0.2s ease, box-shadow 0.2s ease;
}
.howto-card:hover { transform:translateY(-3px); box-shadow:0 6px 18px rgba(28,58,28,0.1); }
.howto-icon  { font-size:1.75rem; margin-bottom:0.4rem; display:block; }
.howto-num   { font-size:0.62rem; font-weight:700; letter-spacing:1.5px; text-transform:uppercase;
               color:#5a9a6a; margin-bottom:0.2rem; }
.howto-t     { font-family:'Cormorant Garamond',serif; font-size:0.95rem;
               font-weight:600; color:#1c3a1c; margin-bottom:0.3rem; }
.howto-d     { font-size:0.74rem; color:#5a7a5a; line-height:1.45; font-weight:300; }

/* PROGRESS BAR */
.progress-bar {
    background:white; border:1px solid #d4e8d4; border-radius:50px;
    padding:0.7rem 1.8rem; margin-bottom:1.5rem; display:flex;
    align-items:center; justify-content:space-between;
    box-shadow:0 1px 8px rgba(0,0,0,0.04);
}
.pb-step { display:flex; align-items:center; gap:0.5rem; }
.pb-dot {
    width:28px; height:28px; border-radius:50%; display:flex;
    align-items:center; justify-content:center; font-size:0.75rem; font-weight:700;
    background:#e4f2e6; color:#5a9a6a; border:1.5px solid #b8dcc0; flex-shrink:0;
}
.pb-dot.done { background:#2d5a2d; color:white; border-color:#2d5a2d; }
.pb-label { font-size:0.76rem; color:#4a7a4a; font-weight:500; }
.pb-line { flex:1; height:1px; background:#c8e4c8; margin:0 0.4rem; }

/* BUTTONS */
.stButton > button {
    font-family:'Jost',sans-serif !important; font-size:0.83rem !important;
    font-weight:500 !important; background:white !important; color:#2d5a2d !important;
    border:1.5px solid #b8dcc0 !important; border-radius:8px !important;
    transition:all 0.18s ease !important;
}
.stButton > button:hover {
    background:#2d5a2d !important; color:white !important;
    border-color:#2d5a2d !important; box-shadow:0 4px 14px rgba(45,90,45,0.25) !important;
}
.stButton > button[kind="primary"] {
    background:linear-gradient(135deg,#1c3a1c,#2d5a2d) !important; color:white !important;
    border:none !important; font-size:1rem !important; font-weight:600 !important;
    letter-spacing:0.3px !important; padding:0.65rem 2rem !important;
    box-shadow:0 5px 18px rgba(28,58,28,0.3) !important; border-radius:10px !important;
}
.stButton > button[kind="primary"]:hover {
    background:linear-gradient(135deg,#2d5a2d,#3a7a4a) !important;
    box-shadow:0 7px 24px rgba(28,58,28,0.4) !important; transform:translateY(-1px) !important;
}

/* EXPANDERS */
details[data-testid="stExpander"] {
    border:1px solid #d0e8d0 !important; border-radius:12px !important;
    margin-bottom:0.8rem !important; overflow:hidden; background:white !important;
    box-shadow:0 1px 6px rgba(0,0,0,0.04) !important;
}
details[data-testid="stExpander"] summary {
    background:#f5faf5 !important; color:#1c3a1c !important;
    font-family:'Cormorant Garamond',serif !important; font-size:1.05rem !important;
    font-weight:600 !important; padding:0.85rem 1.2rem !important;
    border-bottom:1px solid #d0e8d0;
}
details[open] > summary { background:#1c3a1c !important; color:#e8f5e4 !important; border-bottom:none !important; }
details[open] > summary svg { fill:#e8f5e4 !important; }
details[data-testid="stExpander"] > div { background:white !important; padding:1.2rem 1.4rem !important; }

/* LABELS & TIPS */
.sec-label {
    font-family:'Jost',sans-serif; font-size:0.7rem; font-weight:700;
    letter-spacing:1.8px; text-transform:uppercase; color:#5a9a6a;
    margin-bottom:0.5rem; padding-bottom:0.3rem; border-bottom:1px solid #d4e8d4;
}
.expander-desc {
    font-size:0.82rem; color:#6a8a6a; font-style:italic; margin-bottom:1rem;
    padding:0.5rem 0.8rem; background:#f5faf5;
    border-left:3px solid #5a9a6a; border-radius:0 6px 6px 0;
}
.tip-strip {
    background:#f0faf2; border:1px solid #9acea8; border-radius:8px;
    padding:0.65rem 1rem; font-size:0.82rem; color:#2a5a2a; margin:0.5rem 0;
}
.info-strip {
    background:#edf5ff; border:1px solid #aacfee; border-radius:8px;
    padding:0.75rem 1rem; font-size:0.85rem; color:#1a4a7a; margin:0.5rem 0;
}

/* METRIC CARDS */
.m-card {
    background:white; border:1px solid #d4e8d4; border-radius:12px;
    padding:1rem 1.1rem; text-align:center;
    box-shadow:0 1px 8px rgba(28,58,28,0.05);
}
.m-label { font-size:0.68rem; font-weight:700; text-transform:uppercase;
           letter-spacing:1px; color:#7aaa7a; margin-bottom:0.3rem; }
.m-value { font-family:'Cormorant Garamond',serif; font-size:1.65rem;
           font-weight:700; color:#1c3a1c; line-height:1.1; }
.m-delta { font-size:0.72rem; color:#7a9a7a; margin-top:0.2rem; font-weight:300; }

/* SECTION HEADER */
.sec-header {
    font-family:'Cormorant Garamond',serif; font-size:1.3rem; font-weight:600;
    color:#1c3a1c; border-left:4px solid #3a7a4a; padding-left:0.7rem;
    margin:1.5rem 0 0.7rem;
}

/* RECO BOX */
.reco-box {
    background:linear-gradient(145deg,#edf7ef,#e0f2e4); border:1px solid #8ac89a;
    border-left:5px solid #2d5a2d; border-radius:12px; padding:1.3rem 1.6rem;
    font-size:0.93rem; color:#1c3a1c; line-height:1.75; margin:0.8rem 0;
}

/* ESG PILLS */
.p-high { background:#e0f5e4; color:#1c6a1c; border:1px solid #7ac47a;
          border-radius:20px; padding:2px 11px; font-size:0.76rem; font-weight:600; }
.p-mid  { background:#fdf5e0; color:#7a5a00; border:1px solid #e4c46a;
          border-radius:20px; padding:2px 11px; font-size:0.76rem; font-weight:600; }
.p-low  { background:#fde8e8; color:#8a1c1c; border:1px solid #e49a9a;
          border-radius:20px; padding:2px 11px; font-size:0.76rem; font-weight:600; }

/* ASSET CARD */
.asset-card {
    background:white; border:1px solid #d4e8d4; border-radius:12px;
    padding:1.2rem 1.4rem; box-shadow:0 2px 10px rgba(28,58,28,0.05);
}
.asset-name { font-family:'Cormorant Garamond',serif; font-size:1.1rem;
              font-weight:700; color:#1c3a1c; margin-bottom:0.4rem; }
.asset-esg-score { font-family:'Cormorant Garamond',serif; font-size:2rem;
                   font-weight:700; color:#2d5a2d; line-height:1; }

/* TABS */
[data-testid="stTabs"] [role="tab"] {
    font-family:'Jost',sans-serif !important; font-weight:600 !important;
    font-size:0.88rem !important; color:#5a8a5a !important;
}
[data-testid="stTabs"] [role="tab"][aria-selected="true"] {
    color:#1c3a1c !important; border-bottom:3px solid #3a7a4a !important;
}

/* DATAFRAME */
[data-testid="stDataFrame"] {
    border-radius:10px !important; overflow:hidden; border:1px solid #d4e8d4 !important;
}

/* INPUTS */
[data-baseweb="input"] input, [data-baseweb="base-input"] input {
    background:#f5faf5 !important; border:1px solid #c8e4c8 !important;
    border-radius:7px !important; color:#1c3a1c !important;
    font-family:'Jost',sans-serif !important;
}
[data-baseweb="select"] > div {
    background:#f5faf5 !important; border:1px solid #c8e4c8 !important; border-radius:7px !important;
}

/* DOWNLOAD */
.stDownloadButton > button {
    background:white !important; color:#2d5a2d !important;
    border:1.5px solid #2d5a2d !important; border-radius:8px !important;
    font-family:'Jost',sans-serif !important; font-weight:600 !important;
}
.stDownloadButton > button:hover { background:#2d5a2d !important; color:white !important; }

/* DIVIDER */
.green-rule {
    height:2px; background:linear-gradient(90deg,#2d5a2d,#7ac47a,transparent);
    border:none; border-radius:2px; margin:1.8rem 0;
}

/* LANDING */
.landing-box {
    background:linear-gradient(145deg,#edf7ef 0%,#e4f5e8 100%);
    border:1px solid #b8dcc0; border-radius:14px; padding:1.8rem 2.2rem;
    margin-top:0.5rem; text-align:center;
}

/* FOOTER */
.footer {
    text-align:center; padding:1.5rem; color:#7aaa7a; font-size:0.76rem;
    border-top:1px solid #d4e8d4; margin-top:2rem; font-weight:300; letter-spacing:0.3px;
}

.stCaption { color:#6a8a6a !important; font-size:0.8rem !important; }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════
# PURE FUNCTIONS  —  DO NOT MODIFY
# ══════════════════════════════════════════════════════════════════════

def classify_esg(score):
    if score >= 80:   return "High ESG",     '<span class="p-high">🌿 High ESG</span>'
    elif score >= 50: return "Moderate ESG", '<span class="p-mid">🌤 Moderate ESG</span>'
    else:             return "Low ESG",      '<span class="p-low">⚠️ Low ESG</span>'

def compute_esg(E, S, G, w_e, w_s, w_g):
    return w_e * E + w_s * S + w_g * G

def portfolio_ret(w1, r1, r2):
    return w1 * r1 + (1 - w1) * r2

def portfolio_sd(w1, sd1, sd2, rho):
    var = (w1**2 * sd1**2
           + (1 - w1)**2 * sd2**2
           + 2 * rho * w1 * (1 - w1) * sd1 * sd2)
    return np.sqrt(np.maximum(var, 0.0))

def portfolio_esg(w1, esg1, esg2):
    return w1 * esg1 + (1 - w1) * esg2

def sharpe_ratio(w1, r1, r2, sd1, sd2, rho, r_free):
    ret = portfolio_ret(w1, r1, r2)
    sd  = portfolio_sd(w1, sd1, sd2, rho)
    if sd == 0: return 0.0
    return (ret - r_free) / sd

def utility(w1, r1, r2, sd1, sd2, rho, r_free,
            gamma, theta, esg1, esg2,
            sin_choice, excluded, name1, name2,
            apply_threshold, threshold, penalty_strength):
    """
    ESG-adjusted mean-variance utility (Lecture 6):
      U = (E[r_p] - r_f) - (gamma/2).sigma^2_p + theta.(ESG_p/100)
    Plus shortfall penalty and hard sin stock exclusion.
    """
    ret = portfolio_ret(w1, r1, r2)
    sd  = portfolio_sd(w1, sd1, sd2, rho)
    esg = portfolio_esg(w1, esg1, esg2)
    base = (ret - r_free) - (gamma / 2) * sd**2 + theta * (esg / 100)
    excl = 0.0
    if sin_choice == 1:
        if name1 in excluded and w1 > 0:  excl -= 1e6 * w1
        if name2 in excluded and w1 < 1:  excl -= 1e6 * (1 - w1)
    thr = 0.0
    if apply_threshold and esg < threshold:
        thr = -penalty_strength * ((threshold - esg) / 100) ** 2
    return base + excl + thr

def run_optimisation(r1, r2, sd1, sd2, rho, r_free,
                     gamma, theta, esg1, esg2,
                     sin_choice, excluded, name1, name2,
                     apply_threshold, threshold, penalty_strength, n=1000):
    weights = np.linspace(0, 1, n)
    utils   = np.array([utility(w, r1, r2, sd1, sd2, rho, r_free, gamma, theta,
                                esg1, esg2, sin_choice, excluded, name1, name2,
                                apply_threshold, threshold, penalty_strength)
                        for w in weights])
    sharpes = np.array([sharpe_ratio(w, r1, r2, sd1, sd2, rho, r_free) for w in weights])
    rets    = np.array([portfolio_ret(w, r1, r2)       for w in weights])
    risks   = np.array([portfolio_sd(w, sd1, sd2, rho) for w in weights])
    esgs    = np.array([portfolio_esg(w, esg1, esg2)   for w in weights])
    oi, ti, mi = np.argmax(utils), np.argmax(sharpes), np.argmin(risks)
    return dict(
        weights=weights, utils=utils, sharpes=sharpes,
        rets=rets, risks=risks, esgs=esgs,
        w1_optimal  =weights[oi], ret_optimal  =rets[oi],
        sd_optimal  =risks[oi],   esg_optimal  =esgs[oi],  sr_optimal  =sharpes[oi],
        w1_tangency =weights[ti], ret_tangency =rets[ti],
        sd_tangency =risks[ti],   esg_tangency =esgs[ti],  sr_tangency =sharpes[ti],
        w1_min_var  =weights[mi], ret_min_var  =rets[mi],
        sd_min_var  =risks[mi],   esg_min_var  =esgs[mi],  sr_min_var  =sharpes[mi],
    )

@st.cache_data(show_spinner=False)
def cached_sensitivity(r1, r2, sd1, sd2, rho, r_free,
                       gamma, theta, esg1, esg2,
                       sin_choice, excluded_tuple, name1, name2,
                       apply_threshold, threshold, penalty_strength):
    excluded = dict(excluded_tuple)
    theta_range = np.linspace(0, 4, 60)
    gamma_range = np.linspace(1, 15, 60)
    theta_grid  = np.linspace(0, 4, 12)
    gamma_grid  = np.linspace(1, 15, 12)

    def opt(t, g):
        res = run_optimisation(r1, r2, sd1, sd2, rho, r_free, g, t,
                               esg1, esg2, sin_choice, excluded, name1, name2,
                               apply_threshold, threshold, penalty_strength, n=500)
        return res["w1_optimal"]

    sa_w, sa_esg, sa_sr = [], [], []
    for t in theta_range:
        w = opt(t, gamma)
        sa_w.append(w * 100)
        sa_esg.append(portfolio_esg(w, esg1, esg2))
        sa_sr.append(sharpe_ratio(w, r1, r2, sd1, sd2, rho, r_free))

    sg_sr = []
    for g in gamma_range:
        w = opt(theta, g)
        sg_sr.append(sharpe_ratio(w, r1, r2, sd1, sd2, rho, r_free))

    heatmap = np.zeros((len(gamma_grid), len(theta_grid)))
    for i, g in enumerate(gamma_grid):
        for j, t in enumerate(theta_grid):
            heatmap[i, j] = portfolio_esg(opt(t, g), esg1, esg2)

    return (theta_range, gamma_range, theta_grid, gamma_grid,
            np.array(sa_w), np.array(sa_esg), np.array(sa_sr),
            np.array(sg_sr), heatmap)


# ══════════════════════════════════════════════════════════════════════
# CONSTANTS
# ══════════════════════════════════════════════════════════════════════
PRESETS = {
    "🌿 Eco-First":           dict(r1=8,  sd1=22, r2=4,  sd2=10, rho=0.15, rfree=2.0, risk=0, theta=3.8, focus=0, thr=60,  use_thr=True),
    "⚖️ Balanced":            dict(r1=8,  sd1=20, r2=4,  sd2=10, rho=0.20, rfree=2.0, risk=1, theta=2.0, focus=3, thr=0,   use_thr=False),
    "🛡️ Conservative Green":  dict(r1=6,  sd1=14, r2=3,  sd2=7,  rho=0.10, rfree=2.0, risk=0, theta=2.5, focus=3, thr=50,  use_thr=True),
    "🚀 Growth Hunter":       dict(r1=14, sd1=30, r2=5,  sd2=12, rho=0.25, rfree=2.0, risk=2, theta=0.5, focus=3, thr=0,   use_thr=False),
    "🤝 Social Impact":       dict(r1=7,  sd1=18, r2=4,  sd2=9,  rho=0.18, rfree=2.0, risk=1, theta=3.0, focus=1, thr=55,  use_thr=True),
}
PILLAR_OPTIONS = [
    "🌍 Environmental focus  (E=0.60, S=0.20, G=0.20)",
    "🤝 Social focus         (E=0.20, S=0.60, G=0.20)",
    "🏛️ Governance focus     (E=0.20, S=0.20, G=0.60)",
    "⚖️ Balanced ESG         (E=0.34, S=0.33, G=0.33)",
]
PILLAR_WEIGHTS = {
    0: (0.60, 0.20, 0.20, "Environmental focus"),
    1: (0.20, 0.60, 0.20, "Social focus"),
    2: (0.20, 0.20, 0.60, "Governance focus"),
    3: (0.34, 0.33, 0.33, "Balanced ESG"),
}
RISK_MAP    = {0: (10, "Conservative"), 1: (5, "Balanced"), 2: (2, "Aggressive")}
SIN_SECTORS = {"Tobacco", "Weapons & Defence", "Gambling", "Fossil Fuels"}
SECTORS     = ["Technology", "Healthcare", "Financial Services", "Consumer Goods",
               "Energy", "Fossil Fuels", "Tobacco", "Weapons & Defence", "Gambling", "Other"]

if "preset" not in st.session_state:
    st.session_state.preset = None


# ══════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero">
  <div style="display:flex; align-items:center; gap:2rem;">

    <!-- GENIE SVG ILLUSTRATION -->
    <div style="flex-shrink:0;">
      <svg width="130" height="160" viewBox="0 0 130 160" xmlns="http://www.w3.org/2000/svg">
        <!-- Lamp -->
        <ellipse cx="65" cy="148" rx="38" ry="7" fill="rgba(255,255,255,0.08)"/>
        <path d="M28 140 Q40 130 55 135 Q65 138 75 135 Q90 130 102 140 Q95 148 65 148 Q35 148 28 140Z"
              fill="#c8a84b" opacity="0.9"/>
        <path d="M55 135 Q65 120 75 135" fill="#e8c86a" opacity="0.9"/>
        <ellipse cx="65" cy="135" rx="12" ry="4" fill="#e8c86a" opacity="0.7"/>
        <!-- Spout -->
        <path d="M28 140 Q15 132 10 124 Q18 118 30 126 Q32 133 28 140Z"
              fill="#c8a84b" opacity="0.9"/>
        <!-- Handle -->
        <path d="M102 140 Q118 136 120 128 Q118 120 108 122 Q104 130 102 140Z"
              fill="#c8a84b" opacity="0.9"/>

        <!-- Smoke / magic swirl rising from lamp -->
        <path d="M65 130 Q58 115 65 100 Q72 85 63 70 Q56 57 65 44"
              stroke="rgba(168,230,180,0.35)" stroke-width="14" fill="none"
              stroke-linecap="round"/>
        <path d="M65 130 Q72 115 65 100 Q58 85 67 70 Q74 57 65 44"
              stroke="rgba(168,230,180,0.2)" stroke-width="10" fill="none"
              stroke-linecap="round"/>

        <!-- Genie body (emerging from smoke) -->
        <!-- Torso -->
        <ellipse cx="65" cy="88" rx="20" ry="26" fill="#74c494" opacity="0.92"/>
        <!-- Belly detail -->
        <ellipse cx="65" cy="94" rx="12" ry="14" fill="#95d5b2" opacity="0.45"/>

        <!-- Left arm -->
        <path d="M45 78 Q30 72 28 62 Q34 58 42 66 Q46 72 48 80Z"
              fill="#74c494" opacity="0.92"/>
        <!-- Right arm (raised / waving) -->
        <path d="M85 78 Q98 64 104 56 Q110 60 106 68 Q98 76 88 82Z"
              fill="#74c494" opacity="0.92"/>
        <!-- Right hand sparkle -->
        <circle cx="107" cy="54" r="3" fill="#ffd700" opacity="0.9"/>
        <circle cx="113" cy="50" r="2" fill="#ffd700" opacity="0.7"/>
        <circle cx="103" cy="48" r="2" fill="#ffd700" opacity="0.7"/>
        <path d="M107 54 L113 50 M107 54 L103 48 M107 54 L110 60"
              stroke="#ffd700" stroke-width="1.2" opacity="0.8"/>

        <!-- Neck -->
        <rect x="59" y="62" width="12" height="10" rx="5" fill="#95d5b2"/>

        <!-- Head -->
        <ellipse cx="65" cy="52" rx="18" ry="20" fill="#a8e6b8"/>
        <!-- Head shading -->
        <ellipse cx="60" cy="48" rx="10" ry="12" fill="rgba(255,255,255,0.12)"/>

        <!-- Turban base -->
        <ellipse cx="65" cy="34" rx="18" ry="7" fill="#1c3a1c"/>
        <!-- Turban wrap -->
        <path d="M47 34 Q65 22 83 34 Q75 42 65 40 Q55 42 47 34Z"
              fill="#2d5a2d"/>
        <!-- Turban highlight -->
        <path d="M52 31 Q65 24 78 31" stroke="rgba(168,230,180,0.5)"
              stroke-width="2" fill="none" stroke-linecap="round"/>
        <!-- Jewel on turban -->
        <ellipse cx="65" cy="33" rx="5" ry="4" fill="#ffd700" opacity="0.9"/>
        <ellipse cx="65" cy="33" rx="3" ry="2.5" fill="#fff8dc" opacity="0.7"/>

        <!-- Eyes -->
        <ellipse cx="59" cy="50" rx="3.5" ry="4" fill="#1c3a1c"/>
        <ellipse cx="71" cy="50" rx="3.5" ry="4" fill="#1c3a1c"/>
        <!-- Eye shine -->
        <circle cx="60.5" cy="49" r="1.2" fill="white" opacity="0.8"/>
        <circle cx="72.5" cy="49" r="1.2" fill="white" opacity="0.8"/>

        <!-- Eyebrows -->
        <path d="M55 45 Q59 43 63 45" stroke="#1c3a1c" stroke-width="1.5"
              fill="none" stroke-linecap="round"/>
        <path d="M67 45 Q71 43 75 45" stroke="#1c3a1c" stroke-width="1.5"
              fill="none" stroke-linecap="round"/>

        <!-- Smile -->
        <path d="M59 57 Q65 62 71 57" stroke="#1c3a1c" stroke-width="1.8"
              fill="none" stroke-linecap="round"/>

        <!-- Floating sparkles around genie -->
        <circle cx="22" cy="90" r="2.5" fill="#ffd700" opacity="0.6"/>
        <circle cx="18" cy="80" r="1.5" fill="#a8e6b8" opacity="0.7"/>
        <circle cx="26" cy="74" r="2" fill="#ffd700" opacity="0.5"/>
        <circle cx="108" cy="90" r="2" fill="#a8e6b8" opacity="0.6"/>
        <circle cx="114" cy="80" r="1.5" fill="#ffd700" opacity="0.7"/>
      </svg>
    </div>

    <!-- TITLE BLOCK -->
    <div style="flex:1;">
      <div class="hero-eyebrow">🌱 Sustainable Finance · Portfolio Optimisation</div>
      <p style="
        font-family: 'Cormorant Garamond', serif;
        font-size: 5rem;
        font-weight: 700;
        color: #ffffff;
        margin: 0 0 0.15rem 0;
        line-height: 1;
        letter-spacing: -2px;
        text-shadow: 0 2px 24px rgba(0,0,0,0.35), 0 0 60px rgba(168,230,180,0.2);
      ">ESGenie</p>
      <p class="hero-sub">A personalised investment advisor that balances financial returns
      with your values — because profit and purpose can coexist.</p>
      <div class="hero-pills">
        <span class="hero-pill">🌍 ESG Scoring</span>
        <span class="hero-pill">📐 Mean-Variance Optimisation</span>
        <span class="hero-pill">🛡️ Ethical Screening</span>
        <span class="hero-pill">🔬 Sensitivity Analysis</span>
        <span class="hero-pill">📊 Efficient Frontier</span>
      </div>
    </div>

  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════
# HOW TO USE  (always visible at top, before any inputs)
# ══════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="howto-wrap">
  <div class="howto-heading">📖 How to Use ESGenie</div>
  <div class="howto-sub">New here? Follow these five steps in order to generate your personalised sustainable portfolio.</div>
  <div class="howto-grid">
    <div class="howto-card">
      <span class="howto-icon">📈</span>
      <div class="howto-num">Step 01</div>
      <div class="howto-t">Enter Financial Data</div>
      <div class="howto-d">Provide expected returns, standard deviations, asset correlation, and the risk-free rate.</div>
    </div>
    <div class="howto-card">
      <span class="howto-icon">🧭</span>
      <div class="howto-num">Step 02</div>
      <div class="howto-t">Set Risk Profile</div>
      <div class="howto-d">Tell us how comfortable you are with volatility — this sets your risk aversion coefficient γ.</div>
    </div>
    <div class="howto-card">
      <span class="howto-icon">🌱</span>
      <div class="howto-num">Step 03</div>
      <div class="howto-t">Define ESG Priorities</div>
      <div class="howto-d">Choose your ESG weight θ and which pillar — Environment, Social, or Governance — matters most to you.</div>
    </div>
    <div class="howto-card">
      <span class="howto-icon">🔍</span>
      <div class="howto-num">Step 04</div>
      <div class="howto-t">Score & Screen Assets</div>
      <div class="howto-d">Rate each asset on E, S, and G pillars (0–100). Optionally exclude controversial sectors.</div>
    </div>
    <div class="howto-card">
      <span class="howto-icon">✨</span>
      <div class="howto-num">Step 05</div>
      <div class="howto-t">Run & Explore</div>
      <div class="howto-d">Click Run Optimisation. Review your allocation, charts, and sensitivity analysis across three tabs.</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════
# PROGRESS BAR
# ══════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="progress-bar">
  <div class="pb-step"><div class="pb-dot done">01</div><span class="pb-label">Financial Data</span></div>
  <div class="pb-line"></div>
  <div class="pb-step"><div class="pb-dot done">02</div><span class="pb-label">Risk Profile</span></div>
  <div class="pb-line"></div>
  <div class="pb-step"><div class="pb-dot done">03</div><span class="pb-label">ESG Preferences</span></div>
  <div class="pb-line"></div>
  <div class="pb-step"><div class="pb-dot done">04</div><span class="pb-label">ESG Scores</span></div>
  <div class="pb-line"></div>
  <div class="pb-step"><div class="pb-dot done">05</div><span class="pb-label">Ethical Screening</span></div>
  <div class="pb-line"></div>
  <div class="pb-step">
    <div class="pb-dot" style="background:#e4f2e6;color:#5a9a6a;">✨</div>
    <span class="pb-label">Your Results</span>
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════
# QUICK-START PRESETS
# ══════════════════════════════════════════════════════════════════════
st.markdown("""
<div style="background:white;border:1px solid #d4e8d4;border-radius:12px;
            padding:1.2rem 1.6rem;margin-bottom:1.2rem;
            box-shadow:0 1px 8px rgba(28,58,28,0.05);">
  <div style="font-family:'Cormorant Garamond',serif;font-size:1.1rem;
              font-weight:600;color:#1c3a1c;margin-bottom:0.25rem;">
    ⚡ Quick-Start — Choose an Investor Profile
  </div>
  <div style="font-size:0.8rem;color:#6a8a6a;font-weight:300;">
    Load a pre-built investor profile to auto-fill all inputs instantly, or try the Apple vs BP worked example.
  </div>
</div>
""", unsafe_allow_html=True)

preset_cols = st.columns(len(PRESETS) + 1)
for col, pname in zip(preset_cols, PRESETS):
    with col:
        if st.button(pname, key=f"pre_{pname}", use_container_width=True):
            st.session_state.preset = pname
            st.rerun()

with preset_cols[-1]:
    if st.button("📋 Apple vs BP Example", use_container_width=True):
        st.session_state.update(dict(
            _name1="Apple", _name2="BP",
            _r1=12.0, _r2=6.0, _sd1=18.0, _sd2=22.0, _rho=-0.1, _rfree=4.5,
            _E1=78.0, _S1=72.0, _G1=81.0,
            _E2=32.0, _S2=41.0, _G2=55.0,
            _risk=0, _theta=2.5, _focus=0, _use_thr=True, _thr=50.0,
        ))
        st.session_state.preset = None
        st.rerun()

p = PRESETS.get(st.session_state.preset, {})

st.markdown('<div class="green-rule"></div>', unsafe_allow_html=True)
st.markdown("""
<div style="font-family:'Cormorant Garamond',serif;font-size:1.4rem;
            font-weight:600;color:#1c3a1c;margin-bottom:0.3rem;">
  Configure Your Portfolio Parameters
</div>
<div style="font-size:0.85rem;color:#6a8a6a;margin-bottom:1rem;font-weight:300;">
  Expand each section below, fill in your details, then click <strong>Run Optimisation</strong>.
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════
# 01 — FINANCIAL DATA
# ══════════════════════════════════════════════════════════════════════
with st.expander("01  ·  Financial Data", expanded=True):
    st.markdown('<div class="expander-desc">Enter the expected return and risk for each asset, their correlation, and the current risk-free rate (e.g. UK gilt yield).</div>', unsafe_allow_html=True)
    col_a, col_b = st.columns(2, gap="large")
    with col_a:
        st.markdown('<div class="sec-label">Asset 1</div>', unsafe_allow_html=True)
        name1 = st.text_input("Asset name", value=st.session_state.get("_name1", "Asset 1"), key="n1")
        r1    = st.number_input("Expected Return (%)", -50.0, 50.0,
                                float(p.get("r1",  st.session_state.get("_r1",  8.0))),  step=0.5) / 100
        sd1   = st.number_input("Standard Deviation (%)", 0.0, 100.0,
                                float(p.get("sd1", st.session_state.get("_sd1", 20.0))), step=0.5) / 100
    with col_b:
        st.markdown('<div class="sec-label">Asset 2</div>', unsafe_allow_html=True)
        name2 = st.text_input("Asset name", value=st.session_state.get("_name2", "Asset 2"), key="n2")
        r2    = st.number_input("Expected Return (%)", -50.0, 50.0,
                                float(p.get("r2",  st.session_state.get("_r2",  4.0))),  step=0.5, key="r2i") / 100
        sd2   = st.number_input("Standard Deviation (%)", 0.0, 100.0,
                                float(p.get("sd2", st.session_state.get("_sd2", 10.0))), step=0.5, key="sd2i") / 100
    col_c, col_d = st.columns(2, gap="large")
    with col_c:
        st.markdown('<div class="sec-label">Correlation between Assets</div>', unsafe_allow_html=True)
        rho = st.slider("ρ  (–1 = perfectly inverse  ·  0 = no link  ·  +1 = perfectly correlated)",
                        -1.0, 1.0, float(p.get("rho", st.session_state.get("_rho", 0.2))), step=0.05)
    with col_d:
        st.markdown('<div class="sec-label">Risk-Free Rate</div>', unsafe_allow_html=True)
        r_free = st.number_input("Risk-Free Rate (%) — e.g. current UK gilt yield", 0.0, 15.0,
                                 float(p.get("rfree", st.session_state.get("_rfree", 2.0))), step=0.25) / 100
    st.markdown('<div class="tip-strip">💡 <strong>Tip:</strong> Use annualised figures. A positive correlation means the assets tend to move together, reducing diversification benefits.</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════
# 02 — RISK PROFILE
# ══════════════════════════════════════════════════════════════════════
with st.expander("02  ·  Risk Profile", expanded=False):
    st.markdown('<div class="expander-desc">Your risk profile determines γ, the risk aversion coefficient in the utility function. A higher γ penalises portfolio volatility more heavily.</div>', unsafe_allow_html=True)
    risk_idx = st.radio(
        "How do you feel about investment risk?",
        [0, 1, 2],
        format_func=lambda x: [
            "🛡️  Conservative  —  I prioritise protecting my capital above all else",
            "⚖️  Balanced  —  I accept moderate fluctuations for reasonable returns",
            "🚀  Aggressive  —  I am comfortable with high volatility in pursuit of growth",
        ][x],
        index=int(p.get("risk", st.session_state.get("_risk", 1))),
        horizontal=False,
    )
    gamma, risk_label = RISK_MAP[risk_idx]
    risk_context = {
        0: "**Conservative (γ = 10):** The model strongly penalises volatility. You will typically be directed toward the lower-risk asset.",
        1: "**Balanced (γ = 5):** A middle-ground approach. The model weighs risk and return evenly alongside your ESG preferences.",
        2: "**Aggressive (γ = 2):** Volatility is minimally penalised. Higher-return assets are favoured unless ESG preferences pull strongly in the other direction.",
    }
    st.markdown(f'<div class="info-strip">ℹ️ {risk_context[risk_idx]}</div>', unsafe_allow_html=True)
    st.caption(f"Utility function: U = (E[rₚ] − r_f) − (γ/2)·σ²ₚ + θ·(ESGₚ/100)   →   γ = {gamma}")


# ══════════════════════════════════════════════════════════════════════
# 03 — ESG PREFERENCES
# ══════════════════════════════════════════════════════════════════════
with st.expander("03  ·  ESG Preferences", expanded=False):
    st.markdown('<div class="expander-desc">Set how strongly sustainability influences your recommendation. θ controls the ESG weight in the utility function; the pillar focus determines how E, S, and G are combined.</div>', unsafe_allow_html=True)
    col_e, col_f = st.columns(2, gap="large")
    with col_e:
        st.markdown('<div class="sec-label">ESG Weight in Utility (θ)</div>', unsafe_allow_html=True)
        theta = st.slider("0 = purely financial  ·  4 = ESG takes priority",
                          0.0, 4.0, float(p.get("theta", st.session_state.get("_theta", 2.0))), step=0.1)
        if theta == 0:        theta_desc = "🔵 Purely financial — ESG has no influence."
        elif theta < 1.5:     theta_desc = "🟡 Mild ESG preference — financial returns still dominate."
        elif theta < 3:       theta_desc = "🟢 Moderate ESG preference — a balanced sustainability stance."
        else:                 theta_desc = "🌿 Strong ESG preference — sustainability is your primary driver."
        st.caption(theta_desc)
    with col_f:
        st.markdown('<div class="sec-label">ESG Pillar Focus</div>', unsafe_allow_html=True)
        focus_idx = st.radio(
            "Which sustainability dimension matters most?",
            [0, 1, 2, 3],
            format_func=lambda x: PILLAR_OPTIONS[x],
            index=int(p.get("focus", st.session_state.get("_focus", 3))),
        )
    w_e, w_s, w_g, esg_focus_label = PILLAR_WEIGHTS[focus_idx]
    st.markdown(f'<div class="tip-strip">💡 Composite ESG formula: ESG = E×{w_e:.2f} + S×{w_s:.2f} + G×{w_g:.2f}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════
# 04 — ASSET ESG SCORES
# ══════════════════════════════════════════════════════════════════════
with st.expander("04  ·  Asset ESG Scores", expanded=False):
    st.markdown('<div class="expander-desc">Rate each asset from 0 (worst) to 100 (best) across three ESG pillars. Scores are combined using your pillar weights above.</div>', unsafe_allow_html=True)
    col_g, col_h = st.columns(2, gap="large")
    with col_g:
        st.markdown(f'<div class="sec-label">{name1}</div>', unsafe_allow_html=True)
        sector1 = st.selectbox("Sector", SECTORS, key="sec1")
        E1 = st.slider("🌍 Environmental (E) — climate, emissions, resource use", 0, 100, int(st.session_state.get("_E1", 60)), key="e1")
        S1 = st.slider("🤝 Social (S) — labour, community, human rights",         0, 100, int(st.session_state.get("_S1", 60)), key="s1")
        G1 = st.slider("🏛️ Governance (G) — board, transparency, ethics",         0, 100, int(st.session_state.get("_G1", 60)), key="g1")
    with col_h:
        st.markdown(f'<div class="sec-label">{name2}</div>', unsafe_allow_html=True)
        sector2 = st.selectbox("Sector", SECTORS, key="sec2")
        E2 = st.slider("🌍 Environmental (E) — climate, emissions, resource use", 0, 100, int(st.session_state.get("_E2", 40)), key="e2")
        S2 = st.slider("🤝 Social (S) — labour, community, human rights",         0, 100, int(st.session_state.get("_S2", 40)), key="s2")
        G2 = st.slider("🏛️ Governance (G) — board, transparency, ethics",         0, 100, int(st.session_state.get("_G2", 40)), key="g2")
    st.markdown('<div class="tip-strip">💡 <strong>Tip:</strong> Scores above 70 are generally considered strong. Below 40 indicates meaningful sustainability concerns.</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════
# 05 — ETHICAL SCREENING
# ══════════════════════════════════════════════════════════════════════
with st.expander("05  ·  Ethical Screening", expanded=False):
    st.markdown('<div class="expander-desc">ESGenie automatically detects controversial sectors. You can exclude them entirely, apply a utility penalty, or proceed without restriction. You can also set a minimum ESG floor.</div>', unsafe_allow_html=True)

    excluded = {}
    for aname, sector in [(name1, sector1), (name2, sector2)]:
        if sector in SIN_SECTORS:
            excluded[aname] = sector

    if excluded:
        st.warning(f"⚠️ Restricted sector detected: {', '.join(excluded.values())}. Please choose how to proceed.")
        sin_choice = st.radio(
            "How should ESGenie handle the restricted sector(s)?",
            [1, 2, 3],
            format_func=lambda x: {
                1: "❌ Exclude entirely — force the weight of this asset to zero",
                2: "⚠️ Apply utility penalty — reduce attractiveness without hard exclusion",
                3: "✅ Proceed without restriction — include as normal",
            }[x],
        )
    else:
        st.success("✅ No restricted sectors detected across your two assets.")
        sin_choice = 3

    st.markdown('<div class="sec-label" style="margin-top:1rem;">Minimum ESG Floor</div>', unsafe_allow_html=True)
    use_thr = st.checkbox(
        "Enforce a minimum portfolio ESG score — portfolios below this threshold will be penalised",
        value=bool(p.get("use_thr", st.session_state.get("_use_thr", False)))
    )
    if use_thr:
        threshold = st.slider("Minimum acceptable portfolio ESG score (0–100)", 0.0, 100.0,
                              float(p.get("thr", st.session_state.get("_thr", 50.0))), step=1.0)
        st.caption(f"Allocations producing a weighted ESG score below {threshold:.0f} will receive a utility penalty.")
    else:
        threshold = 0.0

    apply_threshold  = use_thr and threshold > 0
    penalty_strength = 0.01 * theta


# ══════════════════════════════════════════════════════════════════════
# RUN BUTTON
# ══════════════════════════════════════════════════════════════════════
st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)
col_run, _, _ = st.columns([1.2, 1, 1.8])
with col_run:
    run = st.button("✨ Run Optimisation", type="primary", use_container_width=True)


# ══════════════════════════════════════════════════════════════════════
# LANDING STATE
# ══════════════════════════════════════════════════════════════════════
if not run:
    st.markdown("""
    <div class="landing-box" style="margin-top:1.2rem;">
      <div style="font-family:'Cormorant Garamond',serif;font-size:1.4rem;color:#1c3a1c;margin-bottom:0.4rem;">
        Ready when you are 🌿
      </div>
      <div style="font-size:0.9rem;color:#3a6a3a;line-height:1.7;font-weight:300;">
        Complete the five sections above and click <strong>Run Optimisation</strong> to receive
        your personalised ESG portfolio recommendation — including an efficient frontier chart,
        utility analysis, and sensitivity breakdown.
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()


# ══════════════════════════════════════════════════════════════════════
# GUARDS
# ══════════════════════════════════════════════════════════════════════
if sin_choice == 1 and len(excluded) == 2:
    st.error("❌ Both assets are in restricted sectors and have been excluded. No valid portfolio can be constructed. Please adjust your ethical screening settings.")
    st.stop()


# ══════════════════════════════════════════════════════════════════════
# COMPUTE
# ══════════════════════════════════════════════════════════════════════
esg1 = compute_esg(E1, S1, G1, w_e, w_s, w_g)
esg2 = compute_esg(E2, S2, G2, w_e, w_s, w_g)

with st.spinner("🌿 ESGenie is optimising your portfolio..."):
    res = run_optimisation(
        r1, r2, sd1, sd2, rho, r_free,
        gamma, theta, esg1, esg2,
        sin_choice, excluded, name1, name2,
        apply_threshold, threshold, penalty_strength,
    )

w1_opt = res["w1_optimal"];  w2_opt = 1 - w1_opt
w1_tan = res["w1_tangency"]; w2_tan = 1 - w1_tan
w1_mv  = res["w1_min_var"];  w2_mv  = 1 - w1_mv
esg_premium = res["sr_tangency"] - res["sr_optimal"]

if theta <= 1:     esg_importance_label = "Low ESG preference"
elif theta <= 2.5: esg_importance_label = "Moderate ESG preference"
else:              esg_importance_label = "High ESG preference"

dominant = name1 if w1_opt >= w2_opt else name2
dom_esg  = esg1  if w1_opt >= w2_opt else esg2
sec_esg  = esg2  if w1_opt >= w2_opt else esg1

if theta > 3:     identity = "🌱 Impact Investor"
elif theta > 1.5: identity = "⚖️ Balanced ESG Investor"
else:             identity = "💰 Return-Focused Investor"


# ══════════════════════════════════════════════════════════════════════
# RESULTS HEADER
# ══════════════════════════════════════════════════════════════════════
st.markdown('<div class="green-rule"></div>', unsafe_allow_html=True)
st.markdown("""
<div style="font-family:'Cormorant Garamond',serif;font-size:1.9rem;font-weight:700;
            color:#1c3a1c;margin-bottom:0.2rem;">Your Portfolio Results</div>
<div style="font-size:0.85rem;color:#6a8a6a;margin-bottom:1.2rem;font-weight:300;">
  Based on your inputs, here is what ESGenie recommends. Review your profile, ESG scores,
  and detailed results across the three tabs below.
</div>
""", unsafe_allow_html=True)


# ── Investor Profile Strip ────────────────────────────────────────────
st.markdown('<div class="sec-header">👤 Your Investor Profile</div>', unsafe_allow_html=True)
c1, c2, c3, c4, c5 = st.columns(5)
for col, label, value, delta in [
    (c1, "Risk Profile",   risk_label,           f"γ = {gamma}"),
    (c2, "ESG Importance", esg_importance_label, f"θ = {theta}"),
    (c3, "ESG Focus",      esg_focus_label,      "pillar weighting"),
    (c4, "ESG Floor",      f"{threshold:.0f}" if apply_threshold else "None", "min score"),
    (c5, "Investor Type",  identity,             ""),
]:
    with col:
        st.markdown(f"""
        <div class="m-card">
          <div class="m-label">{label}</div>
          <div class="m-value" style="font-size:1rem;line-height:1.3;">{value}</div>
          <div class="m-delta">{delta}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ── ESG Score Summary ─────────────────────────────────────────────────
st.markdown('<div class="sec-header">🌱 ESG Score Summary</div>', unsafe_allow_html=True)
st.caption("Composite scores are calculated using your pillar weights. Higher is better.")

ca, cb = st.columns(2, gap="large")
for col, aname, sector, esg_score, E, S, G in [
    (ca, name1, sector1, esg1, E1, S1, G1),
    (cb, name2, sector2, esg2, E2, S2, G2),
]:
    _, pill = classify_esg(esg_score)
    with col:
        st.markdown(f"""
        <div class="asset-card">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:0.7rem;">
            <div>
              <div class="asset-name">{aname}</div>
              <div style="font-size:0.78rem;color:#7a9a7a;">{sector}</div>
            </div>
            {pill}
          </div>
          <div style="margin-bottom:0.7rem;">
            <span class="asset-esg-score">{esg_score:.1f}</span>
            <span style="font-size:0.85rem;color:#7a9a7a;"> / 100</span>
          </div>
          <div style="font-size:0.78rem;color:#5a7a5a;line-height:2;">
            🌍 Environmental &nbsp; E = {E} &nbsp;×&nbsp; {w_e:.2f} &nbsp;→&nbsp; <strong>{E*w_e:.1f}</strong><br>
            🤝 Social &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; S = {S} &nbsp;×&nbsp; {w_s:.2f} &nbsp;→&nbsp; <strong>{S*w_s:.1f}</strong><br>
            🏛️ Governance &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; G = {G} &nbsp;×&nbsp; {w_g:.2f} &nbsp;→&nbsp; <strong>{G*w_g:.1f}</strong>
          </div>
        </div>
        """, unsafe_allow_html=True)

if apply_threshold:
    if esg1 < threshold: st.warning(f"⚠️ {name1}'s ESG score ({esg1:.1f}) falls below your minimum threshold of {threshold:.0f}.")
    if esg2 < threshold: st.warning(f"⚠️ {name2}'s ESG score ({esg2:.1f}) falls below your minimum threshold of {threshold:.0f}.")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="green-rule"></div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════
# RESULT TABS
# ══════════════════════════════════════════════════════════════════════
tab1, tab2, tab3 = st.tabs(["📊  Portfolio Results", "📈  Charts", "🔬  Sensitivity Analysis"])


# ─────────────────────────────────────────────────────────────────────
# TAB 1
# ─────────────────────────────────────────────────────────────────────
with tab1:
    st.markdown('<div class="sec-header">📐 Recommended Portfolio at a Glance</div>', unsafe_allow_html=True)
    m1, m2, m3, m4, m5 = st.columns(5)
    for col, label, value, delta in [
        (m1, "Expected Return",  f"{res['ret_optimal']*100:.2f}%",  "annualised"),
        (m2, "Risk (Std Dev)",   f"{res['sd_optimal']*100:.2f}%",   "annualised"),
        (m3, "Sharpe Ratio",     f"{res['sr_optimal']:.3f}",        "risk-adjusted"),
        (m4, "ESG Score",        f"{res['esg_optimal']:.1f} / 100", classify_esg(res['esg_optimal'])[0]),
        (m5, "ESG Premium",      f"{esg_premium:+.3f}",             "vs tangency Sharpe"),
    ]:
        with col:
            st.markdown(f"""
            <div class="m-card">
              <div class="m-label">{label}</div>
              <div class="m-value">{value}</div>
              <div class="m-delta">{delta}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="sec-header">💼 Asset Allocation</div>', unsafe_allow_html=True)
    _, p1 = classify_esg(esg1)
    _, p2 = classify_esg(esg2)
    _, pp = classify_esg(res["esg_optimal"])
    st.markdown(f"""
    <table style="width:100%;border-collapse:collapse;font-size:0.9rem;
                  background:white;border-radius:12px;overflow:hidden;
                  border:1px solid #d4e8d4;box-shadow:0 1px 8px rgba(28,58,28,0.05);">
      <thead>
        <tr style="background:#edf7ef;">
          <th style="text-align:left;padding:11px 16px;color:#1c3a1c;font-family:'Jost',sans-serif;font-weight:600;font-size:0.78rem;letter-spacing:0.8px;text-transform:uppercase;">Asset</th>
          <th style="text-align:right;padding:11px 16px;color:#1c3a1c;font-family:'Jost',sans-serif;font-weight:600;font-size:0.78rem;letter-spacing:0.8px;text-transform:uppercase;">Weight</th>
          <th style="text-align:right;padding:11px 16px;color:#1c3a1c;font-family:'Jost',sans-serif;font-weight:600;font-size:0.78rem;letter-spacing:0.8px;text-transform:uppercase;">ESG Score</th>
          <th style="text-align:center;padding:11px 16px;color:#1c3a1c;font-family:'Jost',sans-serif;font-weight:600;font-size:0.78rem;letter-spacing:0.8px;text-transform:uppercase;">ESG Class</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="padding:10px 16px;color:#1c3a1c;font-weight:500;">{name1}</td>
          <td style="text-align:right;padding:10px 16px;font-weight:700;color:#1c3a1c;font-family:'Cormorant Garamond',serif;font-size:1.05rem;">{w1_opt*100:.1f}%</td>
          <td style="text-align:right;padding:10px 16px;color:#4a6a4a;">{esg1:.1f}</td>
          <td style="text-align:center;padding:10px 16px;">{p1}</td>
        </tr>
        <tr style="background:#f9fdf9;">
          <td style="padding:10px 16px;color:#1c3a1c;font-weight:500;">{name2}</td>
          <td style="text-align:right;padding:10px 16px;font-weight:700;color:#1c3a1c;font-family:'Cormorant Garamond',serif;font-size:1.05rem;">{w2_opt*100:.1f}%</td>
          <td style="text-align:right;padding:10px 16px;color:#4a6a4a;">{esg2:.1f}</td>
          <td style="text-align:center;padding:10px 16px;">{p2}</td>
        </tr>
        <tr style="border-top:2px solid #d4e8d4;background:#edf7ef;">
          <td style="padding:10px 16px;font-weight:700;color:#1c3a1c;">Portfolio (weighted)</td>
          <td style="text-align:right;padding:10px 16px;font-weight:700;color:#1c3a1c;font-family:'Cormorant Garamond',serif;font-size:1.05rem;">100.0%</td>
          <td style="text-align:right;padding:10px 16px;font-weight:700;color:#1c3a1c;">{res['esg_optimal']:.1f}</td>
          <td style="text-align:center;padding:10px 16px;">{pp}</td>
        </tr>
      </tbody>
    </table>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="sec-header">📋 Portfolio Comparison</div>', unsafe_allow_html=True)
    st.caption("How your ESG-optimal recommendation compares to two purely financial benchmarks.")
    chars_df = pd.DataFrame({
        "Metric": ["Expected Return", "Risk (Std Dev)", "Sharpe Ratio", "ESG Score", "ESG Class"],
        f"🟢 Recommended ({w1_opt*100:.0f}% {name1})": [
            f"{res['ret_optimal']*100:.2f}%", f"{res['sd_optimal']*100:.2f}%",
            f"{res['sr_optimal']:.3f}", f"{res['esg_optimal']:.1f}", classify_esg(res['esg_optimal'])[0]],
        f"📐 Tangency ({w1_tan*100:.0f}% {name1})": [
            f"{res['ret_tangency']*100:.2f}%", f"{res['sd_tangency']*100:.2f}%",
            f"{res['sr_tangency']:.3f}", f"{res['esg_tangency']:.1f}", classify_esg(res['esg_tangency'])[0]],
        f"🛡️ Min Variance ({w1_mv*100:.0f}% {name1})": [
            f"{res['ret_min_var']*100:.2f}%", f"{res['sd_min_var']*100:.2f}%",
            f"{res['sr_min_var']:.3f}", f"{res['esg_min_var']:.1f}", classify_esg(res['esg_min_var'])[0]],
    })
    st.dataframe(chars_df, use_container_width=True, hide_index=True)

    if esg_premium > 0:
        st.warning(f"📉 **ESG Premium: {esg_premium:+.3f} Sharpe points** — your ESG preferences reduce risk-adjusted return relative to the purely financial tangency portfolio.")
    else:
        st.success(f"📈 **ESG Premium: {esg_premium:+.3f} Sharpe points** — your ESG preferences align with financial performance. No return sacrifice detected.")

    st.markdown('<div class="sec-header">💬 Why This Portfolio?</div>', unsafe_allow_html=True)
    driver = (
        f"The tilt toward <strong>{dominant}</strong> is partly driven by its stronger ESG score "
        f"({dom_esg:.1f} vs {sec_esg:.1f}), consistent with your {esg_focus_label.lower()} and θ = {theta}."
        if dom_esg > sec_esg else
        f"The tilt toward <strong>{dominant}</strong> is driven primarily by its superior "
        f"risk-return profile rather than ESG performance."
    )
    st.markdown(f"""
    <div class="reco-box">
      Based on your <strong>{risk_label.lower()} risk profile</strong> (γ = {gamma}) and
      <strong>{esg_importance_label.lower()}</strong> (θ = {theta}), ESGenie recommends allocating
      <strong>{w1_opt*100:.1f}% to {name1}</strong> and
      <strong>{w2_opt*100:.1f}% to {name2}</strong>.<br><br>{driver}
    </div>
    """, unsafe_allow_html=True)

    if apply_threshold and (esg1 < threshold or esg2 < threshold):
        st.warning(f"One or more assets fell below your minimum ESG floor of {threshold:.0f}. A utility shortfall penalty was applied.")
    if sin_choice == 1 and excluded:
        for aname, sec in excluded.items():
            st.error(f"**{aname}** ({sec}) was excluded per your ethical screening preferences.")

    st.markdown("<br>", unsafe_allow_html=True)
    summary_txt = (
        f"ESGenie 🌿 — Portfolio Summary\n{'='*42}\n"
        f"Risk Profile:    {risk_label}  (γ = {gamma})\n"
        f"ESG Importance:  θ = {theta}  ({esg_importance_label})\n"
        f"ESG Focus:       {esg_focus_label}\n"
        f"Investor Type:   {identity}\n\n"
        f"Recommended Allocation\n{'-'*42}\n"
        f"  {name1}: {w1_opt*100:.1f}%\n"
        f"  {name2}: {w2_opt*100:.1f}%\n\n"
        f"Portfolio Metrics\n{'-'*42}\n"
        f"  Expected Return : {res['ret_optimal']*100:.2f}%\n"
        f"  Risk (Std Dev)  : {res['sd_optimal']*100:.2f}%\n"
        f"  Sharpe Ratio    : {res['sr_optimal']:.3f}\n"
        f"  ESG Score       : {res['esg_optimal']:.1f} / 100  ({classify_esg(res['esg_optimal'])[0]})\n"
        f"  ESG Premium     : {esg_premium:+.3f} Sharpe points vs tangency\n"
    )
    st.download_button(label="⬇️ Download Portfolio Summary (.txt)", data=summary_txt,
                       file_name="esgenie_summary.txt", mime="text/plain")


# ─────────────────────────────────────────────────────────────────────
# TAB 2 — Charts
# ─────────────────────────────────────────────────────────────────────
with tab2:
    weights_plot = res["weights"]
    ret_plot     = res["rets"]
    risk_plot    = res["risks"]
    esg_plot     = res["esgs"]
    util_plot    = res["utils"]

    st.markdown('<div class="sec-header">📈 ESG-Efficient Frontier</div>', unsafe_allow_html=True)
    st.caption("Each point represents a different portfolio split, coloured by its ESG score. The star marks your recommended portfolio.")

    fig_f = go.Figure()
    fig_f.add_trace(go.Scatter(
        x=risk_plot * 100, y=ret_plot * 100, mode="markers",
        marker=dict(color=esg_plot, colorscale="RdYlGn", cmin=0, cmax=100, size=5, opacity=0.8,
                    colorbar=dict(title=dict(text="ESG Score", font=dict(color="#1c3a1c")),
                                  thickness=14, tickfont=dict(color="#1c3a1c"))),
        text=[f"{name1}: {w*100:.1f}%  |  {name2}: {(1-w)*100:.1f}%<br>"
              f"Return: {r*100:.2f}%  |  Risk: {s*100:.2f}%  |  ESG: {e:.1f}"
              for w, r, s, e in zip(weights_plot, ret_plot, risk_plot, esg_plot)],
        hoverinfo="text", showlegend=False,
    ))
    cml_x = np.linspace(0, max(risk_plot) * 1.2, 100)
    cml_s = (res["ret_tangency"] - r_free) / res["sd_tangency"] if res["sd_tangency"] > 0 else 0
    fig_f.add_trace(go.Scatter(
        x=cml_x * 100, y=(r_free + cml_s * cml_x) * 100,
        mode="lines", line=dict(dash="dash", color="#5a9a6a", width=1.8), name="Capital Market Line",
    ))
    for sx, ry, label, colour, sym, sz, wv in [
        (0,                  r_free,             f"Risk-Free ({r_free*100:.1f}%)", "#4a7a4a", "diamond",     10, None),
        (res["sd_min_var"],  res["ret_min_var"],  "Min Variance",                  "#7b5ea7", "square",      13, w1_mv),
        (res["sd_tangency"], res["ret_tangency"], "Tangency",                      "#2979aa", "triangle-up", 15, w1_tan),
        (res["sd_optimal"],  res["ret_optimal"],  "✨ Recommended",                "#1c3a1c", "star",        22, w1_opt),
    ]:
        hover = (f"{label}<br>{name1}: {wv*100:.1f}%  |  {name2}: {(1-wv)*100:.1f}%<br>"
                 f"Return: {ry*100:.2f}%  |  Risk: {sx*100:.2f}%" if wv is not None else label)
        fig_f.add_trace(go.Scatter(
            x=[sx * 100], y=[ry * 100], mode="markers+text",
            marker=dict(symbol=sym, color=colour, size=sz, line=dict(color="white", width=1.5)),
            text=[label], textposition="top right",
            textfont=dict(color="#1c3a1c", size=9, family="Jost"),
            hovertext=[hover], hoverinfo="text", name=label,
        ))
    fig_f.update_layout(
        xaxis_title="Risk — Standard Deviation (%)", yaxis_title="Expected Return (%)",
        height=440, paper_bgcolor="#f9faf5", plot_bgcolor="#ffffff",
        font=dict(family="Jost", color="#1c3a1c"),
        margin=dict(l=55, r=20, t=20, b=55),
        legend=dict(orientation="h", yanchor="bottom", y=-0.42, xanchor="left", x=0,
                    font=dict(color="#1c3a1c", family="Jost"),
                    bgcolor="rgba(255,255,255,0.9)", bordercolor="#c8e4c8", borderwidth=1),
        xaxis=dict(gridcolor="#e8f2e4", zerolinecolor="#c8e4c8",
                   title_font=dict(color="#4a7a4a"), tickfont=dict(color="#4a7a4a")),
        yaxis=dict(gridcolor="#e8f2e4", zerolinecolor="#c8e4c8",
                   title_font=dict(color="#4a7a4a"), tickfont=dict(color="#4a7a4a")),
    )
    st.plotly_chart(fig_f, use_container_width=True)

    st.markdown('<div class="sec-header">📉 Utility Function vs Portfolio Weight</div>', unsafe_allow_html=True)
    st.caption(f"Shows how utility (combining return, risk, and ESG) changes as the weight in {name1} varies. The star marks the maximum — your recommended allocation.")

    fig_u, ax = plt.subplots(figsize=(10, 4))
    fig_u.patch.set_facecolor("#f9faf5")
    ax.set_facecolor("#ffffff")
    for sp in ax.spines.values():
        sp.set_edgecolor("#c8e4c8"); sp.set_linewidth(0.8)
    ax.plot(weights_plot * 100, util_plot, color="#3a7a4a", linewidth=2.5, label="Utility U(w)")
    ax.fill_between(weights_plot * 100, util_plot, alpha=0.07, color="#3a7a4a")
    ax.axvline(x=w1_opt * 100, color="#1c3a1c", linestyle="--", linewidth=1.5, alpha=0.75)
    ax.scatter(w1_opt * 100, res["utils"][np.argmax(res["utils"])],
               marker="*", color="#1c3a1c", s=280, zorder=5, label=f"✨ Optimal: {w1_opt*100:.1f}%")
    ax.axvline(x=w1_tan * 100, color="#5a9a6a", linestyle=":", linewidth=1.5, alpha=0.75,
               label=f"Tangency: {w1_tan*100:.1f}%")
    ax.set_xlabel(f"Weight in {name1} (%)", color="#4a7a4a", fontsize=10)
    ax.set_ylabel("Utility", color="#4a7a4a", fontsize=10)
    ax.set_title("Utility Function vs Portfolio Weight", color="#1c3a1c", fontweight="bold", fontsize=11)
    ax.tick_params(colors="#4a7a4a")
    ax.legend(fontsize=9, framealpha=0.9)
    ax.grid(True, alpha=0.3, color="#c8e4c8")
    fig_u.tight_layout()
    st.pyplot(fig_u)
    plt.close(fig_u)


# ─────────────────────────────────────────────────────────────────────
# TAB 3 — Sensitivity Analysis
# ─────────────────────────────────────────────────────────────────────
with tab3:
    st.markdown('<div class="sec-header">🔬 Sensitivity Analysis</div>', unsafe_allow_html=True)
    st.caption("Explore how your recommendation shifts as investor preferences change. Results are cached — no recomputing unless inputs change.")
    st.markdown('<div class="info-strip">ℹ️ <strong>How to read this:</strong> Higher θ puts more weight on ESG; higher γ reduces risk tolerance. The heatmap shows how portfolio ESG score responds to different combinations of both preferences.</div>', unsafe_allow_html=True)

    with st.spinner("🌿 Computing sensitivity across parameter space..."):
        (theta_range, gamma_range, theta_grid, gamma_grid,
         sa_w, sa_esg, sa_sr, sg_sr, heatmap) = cached_sensitivity(
            r1, r2, sd1, sd2, rho, r_free, gamma, theta, esg1, esg2,
            sin_choice, tuple(excluded.items()), name1, name2,
            apply_threshold, threshold, penalty_strength,
        )

    st.markdown(f'<div class="sec-header">📋 θ Sensitivity Table  (γ fixed at {gamma})</div>', unsafe_allow_html=True)
    rows = []
    for idx in np.linspace(0, len(theta_range) - 1, 9, dtype=int):
        t_val = theta_range[idx]
        rows.append({
            "θ":                  f"{t_val:.2f}" + (" ← your θ" if abs(t_val - theta) < 0.25 else ""),
            f"Weight in {name1}": f"{sa_w[idx]:.1f}%",
            "Portfolio ESG":      f"{sa_esg[idx]:.1f}",
            "ESG Class":          classify_esg(sa_esg[idx])[0],
            "Sharpe":             f"{sa_sr[idx]:.3f}",
        })
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

    fig_sa, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig_sa.patch.set_facecolor("#f9faf5")
    for row_axes in axes:
        for ax in row_axes:
            ax.set_facecolor("#ffffff")
            for sp in ax.spines.values():
                sp.set_edgecolor("#c8e4c8"); sp.set_linewidth(0.8)
            ax.tick_params(colors="#4a7a4a")
    fig_sa.suptitle("ESGenie — Sensitivity Analysis", fontsize=13, fontweight="bold", color="#1c3a1c")

    ax = axes[0, 0]
    ax.plot(theta_range, sa_w, color="#3a7a4a", linewidth=2.5)
    ax.fill_between(theta_range, sa_w, alpha=0.07, color="#3a7a4a")
    ax.axvline(x=theta, color="#1c3a1c", linestyle="--", linewidth=1.5, alpha=0.8, label=f"Your θ = {theta}")
    ax.axhline(y=sa_w[np.argmin(np.abs(theta_range - theta))], color="#c8e4c8", linestyle=":", linewidth=1)
    ax.set_xlabel("ESG Preference (θ)", color="#4a7a4a"); ax.set_ylabel(f"Weight in {name1} (%)", color="#4a7a4a")
    ax.set_title(f"Allocation vs ESG Preference  (γ = {gamma})", color="#1c3a1c", fontweight="bold")
    ax.legend(fontsize=9); ax.grid(True, alpha=0.25, color="#c8e4c8"); ax.set_xlim(0, 4)

    ax = axes[0, 1]
    ax.plot(theta_range, sa_esg, color="#5a9a6a", linewidth=2.5)
    ax.fill_between(theta_range, sa_esg, alpha=0.07, color="#5a9a6a")
    ax.axvline(x=theta, color="#1c3a1c", linestyle="--", linewidth=1.5, alpha=0.8, label=f"Your θ = {theta}")
    ax.axhspan(80, 100, alpha=0.07, color="green",  label="High ESG (≥80)")
    ax.axhspan(50,  80, alpha=0.07, color="yellow", label="Moderate (50–80)")
    ax.axhspan(0,   50, alpha=0.07, color="red",    label="Low ESG (<50)")
    ax.set_xlabel("ESG Preference (θ)", color="#4a7a4a"); ax.set_ylabel("Portfolio ESG Score", color="#4a7a4a")
    ax.set_title(f"ESG Score vs ESG Preference  (γ = {gamma})", color="#1c3a1c", fontweight="bold")
    ax.legend(fontsize=8); ax.grid(True, alpha=0.25, color="#c8e4c8"); ax.set_xlim(0, 4); ax.set_ylim(0, 100)

    ax = axes[1, 0]
    ax.plot(gamma_range, sg_sr, color="#3a7a4a", linewidth=2.5, label="Sharpe Ratio")
    ax.fill_between(gamma_range, sg_sr, alpha=0.07, color="#3a7a4a")
    ax.axvline(x=gamma, color="#1c3a1c", linestyle="--", linewidth=1.5, alpha=0.8, label=f"Your γ = {gamma}")
    ax.set_xlabel("Risk Aversion (γ)", color="#4a7a4a"); ax.set_ylabel("Portfolio Sharpe Ratio", color="#4a7a4a")
    ax.set_title(f"Sharpe Ratio vs Risk Aversion  (θ = {theta})", color="#1c3a1c", fontweight="bold")
    ax.legend(fontsize=9); ax.grid(True, alpha=0.25, color="#c8e4c8")

    ax = axes[1, 1]
    im = ax.imshow(heatmap, aspect="auto", origin="lower", cmap="RdYlGn", vmin=0, vmax=100,
                   extent=[theta_grid[0], theta_grid[-1], gamma_grid[0], gamma_grid[-1]])
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label("Portfolio ESG Score", color="#4a7a4a")
    cbar.ax.yaxis.set_tick_params(color="#4a7a4a")
    plt.setp(cbar.ax.yaxis.get_ticklabels(), color="#4a7a4a")
    ax.scatter(theta, gamma, marker="*", color="#1c3a1c", s=260, zorder=5, label="✨ Your profile")
    ax.set_xlabel("ESG Preference (θ)", color="#4a7a4a"); ax.set_ylabel("Risk Aversion (γ)", color="#4a7a4a")
    ax.set_title("ESG Score across Parameter Space", color="#1c3a1c", fontweight="bold")
    ax.legend(fontsize=9, loc="upper left")

    plt.tight_layout()
    st.pyplot(fig_sa)
    plt.close(fig_sa)


# ══════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════
st.markdown('<div class="green-rule"></div>', unsafe_allow_html=True)
st.markdown("#### ⚠️ Model Limitations & Disclaimer")
st.caption(
    "This model assumes normally distributed returns, constant correlations, and static ESG scores. "
    "In practice, ESG ratings vary across providers and market conditions are dynamic. "
    "ESGenie is a learning tool and does not constitute financial advice."
)
st.markdown("""
<div class="footer">
  ESGenie 🌿 &nbsp;·&nbsp; Sustainable Portfolio Advisor &nbsp;·&nbsp; Built with Streamlit
  &nbsp;·&nbsp; Sustainable Finance Project &nbsp;·&nbsp; 🌱 Invest with purpose
</div>
""", unsafe_allow_html=True)
