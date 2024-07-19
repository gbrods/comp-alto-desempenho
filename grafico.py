import matplotlib.pyplot as plt

# Dados do programa
algorithms = ['Inicial', 'Com otimização automática', 'Após perfilagem', 'Após perfilagem e com otimização automática']
times = [490.671564, 331.244648, 309.472181, 92.799536]

# Configurar o gráfico
plt.figure(figsize=(10, 6))
plt.bar(algorithms, times, color=['blue', 'green', 'orange', 'red'])

# Adicionar título e rótulos
plt.title('Tempo total de execução de diferentes versões do código', fontsize=18)
#plt.xlabel('Versões do código')
plt.ylabel('Tempo (segundos)', fontsize=16)

# Adicionar valores acima das barras
for i, time in enumerate(times):
    plt.text(i, time + 1, f'{time:.2f}', ha='center', va='bottom', fontsize=14)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid(True, which='both', axis='y', linestyle='--', linewidth=0.3)

# Exibir o gráfico
plt.show()