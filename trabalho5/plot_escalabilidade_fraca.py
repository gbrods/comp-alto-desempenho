import matplotlib.pyplot as plt

def read_results(filename):
    threads = []
    sizes = []
    total_runtime = []

    with open(filename, 'r') as f:
        for line in f:
            thread, size, runtime = line.split()
            threads.append(int(thread))
            sizes.append(int(size))
            total_runtime.append(float(runtime))

    print("Threads:", threads)
    print("Tamanhos da matriz:", sizes)
    print("Total Runtime:", total_runtime)
    return threads, sizes, total_runtime

def plot_results(threads, sizes, total_runtime, title, filename):
    plt.figure()
    plt.plot(threads, total_runtime, label='Tempo total de execução', marker='o')
    for i, size in enumerate(sizes):
        plt.annotate(f'n = {size}', (threads[i], total_runtime[i]), textcoords="offset points", xytext=(0, 8), ha='center')
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
threads, sizes, total_runtime = read_results('resultados_escalabilidade_fraca.txt')

# Chama a função de plotagem
plot_results(threads, sizes, total_runtime, 'Escalabilidade Fraca', 'weak_scaling.png')
