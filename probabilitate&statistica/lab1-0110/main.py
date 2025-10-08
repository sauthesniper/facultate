import numpy as np
import matplotlib.pyplot as plt

# Numărul de simulări
NUM_SAMPLES = 1000

# Setează stilul dark pentru grafic
plt.style.use("dark_background")

# Creează figura și axa
fig, ax = plt.subplots()

# Setează aspect ratio 1:1 pentru a păstra forma circulară
ax.set_aspect("equal", "box")

# Setează limitele axelor pentru a vedea întregul cerc
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Desenează cercul principal cu raza 1, centrat în origine
circle = plt.Circle((0, 0), 1, fill=False, color="white", linewidth=2)
ax.add_patch(circle)

# Desenează triunghiul înscris în cerc
# Calculează cele 3 vârfuri ale triunghiului echilateral
angles = np.array([90, 210, 330]) * np.pi / 180  # Convertește gradele în radiani
x = np.cos(angles)  # Coordonatele x ale vârfurilor
y = np.sin(angles)  # Coordonatele y ale vârfurilor

# Conectează vârfurile pentru a forme triunghiul
ax.plot(np.append(x, x[0]), np.append(y, y[0]), color="cyan", linewidth=2)

# Alege un vârf fix al triunghiului (primul vârf)
x1, y1 = x[0], y[0]

# Simulează corzile și numără câte sunt mai lungi decât √3
count_longer = 0
sqrt3 = np.sqrt(3)

for i in range(NUM_SAMPLES):
    # Generează un punct aleator pe cerc pentru celălalt capăt al corzii
    theta = np.random.uniform(0, 2*np.pi)
    x2, y2 = np.cos(theta), np.sin(theta)
    
    # Calculează lungimea corzii
    chord_length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Verifică dacă lungimea este mai mare decât √3
    if chord_length > sqrt3:
        count_longer += 1
        color = "green"
        alpha = 0.1
    else:
        color = "red"
        alpha = 0.05
    
    # Desenează coarda (primele câteva pentru vizualizare)
    if i < 100:  # Desenăm doar primele 100 pentru claritate vizuală
        ax.plot([x1, x2], [y1, y2], color=color, linewidth=0.5, alpha=alpha)

# Calculează probabilitatea
probability = count_longer / NUM_SAMPLES

# Adaugă punct pentru vârful fix
ax.plot(x1, y1, 'yo', markersize=8, label=f'Vârf fix')

# Adaugă text cu rezultatele
ax.text(0, -1.3, f'Simulări: {NUM_SAMPLES}', ha='center', fontsize=12)
ax.text(0, -1.45, f'Corzi > √3: {count_longer} ({probability:.2%})', ha='center', fontsize=12)
ax.text(0, -1.6, f'Probabilitate teoretică: 1/3 (33.33%)', ha='center', fontsize=10)

# Adaugă legendă
ax.legend(loc='upper right')

# Titlu
ax.set_title(f'Paradoxul lui Bertrand - Metoda 1: Vârf fix', fontsize=14)

# Salvează imaginea
plt.savefig("bertrand_simulation.png", dpi=300)

# Afișează graficul
plt.show()

print(f"\nRezultate simulare:")
print(f"Număr total de corzi: {NUM_SAMPLES}")
print(f"Corzi mai lungi decât √3: {count_longer}")
print(f"Probabilitate estimată: {probability:.4f}")
print(f"Probabilitate teoretică: {1/3:.4f}")
