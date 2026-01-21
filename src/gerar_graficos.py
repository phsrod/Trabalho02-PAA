import os
import pandas as pd
import matplotlib.pyplot as plt

def ler_resultados():
    """Lê os arquivos CSV gerados pelos programas C"""
    # Usar o diretório results (pasta pai de src)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    results_dir = os.path.join(os.path.dirname(script_dir), 'results')
    
    dinamico = pd.read_csv(os.path.join(results_dir, 'resultados_dinamico.csv'))
    recursivo = pd.read_csv(os.path.join(results_dir, 'resultados_recursivo.csv'))

    # Combinar os dataframes (podem ter várias execuções com tamanhos diferentes)
    resultados = pd.concat([dinamico, recursivo], ignore_index=True)
    return resultados, results_dir

def grafico_tempo_linhas(df, results_dir):
    """Gráfico de linhas separado: tempo por tamanho."""
    
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, ax = plt.subplots(figsize=(10, 6))

    cores = {'Recursivo': '#FF6B6B', 'Dinamico': '#4ECDC4'}
    
    for algoritmo in ['Recursivo', 'Dinamico']:
        dados = df[df['algoritmo'] == algoritmo].sort_values('tamanho')
        ax.plot(dados['tamanho'], dados['tempo_segundos'], marker='o', 
                linewidth=2.5, label=algoritmo, color=cores[algoritmo], markersize=8)
        
        # Adicionar valores nos pontos com offset para evitar sobreposição
        for idx, row in dados.iterrows():
            offset_y = 10 if algoritmo == 'Recursivo' else -15
            ax.annotate(f"{row['tempo_segundos']:.6f}s", 
                       (row['tamanho'], row['tempo_segundos']), 
                       textcoords="offset points", 
                       xytext=(0, offset_y), 
                       ha='center', fontsize=9, fontweight='bold')
    
    ax.set_title('Tempo de Execução vs Tamanho da Barra', fontweight='bold', fontsize=14)
    ax.set_xlabel('Tamanho da barra', fontweight='bold', fontsize=12)
    ax.set_ylabel('Tempo (segundos)', fontweight='bold', fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=11)

    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, 'tempo_execucao_comparacao.png'), dpi=300, bbox_inches='tight')
    print("Gráfico salvo como 'tempo_execucao_comparacao.png'")
    plt.close(fig)


def grafico_memoria_linhas(df):
    """Gráfico de linhas separado: memória por tamanho."""
    
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, ax = plt.subplots(figsize=(10, 6))

    cores = {'Recursivo': '#FF6B6B', 'Dinamico': '#4ECDC4'}
    
    for algoritmo in ['Recursivo', 'Dinamico']:
        dados = df[df['algoritmo'] == algoritmo].sort_values('tamanho')
        ax.plot(dados['tamanho'], dados['memoria_bytes'], marker='s', 
                linewidth=2.5, label=algoritmo, color=cores[algoritmo], markersize=8)
        
        # Adicionar valores nos pontos com offset para evitar sobreposição
        for idx, row in dados.iterrows():
            offset_y = 20 if algoritmo == 'Recursivo' else -25
            ax.annotate(f"{int(row['memoria_bytes'])} bytes", 
                       (row['tamanho'], row['memoria_bytes']), 
                       textcoords="offset points", 
                       xytext=(0, offset_y), 
                       ha='center', fontsize=9, fontweight='bold')
    
    ax.set_title('Uso de Memória vs Tamanho da Barra', fontweight='bold', fontsize=14)
    ax.set_xlabel('Tamanho da barra', fontweight='bold', fontsize=12)
    ax.set_ylabel('Memória (bytes)', fontweight='bold', fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=11)

    plt.tight_layout()
    plt.savefig('memoria_uso_comparacao.png', dpi=300, bbox_inches='tight')
    print("Gráfico salvo como 'memoria_uso_comparacao.png'")
    plt.close(fig)


def grafico_linhas(df, coluna_y, titulo, ylabel, nome_arquivo, results_dir):
    """Gráfico de linhas: métrica vs tamanho da entrada, comparando algoritmos."""

    plt.style.use('seaborn-v0_8-darkgrid')
    fig, ax = plt.subplots(figsize=(10, 6))

    cores = {'Recursivo': '#FF6B6B', 'Dinamico': '#4ECDC4'}
    
    for algoritmo, dados in df.groupby('algoritmo'):
        dados_ordenados = dados.sort_values('tamanho')
        cor = cores.get(algoritmo, None)
        ax.plot(dados_ordenados['tamanho'], dados_ordenados[coluna_y], 
                marker='o', linewidth=2.5, label=algoritmo, color=cor, markersize=8)

    ax.set_title(titulo, fontweight='bold', fontsize=14)
    ax.set_xlabel('Tamanho da entrada (barra)', fontweight='bold', fontsize=12)
    ax.set_ylabel(ylabel, fontweight='bold', fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=11)

    # Adicionar anotações com offset alternado para evitar sobreposição
    offset_map = {'Recursivo': 12, 'Dinamico': -18}
    for algoritmo, dados in df.groupby('algoritmo'):
        offset_y = offset_map.get(algoritmo, 8)
        for _, row in dados.iterrows():
            # Formatação diferente para tempo (6 decimais) vs memória (inteiro)
            if coluna_y == 'tempo_segundos':
                valor_str = f"{row[coluna_y]:.6f}s"
            else:
                valor_str = f"{int(row[coluna_y])}"
            
            ax.annotate(valor_str, 
                       (row['tamanho'], row[coluna_y]), 
                       textcoords="offset points", 
                       xytext=(0, offset_y), 
                       ha='center', fontsize=9, fontweight='bold')

    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, nome_arquivo), dpi=300, bbox_inches='tight')
    print(f"Gráfico salvo como '{nome_arquivo}'")
    plt.close(fig)


def grafico_speedup(df, results_dir):
    """Gráfico de speedup (Recursivo / Dinâmico) por tamanho."""

    if set(df['algoritmo']) != {'Recursivo', 'Dinamico'}:
        return

    pivot = df.pivot_table(index='tamanho', columns='algoritmo', values='tempo_segundos')
    pivot = pivot.dropna()
    if pivot.empty:
        return

    pivot['speedup'] = pivot['Recursivo'] / pivot['Dinamico']

    plt.style.use('seaborn-v0_8-darkgrid')
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(pivot.index, pivot['speedup'], marker='s', color='#FF6B6B', linewidth=2)
    ax.axhline(1.0, color='gray', linestyle='--', linewidth=1)
    ax.set_title('Speedup (Recursivo / Dinâmico)', fontweight='bold', fontsize=14)
    ax.set_xlabel('Tamanho da entrada (barra)', fontweight='bold')
    ax.set_ylabel('Speedup', fontweight='bold')
    ax.grid(True, alpha=0.3)

    for x, y in zip(pivot.index, pivot['speedup']):
        ax.annotate(f"{y:.2f}x", (x, y), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=9)

    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, 'speedup_recursivo_sobre_dinamico.png'), dpi=300, bbox_inches='tight')
    print("Gráfico salvo como 'speedup_recursivo_sobre_dinamico.png'")
    plt.close(fig)

def exibir_tabela_comparativa(df):
    """Exibe uma tabela comparativa dos resultados"""
    print("\n" + "="*80)
    print("TABELA COMPARATIVA DOS ALGORITMOS")
    print("="*80)
    print(df.to_string(index=False))
    print("="*80)
    
    # Calcular diferenças
    if len(df) == 2:
        tempo_recursivo = df[df['algoritmo'] == 'Recursivo']['tempo_segundos'].values[0]
        tempo_dinamico = df[df['algoritmo'] == 'Dinamico']['tempo_segundos'].values[0]
        
        if tempo_dinamico > 0:
            speedup = tempo_recursivo / tempo_dinamico
            print(f"\nSpeedup (Recursivo/Dinâmico): {speedup:.2f}x")
            if speedup > 1:
                print(f"A versão dinâmica é {speedup:.2f}x mais rápida!")
            else:
                print(f"A versão recursiva é {1/speedup:.2f}x mais rápida!")
        print("="*80 + "\n")

def main():
    """Função principal"""
    print("Gerando gráficos comparativos...")
    
    # Usar o diretório results (pasta pai de src)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    results_dir = os.path.join(os.path.dirname(script_dir), 'results')
    
    # Verificar se os arquivos CSV existem
    csv_dinamico = os.path.join(results_dir, 'resultados_dinamico.csv')
    csv_recursivo = os.path.join(results_dir, 'resultados_recursivo.csv')
    
    if not os.path.exists(csv_dinamico):
        print("ERRO: arquivo 'resultados_dinamico.csv' não encontrado!")
        print(f"Procurado em: {csv_dinamico}")
        print("Execute o programa hastes_dinamico.exe primeiro.")
        return
    
    if not os.path.exists(csv_recursivo):
        print("ERRO: arquivo 'resultados_recursivo.csv' não encontrado!")
        print(f"Procurado em: {csv_recursivo}")
        print("Execute o programa hastes_recursivo.exe primeiro.")
        return
    
    # Ler e processar os resultados
    df, results_dir = ler_resultados()
    
    # Exibir tabela comparativa
    exibir_tabela_comparativa(df)
    
    # Gráficos de linhas separados para tempo e memória
    grafico_tempo_linhas(df, results_dir)
    grafico_linhas(df, 'memoria_bytes', 'Memória vs Tamanho da Barra', 'Memória (bytes)', 'memoria_vs_tamanho.png', results_dir)

    # Speedup (Recursivo / Dinâmico) por tamanho
    grafico_speedup(df, results_dir)

if __name__ == "__main__":
    main()