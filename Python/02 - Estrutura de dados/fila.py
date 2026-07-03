#para fazer uma lista ter o comportamento de fila é necessário importar a classe "deque" do módulo "collections"
from collections import deque

#isso faz com que um lista tenha o comportamento de uma fila FIFO (first in first out)

fila = deque()
fila.append(1)
fila.append(2)
fila.append(3)
print(fila)

fila.popleft()
print(fila)

