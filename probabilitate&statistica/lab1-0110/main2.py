import numpy as np
import matplotlib.pyplot as plt
SAMPLES=10000
plt.style.use('dark_background')

ax=plt.gca()
ax.set_aspect('equal', 'box')
ax.set_xlim((-1,1))
ax.set_ylim((-1,1))
def draw_circle_and_triangle(ax):
    # cerc de rază 1
    circle = plt.Circle((0, 0), 1, fill=False, linewidth=2)
    ax.add_patch(circle)

    # triunghi echilateral înscris
    angles = np.deg2rad([90, 210, 330, 90])  # închidem poligonul revenind la primul vârf
    x = np.cos(angles)
    y = np.sin(angles)
    ax.plot(x, y, linewidth=2)

draw_circle_and_triangle(ax)

rng = np.random.default_rng(42)
idx_vertex = rng.integers(0, 3)   # pune 0/1/2 ca să fixezi un vârf anume
A = V[idx_vertex]
ax.plot(A[0], A[1], 'o', ms=8)    # marchează vârful ales

thetas = rng.uniform(0, 2*np.pi, size=SAMPLES)
B = np.column_stack((np.cos(thetas), np.sin(thetas)))

L = np.linalg.norm(B - A, axis=1)
# 5) Verifică dacă L > sqrt(3) și estimează probabilitatea
long_mask = L > np.sqrt(3)
p_hat = long_mask.mean()
print(f"Estimare P(L > sqrt(3)) ≈ {p_hat:.3f}  (teoretic 1/3 ≈ {1/3:.3f})")

# 6) Desenează doar câteva coarde (verde = lungă, roșu = scurtă)
subset = rng.choice(SAMPLES, size=min(SHOW, SAMPLES), replace=False)
for i in subset:
    ax.plot([A[0], B[i,0]], [A[1], B[i,1]],
            linewidth=1, alpha=0.6,
            color=('lime' if long_mask[i] else 'crimson'))

ax.set_title("Coarde dintr-un vârf al triunghiului – simulare")
plt.show()
