import subprocess
import matplotlib.pyplot as plt

# Executa o programa com diferentes tamanhos da matriz e número de threads
def weak_scaling(size_list, threads_list):
    results = []
    for threads in threads_list:
        size = size_list[threads_list.index(threads)]
        print(f"Executando com {threads} threads e tamanho da matriz {size}")
        env = {"OMP_NUM_THREADS": str(threads)}
        result = subprocess.run(['./jacobi_paralelizado', '-n', str(size)], capture_output=True, text=True, env=env)
        print(result.stdout)
        output = result.stdout
        total_runtime = float([line for line in output.splitlines() if "Total runtime" in line][0].split()[-2])
        results.append((threads, size, total_runtime))
    return results

# Cria um gráfico com os resultados
def plot_results(results, title, filename):
    threads, sizes, total_runtime = zip(*results)
    plt.figure()
    plt.plot(threads, total_runtime, label='Tempo total de execução', marker='o')
    plt.xlabel('Número de threads')
    plt.ylabel('Total Runtime (s)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.xscale('linear')
    plt.yscale('linear')
    plt.savefig(filename)
    plt.show()

# Executa as ações descritas acima
threads_list = [1, 2, 4, 8, 16]
size_list = [3000, 3500, 4000, 4500, 5000]
results = weak_scaling(size_list, threads_list)
plot_results(results, 'Escalabilidade Fraca', 'weak_scaling.png')
