import CoolProp.CoolProp as CP

# ==============================================================================
# 1. DONNÉES D'ENTRÉE
# ==============================================================================
fluide = 'Acetone'
m_dot_1 = 0.0105556          # kg/s (Débit du flux 1)
T_1 = 283.15                 # K (Température d'entrée)
ratio_flux_3 = 0.6
m_dot_3 = m_dot_1 * ratio_flux_3  # kg/s (Débit du flux 3)

# Pression de référence pour le calcul initial (celle de DWSIM)
P_ref = 101325               # Pa

# ==============================================================================
# 2. CALCUL ET AFFICHAGE DES RÉSULTATS INITIAUX (HT-1)
# ==============================================================================
print("="*65)
print("RÉSULTATS INITIAUX DE L'ÉCHANGEUR HT-1 (P = 101325 Pa)")
print("="*65)

# Objectif : vapeur saturée (Q = 1)
Q_target = 1

# Température d'ébullition à la pression de référence
T_eb = CP.PropsSI('T', 'P', P_ref, 'Q', Q_target, fluide)

# Enthalpies massiques (J/kg)
h3 = CP.PropsSI('H', 'T', T_1, 'P', P_ref, fluide)   # Entrée liquide
h5 = CP.PropsSI('H', 'P', P_ref, 'Q', Q_target, fluide)  # Sortie vapeur saturée

# Énergie nécessaire (W)
Q_dot = m_dot_3 * (h5 - h3)

# Affichage
print(f"Température d'ébullition : {T_eb:.2f} K")
print(f"Enthalpie du flux 3 (entrée) : {h3/1000:.2f} kJ/kg")
print(f"Enthalpie du flux 5 (sortie) : {h5/1000:.2f} kJ/kg")
print(f"Énergie nécessaire (Q_dot) : {Q_dot/1000:.4f} kW")
print("="*65)

# ==============================================================================
# 3. ANALYSE DE SENSIBILITÉ (Pression vs Température d'ébullition)
# ==============================================================================
# Liste des pressions à tester (extraites de votre capture DWSIM)
pressions_a_tester = [
    10132.5, 25597.9, 41063.3, 56528.7, 71994.1,
    87459.5, 102925, 118390, 133856, 149321,
    164786, 180252, 195717
]

print("\n" + "="*65)
print("ANALYSE DE SENSIBILITÉ : Effet de la Pression sur la Température")
print("="*65)
print(f"{'Pression (Pa)':<15} | {'Temp. Ébullition (K)':<22}")
print("-" * 65)

for P in pressions_a_tester:
    # La pression du flux 3 est la même que celle du flux 1
    P_3 = P
    
    # Température d'ébullition (vapeur saturée, Q=1)
    T_5 = CP.PropsSI('T', 'P', P_3, 'Q', 1, fluide)
    
    # Affichage uniquement pression et température en Kelvin
    print(f"{P:<15.1f} | {T_5:<22.3f}")

print("="*65)
print("Analyse terminée.")