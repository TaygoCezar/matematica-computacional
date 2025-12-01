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
        labels = [f'Vetor{i+1} = ({x:.0f}, {y:.0f})' for i, (x, y) in enumerate(vectors)]
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


def plot_transformation(antes, depois, colors=None, labels=None, figsize=(12, 5), title="Transformação Linear"):
    """
    Plota vetores antes e depois de uma transformação lado a lado
    
    Parâmetros:
    antes: vetores originais (array NumPy ou lista)
    depois: vetores transformados (array NumPy ou lista)
    colors: lista de cores para cada vetor
    labels: lista de labels para cada vetor
    figsize: tamanho da figura
    title: título principal
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)
    
    # Processar vetores de entrada
    def processar_vetores(vectors):
        if isinstance(vectors, np.ndarray):
            if vectors.ndim == 2:
                return [tuple(map(float, vetor)) for vetor in vectors]
            elif vectors.ndim == 1:
                return [tuple(map(float, vectors))]
        else:
            return [tuple(map(float, vetor)) for vetor in vectors]
    
    antes_processed = processar_vetores(antes)
    depois_processed = processar_vetores(depois)
    
    # Valores padrão
    if colors is None:
        colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown'][:len(antes_processed)]
    
    if labels is None:
        labels = [f'Vetor {i+1}' for i in range(len(antes_processed))]
    
    # Configurações comuns
    max_limit = 0
    for vectors in [antes_processed, depois_processed]:
        max_x = max(abs(x) for x, y in vectors) + 0.5
        max_y = max(abs(y) for x, y in vectors) + 0.5
        max_limit = max(max_limit, max_x, max_y, 2)
    
    # Plotar ANTES
    ax1.axhline(y=0, color='black', linewidth=1, alpha=0.5)
    ax1.axvline(x=0, color='black', linewidth=1, alpha=0.5)
    ax1.grid(True, alpha=0.2)
    
    for i, (x, y) in enumerate(antes_processed):
        ax1.quiver(0, 0, x, y, color=colors[i], scale=1, scale_units='xy', 
                  angles='xy', width=0.015, label=labels[i], alpha=0.8)
    
    ax1.set_xlim(-max_limit, max_limit)
    ax1.set_ylim(-max_limit, max_limit)
    ax1.legend()
    ax1.set_title('Antes da Transformação')
    ax1.set_xlabel('Eixo X')
    ax1.set_ylabel('Eixo Y')
    
    # Plotar DEPOIS
    ax2.axhline(y=0, color='black', linewidth=1, alpha=0.5)
    ax2.axvline(x=0, color='black', linewidth=1, alpha=0.5)
    ax2.grid(True, alpha=0.2)
    
    for i, (x, y) in enumerate(depois_processed):
        ax2.quiver(0, 0, x, y, color=colors[i], scale=1, scale_units='xy', 
                  angles='xy', width=0.015, label=labels[i], alpha=0.8)
    
    ax2.set_xlim(-max_limit, max_limit)
    ax2.set_ylim(-max_limit, max_limit)
    ax2.legend()
    ax2.set_title('Depois da Transformação')
    ax2.set_xlabel('Eixo X')
    ax2.set_ylabel('Eixo Y')
    
    plt.suptitle(title, fontsize=16)
    plt.tight_layout()
    plt.show()


def plot_determinante(original_vectors, transformed_vectors, title="Análise do Determinante"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    # Converter para arrays NumPy se necessário
    original_vectors = np.array(original_vectors)
    transformed_vectors = np.array(transformed_vectors)
    
    # Calcular determinantes
    det_original = np.linalg.det(original_vectors)
    det_transformed = np.linalg.det(transformed_vectors)
    area_original = abs(det_original)
    area_transformed = abs(det_transformed)
    
    for ax, vectors, sub_title, det, area in [
        (ax1, original_vectors, "Antes", det_original, area_original),
        (ax2, transformed_vectors, "Depois", det_transformed, area_transformed)
    ]:
        ax.axhline(y=0, color='black', linewidth=1, alpha=0.5)
        ax.axvline(x=0, color='black', linewidth=1, alpha=0.5)
        ax.grid(True, alpha=0.2)
        
        colors = ['red', 'blue', 'green', 'orange']
        
        # Desenhar o paralelogramo da área (apenas para 2 vetores)
        if vectors.shape[0] == 2:  # Usar shape em vez de len
            v1 = vectors[0]  # Já é array NumPy
            v2 = vectors[1]
            
            # Pontos do paralelogramo
            parallelogram = np.array([[0, 0], v1, v1 + v2, v2])
            
            # Desenhar o paralelogramo preenchido
            from matplotlib.patches import Polygon
            poly = Polygon(parallelogram, alpha=0.3, color='gray', 
                          label=f'Área: {area:.2f}')
            ax.add_patch(poly)
        
        # Plotar os vetores
        for i in range(vectors.shape[0]):  # Iterar pelas linhas do array
            x, y = vectors[i]
            ax.quiver(0, 0, x, y, color=colors[i], scale=1, scale_units='xy', 
                     angles='xy', width=0.015, alpha=0.7, 
                     label=f'Vetor {i+1}: ({x:.2f}, {y:.2f})')
        
        # Adicionar informações do determinante
        info_text = f"Determinante: {det:.2f}\nÁrea: {area:.2f}"
        ax.text(0.02, 0.98, info_text, transform=ax.transAxes, 
                fontsize=12, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
        
        # Ajustar limites automaticamente
        max_limit = max(np.max(np.abs(vectors)), 2) + 0.5
        ax.set_xlim(-max_limit, max_limit)
        ax.set_ylim(-max_limit, max_limit)
        ax.set_title(sub_title)
        ax.set_xlabel('Eixo X')
        ax.set_ylabel('Eixo Y')
        ax.legend()
    
    plt.suptitle(title, fontsize=16)
    plt.tight_layout()
    plt.show()