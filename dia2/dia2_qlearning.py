import numpy as np
import gymnasium as gym

# ambiente FrozenLake (sem escorregar)
env = gym.make("FrozenLake-v1", is_slippery=False)

# Parâmetros
n_estados = env.observation_space.n
n_acoes = env.action_space.n
env = gym.make("FrozenLake-v1", is_slippery=False)
alfa = 0.8      # prendizado
gama = 0.95     # desconto
epsilon = 1.0   # taxa de exploração inicial
epsilon_min = 0.01
decaimento = 0.995
episodios = 3000

print(f" Iniciando treinamento...")
print(f"Estados: {n_estados}, Ações: {n_acoes}\n")

# Treinamento
for ep in range(episodios):
    estado, _ = env.reset()
    terminado = False
    recompensa_total = 0

    while not terminado:
        # explora ou aproveita
        if np.random.rand() < epsilon:
            acao = env.action_space.sample()  # EXPLORA
        else:
            acao = np.argmax(Q[estado])       # APROVEITA

        #  ação
        prox_estado, recompensa, terminado, truncado, _ = env.step(acao)
        recompensa_total += recompensa

        # Atualiza Q-table 
        melhor_prox = np.max(Q[prox_estado])
        Q[estado, acao] = Q[estado, acao] + alfa * (recompensa + gama * melhor_prox - Q[estado, acao])

        estado = prox_estado
        terminado = terminado or truncado

    # Decai a exploração
    epsilon = max(epsilon_min, epsilon * decaimento)

    if (ep + 1) % 500 == 0:
        print(f"Episódio {ep+1}: Recompensa = {recompensa_total:.0f}, Epsilon = {epsilon:.3f}")

print("\n Treinamento concluído!")
print("\n Q-table final:")
print(Q)

# Teste do agente treinado
print("\n Testando agente treinado...")
estado, _ = env.reset()
terminado = False
caminho = [estado]

while not terminado:
    acao = np.argmax(Q[estado])
    estado, recompensa, terminado, truncado, _ = env.step(acao)
    caminho.append(estado)

print(f"Caminho percorrido: {caminho}")
env.close()