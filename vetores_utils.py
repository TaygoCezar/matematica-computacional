# vetores_utils.py
import matplotlib.pyplot as plt
import numpy as np

def plot_vectors(vectors, colors=None, labels=None, figsize=(8, 8), title='Vetores no Plano Cartesiano'):
    """
    Parâmetros:
    vectors: lista de tuplas representando os vetores [(x1, y1), (x2, y2), ...]
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
    
    # Valores padrão se não forem fornecidos
    if colors is None:
        colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown'][:len(vectors)]
    
    if labels is None:
        labels = [f'v{i+1} = {vec}' for i, vec in enumerate(vectors)]
    
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

def plot_transformation(original_vectors, transformed_vectors, title="Transformação Linear"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    for ax, vectors, sub_title in [(ax1, original_vectors, "Antes"), (ax2, transformed_vectors, "Depois")]:
        ax.axhline(y=0, color='black', linewidth=1, alpha=0.5)
        ax.axvline(x=0, color='black', linewidth=1, alpha=0.5)
        ax.grid(True, alpha=0.2)
        
        colors = ['red', 'blue', 'green', 'orange']
        for i, (x, y) in enumerate(vectors):
            ax.quiver(0, 0, x, y, color=colors[i], scale=1, scale_units='xy', 
                     angles='xy', width=0.015, alpha=0.7)
        
        max_limit = max(max(abs(x) for x, y in vectors), max(abs(y) for x, y in vectors)) + 0.5
        ax.set_xlim(-max_limit, max_limit)
        ax.set_ylim(-max_limit, max_limit)
        ax.set_title(sub_title)
        ax.set_xlabel('Eixo X')
        ax.set_ylabel('Eixo Y')
    
    plt.suptitle(title, fontsize=16)
    plt.tight_layout()
    plt.show()


def plot_determinante(original_vectors, transformed_vectors, title="Análise do Determinante"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
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
        if len(vectors) == 2:
            v1 = np.array(vectors[0])
            v2 = np.array(vectors[1])
            
            # Pontos do paralelogramo
            parallelogram = np.array([[0, 0], v1, v1 + v2, v2])
            
            # Desenhar o paralelogramo preenchido
            from matplotlib.patches import Polygon
            poly = Polygon(parallelogram, alpha=0.3, color='gray', 
                          label=f'Área: {area:.2f}')
            ax.add_patch(poly)
        
        # Plotar os vetores
        for i, (x, y) in enumerate(vectors):
            ax.quiver(0, 0, x, y, color=colors[i], scale=1, scale_units='xy', 
                     angles='xy', width=0.015, alpha=0.7, 
                     label=f'Vetor {i+1}: ({x}, {y})')
        
        # Adicionar informações do determinante
        info_text = f"Determinante: {det:.2f}\nÁrea: {area:.2f}"
        ax.text(0.02, 0.98, info_text, transform=ax.transAxes, 
                fontsize=12, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
        
        
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        ax.set_title(sub_title)
        ax.set_xlabel('Eixo X')
        ax.set_ylabel('Eixo Y')
        ax.legend()  # Mostrar legenda com a área
    
    plt.suptitle(title, fontsize=16)
    plt.tight_layout()
    plt.show()