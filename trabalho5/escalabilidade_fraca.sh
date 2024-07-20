#!/bin/bash

# Define o diretório onde a biblioteca icx está localizada
LIB_PATH="/opt/intel/oneapi/2024.2/lib/"

# Atualiza LD_LIBRARY_PATH
export LD_LIBRARY_PATH="$LIB_PATH:$LD_LIBRARY_PATH"

# Verifica se a variável de ambiente está configurada corretamente
echo "LD_LIBRARY_PATH: $LD_LIBRARY_PATH"

# Executa o programa com diferentes tamanhos da matriz e número de threads
weak_scaling() {
    local -n size_list=$1
    local -n threads_list=$2
    local results=()

    for i in "${!threads_list[@]}"; do
        local threads=${threads_list[i]}
        local size=${size_list[i]}
        echo "Executando com $threads threads e tamanho da matriz $size"
        
        # Executa o programa com a variável de ambiente OMP_NUM_THREADS
        export OMP_NUM_THREADS=$threads
        output=$(./jacobi_paralelizado -n "$size" 2>&1)
        echo "$output"
        
        # Extrai o tempo total de execução
        total_runtime=$(echo "$output" | grep "Total runtime" | awk '{print $(NF-1)}')
        if [ -n "$total_runtime" ]; then
            results+=("$threads $size $total_runtime")
        fi
    done

    # Imprime e salva os resultados em um arquivo txt
    for result in "${results[@]}"; do
        echo "$result" >> resultados_escalabilidade_fraca.txt
    done
}

# Parâmetros de entrada
THREADS_LIST=(1 2 4 6 8 10 12)
SIZE_LIST=(1500 2000 2500 3000 3500 4000 4500)

# Executa a função
weak_scaling SIZE_LIST THREADS_LIST