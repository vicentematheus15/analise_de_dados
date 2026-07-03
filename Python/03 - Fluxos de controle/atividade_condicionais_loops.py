frutas = []
frutas.append("Banana")
frutas.append("Ameixa")
frutas.append("Laranja")
print(frutas)

frutas.pop()
print(frutas)

from collections import deque

frutas = deque()
frutas.append("Banana")
frutas.append("Ameixa")
frutas.append("Laranja")
frutas.append("Uva")
frutas.append("Jabuticaba")
print(frutas)

frutas.popleft()
for fruta in frutas:
    print(fruta)


for fruta in frutas:
    if fruta == "Uva":
        print(fruta)



