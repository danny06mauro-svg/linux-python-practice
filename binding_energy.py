import numpy as np
import plotly.graph_objects as go

# --- SEMF Math Engine ---
a_V, a_S, a_C, a_A, a_P = 15.67, 17.23, 0.75, 23.2, 12.0

def calculate_be_per_nucleon(Z, N):
    A = Z + N
    if A <= 0: return 0.0
    E_volume = a_V * A
    E_surface = a_S * (A ** (2/3))
    E_coulomb = a_C * (Z ** 2) / (A ** (1/3))
    E_asymmetry = a_A * ((N - Z) ** 2) / A
    delta = a_P / (A ** 0.5) if (Z % 2 == 0 and N % 2 == 0) else (-a_P / (A ** 0.5) if (Z % 2 != 0 and N % 2 != 0) else 0.0)
    return max(0.0, (E_volume - E_surface - E_coulomb - E_asymmetry + delta) / A)

vectorized_be = np.vectorize(calculate_be_per_nucleon)
z_range = np.arange(1, 151)
n_range = np.arange(1, 151)
Z, N = np.meshgrid(z_range, n_range)
BE_per_nucleon = vectorized_be(Z, N)
BE_per_nucleon[BE_per_nucleon == 0] = np.nan

# We scan across total mass numbers A to calculate stable Z and N pairings
A_vals = np.arange(2, 250)
Z_stable = A_vals / (2 + (a_C / (2 * a_A)) * (A_vals ** (2/3)))
N_stable = A_vals - Z_stable

# Compute the precise BE/A height for the stability line points so it sits perfectly on the surface
BE_stable = np.array([calculate_be_per_nucleon(z, n) for z, n in zip(Z_stable, N_stable)])

# Create Interactive Plotly Surface
fig = go.Figure(data=[go.Surface(
    x=n_range,
    y=z_range,
    z=BE_per_nucleon.T, # Transpose to correctly match axes alignment
    colorscale='Viridis',
    colorbar=dict(title="BE / A (MeV)")
)])

# Overlay the 3D Stability Line (rendered as a thick red path along the peak ridge)
fig.add_trace(go.Scatter3d(
    x=N_stable,
    y=Z_stable,
    z=BE_stable,
    mode='lines',
    line=dict(color='red', width=6),
    name='Line of Stability'
))

# Update Layout settings for interactive labels and titles
fig.update_layout(
    title='Interactive Nuclear Binding Energy in the N-Z Plane',
    scene = dict(
        xaxis_title='Neutrons (N)',
        yaxis_title='Protons (Z)',
        zaxis_title='BE / A (MeV)'
    ),
    width=900,
    height=700,
    margin=dict(l=65, r=50, b=65, t=90)
)

# Display in Colab
fig.write_html("binding_energy.html")
print("Saved interactive plot to binding_energy.html")
