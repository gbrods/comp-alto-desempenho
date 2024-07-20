#!/bin/bash

# Define o diretório onde a biblioteca icx está localizada
LIB_PATH="/opt/intel/oneapi/2024.2/lib/"

# Atualiza LD_LIBRARY_PATH
export LD_LIBRARY_PATH="$LIB_PATH:$LD_LIBRARY_PATH"

# Verifica se a variável de ambiente está configurada corretamente
echo "LD_LIBRARY_PATH: $LD_LIBRARY_PATH"

# Executa o programa com diferentes números de threads
strong_scaling() {
    local fixed_size=$1
    shift
    local threads_list=("$@")
    local results=()

    for threads in "${threads_list[@]}"; do
        echo "Executando com $threads threads"
        # Executa o programa com a variável de ambiente OMP_NUM_THREADS
        export OMP_NUM_THREADS=$threads
        output=$(./jacobi_paralelizado -n "$fixed_size" 2>&1)
        echo "$output"
        
        # Extrai o tempo total de execução
        total_runtime=$(echo "$output" | grep "Total runtime" | awk '{print $(NF-1)}')
        if [ -n "$total_runtime" ]; then
            results+=("$threads $total_runtime")
        fi
    done

    # Imprime e salva os resultados em um arquivo txt
    for result in "${results[@]}"; do
        echo "$result" >> resultados_escalabilidade_forte.txt
    done
}

# Parâmetros de entrada
FIXED_SIZE=4000
THREADS_LIST=(1 2 4 6 8 10 12)

# Executa a função
strong_scaling "$FIXED_SIZE" "${THREADS_LIST[@]}"