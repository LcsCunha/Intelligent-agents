import time
from classeAmbiente import classeAmbiente

# tempo inicial
start = time.time()

ambiente = classeAmbiente()

ambiente.getAmbiente()

#ambiente.testeColeta()

#ambiente.testeSelecao()

end = time.time()
print(end - start)