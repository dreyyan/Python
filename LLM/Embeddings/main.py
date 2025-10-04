import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Step 1 — Example embeddings (normally learned during training)
embeddings = {
    "cat":    [0.2, 0.1, 0.4, 0.7],
    "dog":    [0.21, 0.12, 0.39, 0.69],
    "apple":  [0.9, 0.85, 0.1, 0.2],
    "banana": [0.88, 0.82, 0.15, 0.25],
    "car":    [0.3, 0.4, 0.9, 0.8],
}

words = list(embeddings.keys())
X = np.array(list(embeddings.values()))

# Step 2 — Reduce to 2 dimensions
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# Step 3 — Plot
plt.figure(figsize=(8, 6))
for i, word in enumerate(words):
    plt.scatter(X_reduced[i, 0], X_reduced[i, 1])
    plt.text(X_reduced[i, 0]+0.01, X_reduced[i, 1]+0.01, word, fontsize=12)

plt.title("Word Embeddings Visualization (PCA)")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.grid(True)
plt.show()