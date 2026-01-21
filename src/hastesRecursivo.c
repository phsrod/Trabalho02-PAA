#include <stdio.h>
#include <limits.h>
#include <time.h>
#include <string.h>
#include <stdlib.h>

#define NUM_EXECUCOES 11
#define FRAME_BYTES_ESTIMATED 48 /* estimativa média do frame na pilha */

/* Contador de chamadas recursivas para estimar memória */
long long total_chamadas = 0;

/* Função de preço */
int preco(int i) {
    return 3 * i - (i % 4);
}

/* Corte de Hastes recursivo */
int CorteDeHastes(int n, int precos[]) {
    total_chamadas++;

    if (n == 0) {
        return 0;
    }

    int lucro = INT_MIN;

    for (int i = 1; i <= n; i++) {
        int valor = precos[i] + CorteDeHastes(n - i, precos);
        if (valor > lucro)
            lucro = valor;
    }

    return lucro;
}

void executar_teste(int tamanho, FILE *arquivo) {
    int *precos = (int*)malloc((tamanho + 1) * sizeof(int));
    double tempos[NUM_EXECUCOES];
    double tempo_total = 0.0;
    int resultado = 0;
    
    // Preencher tabela de preços
    for (int i = 1; i <= tamanho; i++) {
        precos[i] = preco(i);
    }

    printf("\nExecutando %d testes para tamanho %d (primeira sera ignorada)...\n", NUM_EXECUCOES, tamanho);
    
    // Executar 11 vezes
    for (int exec = 0; exec < NUM_EXECUCOES; exec++) {
        total_chamadas = 0; // Resetar contador
        
        struct timespec inicio, fim;
        clock_gettime(CLOCK_MONOTONIC, &inicio);
        resultado = CorteDeHastes(tamanho, precos);
        clock_gettime(CLOCK_MONOTONIC, &fim);
        
        tempos[exec] = ((fim.tv_sec - inicio.tv_sec) + (fim.tv_nsec - inicio.tv_nsec) / 1e9) * 1000.0;
        
        // Ignorar primeira execução (warm-up) no cálculo da média
        if (exec > 0) {
            tempo_total += tempos[exec];
        }
        
        printf("  Execucao %2d: %.6f milissegundos (chamadas: %lld)%s\n", 
               exec + 1, tempos[exec], total_chamadas,
               exec == 0 ? " (warm-up - ignorada)" : "");
    }
    
    double tempo_medio = tempo_total / (NUM_EXECUCOES - 1);
    unsigned long memoria_estimada = tamanho * FRAME_BYTES_ESTIMATED;

    printf("\n=== Versao Recursiva ===\n");
    printf("Tamanho da barra: %d\n", tamanho);
    printf("Lucro maximo: %d\n", resultado);
    printf("Tempo medio (%d execucoes, ignorando warm-up): %.6f milissegundos\n", NUM_EXECUCOES - 1, tempo_medio);
    printf("Total de chamadas recursivas (ultima exec): %lld\n", total_chamadas);
    printf("Memoria estimada (stack): %lu bytes\n", memoria_estimada);

    // Salvar resultados em CSV (modo append)
    fprintf(arquivo, "Recursivo,%d,%d,%.6f,%lu\n", 
            tamanho, resultado, tempo_medio, memoria_estimada);
    
    free(precos);
}

void mostrar_menu() {
    printf("\n========================================\n");
    printf("  TESTE DE CORTE DE HASTES - RECURSIVO\n");
    printf("========================================\n");
    printf("1. Definir tamanho manualmente\n");
    printf("2. Teste com tamanho 10\n");
    printf("3. Teste com tamanho 20\n");
    printf("4. Teste com tamanho 30\n");
    printf("5. Executar todos os testes (10, 20, 30)\n");
    printf("0. Sair\n");
    printf("========================================\n");
    printf("Escolha uma opcao: ");
}

int main() {
    FILE *arquivo;
    int opcao;
    int tamanho_manual;
    int primeira_escrita = 1;

    do {
        mostrar_menu();
        scanf("%d", &opcao);

        if (opcao == 0) {
            printf("\nEncerrando...\n");
            break;
        }

        // Abrir arquivo em modo apropriado
        if (primeira_escrita) {
            arquivo = fopen("results/resultados_recursivo.csv", "w");
            if (arquivo != NULL) {
                fprintf(arquivo, "algoritmo,tamanho,lucro_maximo,tempo_milissegundos,memoria_bytes\n");
            }
            primeira_escrita = 0;
        } else {
            arquivo = fopen("results/resultados_recursivo.csv", "a");
        }

        if (arquivo == NULL) {
            printf("Erro ao abrir arquivo CSV\n");
            continue;
        }

        switch (opcao) {
            case 1:
                printf("Digite o tamanho da barra: ");
                scanf("%d", &tamanho_manual);
                if (tamanho_manual > 0 && tamanho_manual <= 25) {
                    executar_teste(tamanho_manual, arquivo);
                } else {
                    printf("Tamanho invalido! Use valores entre 1 e 25 (recursivo pode ser muito lento)\n");
                }
                break;
            case 2:
                executar_teste(10, arquivo);
                break;
            case 3:
                executar_teste(20, arquivo);
                break;
            case 4:
                executar_teste(30, arquivo);
                break;
            case 5:
                printf("\n*** EXECUTANDO TODOS OS TESTES ***\n");
                printf("ATENCAO: Tamanho 30 pode demorar varios minutos!\n");
                executar_teste(10, arquivo);
                executar_teste(20, arquivo);
                executar_teste(30, arquivo);
                printf("\n*** TODOS OS TESTES CONCLUIDOS ***\n");
                break;
            default:
                printf("Opcao invalida!\n");
        }

        fclose(arquivo);
        printf("\nResultados salvos em resultados_recursivo.csv\n");

    } while (opcao != 0);

    return 0;
}