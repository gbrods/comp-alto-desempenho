import subprocess
import matplotlib.pyplot as plt

# Executa o programa com tamanho da matriz fixo e diferentes números de threads
def strong_scaling(fixed_size, threads_list):
    results = []
    for threads in threads_list:
        print(f"Executando com {threads} threads")
        env = {"OMP_NUM_THREADS": str(threads)}
        result = subprocess.run(['./jacobi_paralelizado', '-n', str(fixed_size)], capture_output=True, text=True, env=env)
        print(result.stdout)
        output = result.stdout
        total_runtime = float([line for line in output.splitlines() if "Total runtime" in line][0].split()[-2])
        results.append((threads, total_runtime))
    return results

# Cria um gráfico com os resultados
def plot_results(results, title, filename):
    threads, total_runtime = zip(*results)
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
fixed_size = 1000
results = strong_scaling(fixed_size, threads_list)
plot_results(results, 'Escalabilidade Forte', 'strong_scaling.png')