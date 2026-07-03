#dicionarios sao listas com chave e valor em vez de índices.
#TRANSFORMANDO LISTA COM YUPLAS EM DICIONÁRIOS (para buscar por chave)
personagens2 = [('Morgana', 'encantadora'), ('Darius', 'lutador'), ('Senna', 'atiradora')]

personagens2_dict = dict(personagens2)
print(personagens2_dict)

#acessando pela chave
print(personagens2_dict['Morgana'])

#adicionando um novo par de chave e valor
personagens2_dict['Ziggs'] = 'mago'
print(personagens2_dict)

#retirando com por um elemento pela chave
personagens2_dict.pop('Ziggs')
print(personagens2_dict)