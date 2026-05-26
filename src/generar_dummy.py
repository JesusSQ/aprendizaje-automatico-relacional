"""
Genera un features_dummy.csv con la misma estructura que tendrá el
features.csv real, pero con datos aleatorios. Sirve para que el
pipeline de modelos pueda desarrollarse antes de tener las métricas
reales calculadas.
"""

import numpy as np
import pandas as pd

np.random.seed(42)

N_FILAS = 50
N_WORDS = 1433
CLASES = [
    "Case_Based",
    "Genetic_Algorithms",
    "Neural_Networks",
    "Probabilistic_Methods",
    "Reinforcement_Learning",
    "Rule_Learning",
    "Theory",
]

df = pd.DataFrame({
    "node_id": np.arange(N_FILAS),
    "degree": np.random.uniform(1, 20, N_FILAS),
    "closeness": np.random.uniform(0, 0.3, N_FILAS),
    "betweenness": np.random.uniform(0, 0.05, N_FILAS),
    "pagerank": np.random.uniform(0, 0.005, N_FILAS),
    "eigenvector_centrality": np.random.uniform(0, 0.1, N_FILAS),
    "clustering_coef": np.random.uniform(0, 1, N_FILAS),
    "triangles": np.random.randint(0, 10, N_FILAS),
    "kcore": np.random.randint(1, 5, N_FILAS),
    "community_louvain": np.random.randint(0, 8, N_FILAS),
})

# Bolsa de palabras: 1433 columnas binarias
for i in range(N_WORDS):
    df[f"word_{i}"] = np.random.randint(0, 2, N_FILAS)

df["class"] = np.random.choice(CLASES, N_FILAS)

df.to_csv("data/features_dummy.csv", index=False)
print(f"Generado data/features_dummy.csv con {N_FILAS} filas y {len(df.columns)} columnas")