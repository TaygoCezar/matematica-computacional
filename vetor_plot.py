# vetores_utils.py
import matplotlib.pyplot as plt
import numpy as np

def plot_vectors(vectors, colors=None, labels=None, figsize=(8, 8), title='Vetores no Plano Cartesiano'):
    """
    Plota vetores no plano cartesiano
    
    Parâmetros:
    vectors: lista de tuplas, lista de listas OU array NumPy 2D
    colors: lista de cores para cada vetor (opcional)
    labels: lista de labels para cada vetor (opcional)
    figsize: tamanho da figura (opcional)
    title: título do gráfico (opcional)
    """
    plt.figure(figsize=figsize)
    
    # Plano cartesiano
    plt.axhline(y=0, color='black', linewidth=1, alpha=0.5)
    plt.axvline(x=0, color='black', linewidth=1, alpha=0.5)
    
    # Grade
    plt.grid(True, alpha=0.2)
    
    # Converter para formato padrão se for array NumPy e converter para Python native types
    if isinstance(vectors, np.ndarray):
        if vectors.ndim == 2:
            vectors = [tuple(map(float, vetor)) for vetor in vectors]  # Converter para float
        elif vectors.ndim == 1:
            vectors = [tuple(map(float, vectors))]
    
    # Valores padrão se não forem fornecidos
    if colors is None:
        colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown'][:len(vectors)]
    elif isinstance(colors, str):
        # Se for uma string única, usar a mesma cor para todos
        colors = [colors] * len(vectors)
    
    if labels is None:
        # Usar valores convertidos para float nos labels
        labels = [f'v{i+1} = ({x:.1f}, {y:.1f})' for i, (x, y) in enumerate(vectors)]
    elif isinstance(labels, str):
        # Se for uma string única, usar como prefixo
        labels = [f'{labels} {i+1}' for i in range(len(vectors))]
    
    # Plotar cada vetor
    for i, (x, y) in enumerate(vectors):
        plt.quiver(0, 0, x, y, color=colors[i], scale=1, scale_units='xy', 
                  angles='xy', width=0.015, label=labels[i])
    
    # Ajustar limites automaticamente baseado nos vetores
    max_x = max(abs(x) for x, y in vectors) + 0.5
    max_y = max(abs(y) for x, y in vectors) + 0.5
    max_limit = max(max_x, max_y, 2)  # Mínimo de 2
    
    plt.xlim(-max_limit, max_limit)
    plt.ylim(-max_limit, max_limit)
    plt.legend(fontsize=12)
    plt.title(title, fontsize=14)
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    
    plt.show()