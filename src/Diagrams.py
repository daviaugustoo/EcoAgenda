import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
import numpy as np
from matplotlib.lines import Line2D

# Diagrama de Casos de Uso
def create_use_case_diagram():
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Desenhar sistema (retângulo)
    rect = patches.Rectangle((3, 1), 4, 6, linewidth=1, edgecolor='black', facecolor='none')
    ax.add_patch(rect)
    ax.text(5, 6.8, 'EcoAgenda', ha='center', fontsize=12)
    
    # Desenhar atores
    ax.text(1, 6, 'Usuário\nComum', ha='center', fontsize=10)
    ax.text(1, 4, 'Organizador', ha='center', fontsize=10)
    ax.text(1, 2, 'Administrador', ha='center', fontsize=10)
    
    # Desenhar casos de uso (elipses)
    ellipse1 = patches.Ellipse((5, 5.5), 2.5, 0.8, linewidth=1, edgecolor='black', facecolor='none')
    ax.add_patch(ellipse1)
    ax.text(5, 5.5, 'Buscar Evento', ha='center', fontsize=10)
    
    ellipse2 = patches.Ellipse((5, 4.5), 2.5, 0.8, linewidth=1, edgecolor='black', facecolor='none')
    ax.add_patch(ellipse2)
    ax.text(5, 4.5, 'Inscrever-se em Evento', ha='center', fontsize=10)
    
    ellipse3 = patches.Ellipse((5, 3.5), 2.5, 0.8, linewidth=1, edgecolor='black', facecolor='none')
    ax.add_patch(ellipse3)
    ax.text(5, 3.5, 'Cadastrar Evento', ha='center', fontsize=10)
    
    ellipse4 = patches.Ellipse((5, 2.5), 2.5, 0.8, linewidth=1, edgecolor='black', facecolor='none')
    ax.add_patch(ellipse4)
    ax.text(5, 2.5, 'Visualizar Inscrições', ha='center', fontsize=10)
    
    ellipse5 = patches.Ellipse((5, 1.5), 2.5, 0.8, linewidth=1, edgecolor='black', facecolor='none')
    ax.add_patch(ellipse5)
    ax.text(5, 1.5, 'Aprovar Evento', ha='center', fontsize=10)
    
    # Desenhar linhas de associação
    ax.plot([1.5, 3.8], [6, 5.5], 'k-')  # Usuário - Buscar
    ax.plot([1.5, 3.8], [6, 4.5], 'k-')  # Usuário - Inscrever
    
    ax.plot([1.5, 3.8], [4, 3.5], 'k-')  # Organizador - Cadastrar
    ax.plot([1.5, 3.8], [4, 2.5], 'k-')  # Organizador - Visualizar
    
    ax.plot([1.5, 3.8], [2, 1.5], 'k-')  # Admin - Aprovar
    
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Diagrama de Casos de Uso - EcoAgenda')
    
    return fig

# Diagrama de Sequência
def create_sequence_diagram():
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Definir atores e objetos
    actors = ['Usuário', 'Frontend', 'Backend', 'Banco de Dados']
    x_positions = [1, 3, 5, 7]
    
    # Desenhar atores e linhas de vida
    for i, actor in enumerate(actors):
        ax.text(x_positions[i], 7.5, actor, ha='center', fontsize=10)
        ax.plot([x_positions[i], x_positions[i]], [7.3, 1], 'k--')
    
    # Desenhar mensagens
    arrows = [
        (x_positions[0], 7.0, x_positions[1], 7.0, 'Seleciona evento'),
        (x_positions[1], 6.5, x_positions[2], 6.5, 'Solicita inscrição'),
        (x_positions[2], 6.0, x_positions[3], 6.0, 'Verifica disponibilidade'),
        (x_positions[3], 5.5, x_positions[2], 5.5, 'Status do evento'),
        (x_positions[2], 5.0, x_positions[3], 5.0, 'Registra inscrição'),
        (x_positions[3], 4.5, x_positions[2], 4.5, 'Confirmação'),
        (x_positions[2], 4.0, x_positions[1], 4.0, 'Confirma inscrição'),
        (x_positions[1], 3.5, x_positions[0], 3.5, 'Exibe confirmação')
    ]
    
    for x1, y1, x2, y2, text in arrows:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='->', lw=1.5))
        ax.text((x1+x2)/2, y1+0.1, text, ha='center', fontsize=8)
    
    ax.set_xlim(0, 8)
    ax.set_ylim(1, 8)
    ax.axis('off')
    ax.set_title('Diagrama de Sequência - Inscrever-se em Evento')
    
    return fig

# Diagrama de Classes
def create_class_diagram():
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Desenhar classes
    classes = [
        (2, 5, 'Usuario', ['id: int', 'nome: string', 'email: string', 'senha: string', 'tipo: string']),
        (6, 5, 'Evento', ['id: int', 'nome: string', 'data: date', 'local: string', 'categoria: string', 'status: string', 'organizador_id: int']),
        (4, 2, 'Inscricao', ['id: int', 'usuario_id: int', 'evento_id: int', 'data_inscricao: date'])
    ]
    
    for x, y, name, attributes in classes:
        height = 0.5 + 0.3 * len(attributes)
        rect = patches.Rectangle((x-1.5, y-height/2), 3, height, linewidth=1, edgecolor='black', facecolor='none')
        ax.add_patch(rect)
        
        # Linha horizontal para separar nome e atributos
        ax.plot([x-1.5, x+1.5], [y-height/2+0.5, y-height/2+0.5], 'k-')
        
        ax.text(x, y-height/2+0.25, name, ha='center', fontsize=10, fontweight='bold')
        
        for i, attr in enumerate(attributes):
            ax.text(x-1.4, y-height/2+0.7+i*0.3, attr, fontsize=8)
    
    # Desenhar relações
    ax.plot([2.5, 4], [4.5, 2.5], 'k-')  # Usuario - Inscricao
    ax.text(3, 3.7, '1', fontsize=8)
    ax.text(3.7, 2.7, '0..*', fontsize=8)
    ax.text(3.2, 3.3, 'realiza >', fontsize=8, rotation=-45)
    
    ax.plot([5.5, 4], [4.5, 2.5], 'k-')  # Evento - Inscricao
    ax.text(5, 3.7, '1', fontsize=8)
    ax.text(4.3, 2.7, '0..*', fontsize=8)
    ax.text(4.8, 3.3, 'recebe >', fontsize=8, rotation=45)
    
    ax.plot([2.5, 5.5], [5, 5], 'k-')  # Usuario - Evento
    ax.text(2.7, 5.1, '1', fontsize=8)
    ax.text(5.3, 5.1, '0..*', fontsize=8)
    ax.text(4, 5.2, 'organiza >', fontsize=8)
    
    ax.set_xlim(0, 8)
    ax.set_ylim(1, 7)
    ax.axis('off')
    ax.set_title('Diagrama de Classes - EcoAgenda')
    
    return fig

# Diagrama de Estados
def create_state_diagram():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Desenhar estados
    states = [
        (2, 4, 'Pendente'),
        (5, 4, 'Aprovado'),
        (8, 4, 'Realizado'),
        (5, 2, 'Cancelado')
    ]
    
    for x, y, name in states:
        ellipse = patches.Ellipse((x, y), 2, 1, linewidth=1, edgecolor='black', facecolor='none')
        ax.add_patch(ellipse)
        ax.text(x, y, name, ha='center', fontsize=10)
    
    # Ponto inicial
    ax.scatter(0.5, 4, s=100, color='black')
    
    # Desenhar transições
    ax.annotate('', xy=(1, 4), xytext=(0.5, 4),
               arrowprops=dict(arrowstyle='->', lw=1.5))
    
    ax.annotate('', xy=(4, 4), xytext=(3, 4),
               arrowprops=dict(arrowstyle='->', lw=1.5))
    ax.text(3.5, 4.2, 'aprovado', fontsize=8)
    
    ax.annotate('', xy=(7, 4), xytext=(6, 4),
               arrowprops=dict(arrowstyle='->', lw=1.5))
    ax.text(6.5, 4.2, 'realizado', fontsize=8)
    
    ax.annotate('', xy=(5, 2.5), xytext=(2.5, 3.5),
               arrowprops=dict(arrowstyle='->', lw=1.5))
    ax.text(3.5, 3.2, 'cancelado', fontsize=8)
    
    ax.annotate('', xy=(5, 2.5), xytext=(5, 3.5),
               arrowprops=dict(arrowstyle='->', lw=1.5))
    ax.text(5.2, 3, 'cancelado', fontsize=8)
    
    ax.set_xlim(0, 9)
    ax.set_ylim(1, 5)
    ax.axis('off')
    ax.set_title('Diagrama de Estados - Evento')
    
    return fig

# Diagrama de Arquitetura
def create_architecture_diagram():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Desenhar componentes
    components = [
        (2, 4, 'Web'),
        (2, 2, 'Mobile'),
        (5, 3, 'API REST'),
        (8, 3, 'Banco de Dados')
    ]
    
    for x, y, name in components:
        if name == 'Banco de Dados':
            # Desenhar cilindro para banco de dados
            cylinder_body = patches.Rectangle((x-1, y-0.5), 2, 1, linewidth=1, edgecolor='black', facecolor='none')
            cylinder_top = patches.Ellipse((x, y+0.5), 2, 0.5, linewidth=1, edgecolor='black', facecolor='none')
            cylinder_bottom = patches.Ellipse((x, y-0.5), 2, 0.5, linewidth=1, edgecolor='black', facecolor='none')
            ax.add_patch(cylinder_body)
            ax.add_patch(cylinder_top)
            ax.add_patch(cylinder_bottom)
        else:
            rect = patches.Rectangle((x-1, y-0.5), 2, 1, linewidth=1, edgecolor='black', facecolor='none')
            ax.add_patch(rect)
        
        ax.text(x, y, name, ha='center', fontsize=10)
    
    # Desenhar conexões
    ax.annotate('', xy=(4, 3.5), xytext=(3, 4),
               arrowprops=dict(arrowstyle='->', lw=1.5))
    
    ax.annotate('', xy=(4, 2.5), xytext=(3, 2),
               arrowprops=dict(arrowstyle='->', lw=1.5))
    
    ax.annotate('', xy=(7, 3), xytext=(6, 3),
               arrowprops=dict(arrowstyle='->', lw=1.5))
    
    ax.set_xlim(0, 10)
    ax.set_ylim(1, 5)
    ax.axis('off')
    ax.set_title('Diagrama de Arquitetura - EcoAgenda')
    
    return fig

# Criar e salvar todos os diagramas
diagrams = [
    (create_use_case_diagram, "diagrama_casos_uso.png"),
    (create_sequence_diagram, "diagrama_sequencia.png"),
    (create_class_diagram, "diagrama_classes.png"),
    (create_state_diagram, "diagrama_estados.png"),
    (create_architecture_diagram, "diagrama_arquitetura.png")
]

for create_func, filename in diagrams:
    fig = create_func()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f"Diagrama salvo como {filename}")

# Mostrar um dos diagramas como exemplo
create_class_diagram()
plt.show()