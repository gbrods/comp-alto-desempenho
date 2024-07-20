import matplotlib.pyplot as plt

def read_results(filename):
    threads = []
    total_runtime = []

    with open(filename, 'r') as f:
        for line in f:
            thread, runtime = line.split()
            threads.append(int(thread))
            total_runtime.append(float(runtime))

    print(threads)
    print(total_runtime)
    return threads, total_runtime

def plot_results(threads, total_runtime, title, filename):
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

# Lê os resultados do arquivo
threads, total_runtime = read_results('resultados_escalabilidade_forte.txt')

# Chama a função de plotagem
plot_results(threads, total_runtime, 'Escalabilidade Forte', 'strong_scaling.png')
