# Datos del proyecto

## Dataset: Cora

Red de citas entre artículos científicos sobre Machine Learning.

- **2708 nodos** (artículos)
- **5429 aristas dirigidas** (citas)
- **7 clases** (subáreas de ML: Case_Based, Genetic_Algorithms,
  Neural_Networks, Probabilistic_Methods, Reinforcement_Learning,
  Rule_Learning, Theory)
- **1433 features nativas binarias** (bag-of-words del resumen)
- Fuente: https://linqs.org/datasets/#cora

## features.csv

Una fila por nodo. Codificación UTF-8, separador coma.

| Columna                | Tipo      | Descripción                                |
|------------------------|-----------|--------------------------------------------|
| node_id                | int       | Identificador único del nodo               |
| degree                 | float     | Grado del nodo (in + out)                  |
| closeness              | float     | Closeness centrality                       |
| betweenness            | float     | Betweenness centrality                     |
| pagerank               | float     | PageRank                                   |
| eigenvector_centrality | float     | Eigenvector centrality                     |
| clustering_coef        | float     | Coeficiente de clustering local            |
| triangles              | int       | Número de triángulos en los que participa  |
| kcore                  | int       | k-core al que pertenece                    |
| community_louvain      | int       | ID de la comunidad (Louvain)               |
| word_0 ... word_1432   | int (0/1) | Bag-of-words original de Cora              |
| class                  | string    | Subárea de ML (etiqueta a predecir)        |

Sin valores ausentes en ninguna columna.

## features_dummy.csv

Versión de juguete del archivo anterior (10 filas, valores aleatorios)
para que el pipeline de modelos pueda desarrollarse en paralelo antes
de tener las métricas reales. Mismas columnas y tipos que features.csv.

## graph.pkl

Grafo de NetworkX serializado con pickle. Contiene únicamente la
componente conexa gigante (los nodos aislados se descartan).

Carga:

```python
import pickle
with open('data/graph.pkl', 'rb') as f:
    G = pickle.load(f)
```

## División del trabajo

- **Persona A (Jesús)**: carga del dataset, cálculo de métricas
  relacionales y nativas, análisis exploratorio. Genera `features.csv`
  y `graph.pkl`.
- **Persona B (Samuel)**: pipeline de Scikit-Learn, entrenamiento y
  evaluación de los modelos, selección del modelo final.