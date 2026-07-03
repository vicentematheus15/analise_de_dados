# lista normal
personagens = ['Sylas', 'Darius', 'Senna', 'Leona']

#adiciona ao final
personagens.append('Diana')

#adiciona em um local específico
personagens.insert(0, 'Morgana' )
print(personagens)

#remove o elemento passado no parâmetro
personagens.remove('Morgana')
print(personagens)

#remove o elemento por indice
personagens.pop(1)
print(personagens)
 

# lista com tuplas (variáveis com 2 valores)
#cada valor de variável é um indice, entao o primeiro personagem tem o nome no indice 0 e sua classe no índice 1
personagens2 = [('Morgana', 'encantadora'), ('Darius', 'lutador'), ('Senna', 'atiradora')]

#acessando personagem 0 todo
print(personagens2[0])
#acessando o primeiro valor do personagem 0
print(personagens2[0] [0])
#acessando o segundo valor do personagem 0
print(personagens2[0] [1])
