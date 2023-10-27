import matplotlib.pyplot as plt

#Grafico_De_Linha
"""
x = [10, 20, 30]
y = [10, 20, 30]
plt.title("Olá gráfico")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.plot(x, y)
plt.show()
"""

#Grafico_De_Barras
"""
a = [1,2,3,4,5]
b = [20,2,10,3,-1]
titulo = "Grafico de barras"
eixox = "Eixo X"
eixoy = "Eixo Y"
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
plt.bar(a,b)
plt.show()
"""

#Barras_Comparacao
"""
a = [1,2,3,4,5]
b = [2,3,5,6,7]
a2 = [2,3,4,5,6]
b2 = [4,5,6,7,8]

plt.title("WTF")
plt.xlabel("EixoX")
plt.ylabel("EixoY")
plt.bar(a,b, label= "g1")
plt.bar(a2,b2, label="g2")
plt.legend()
plt.show()
"""

#Grafico_Dispersao_Pontos

a = [1,2,3,4,5]
b = [2,3,5,6,7]
pontos = [100,200,50,1000,100]
plt.title("WTF")
plt.xlabel("EixoX")
plt.ylabel("EixoY")
plt.scatter(a, b, label="PONTOS", color="black", marker="*", s=pontos)
plt.plot(a,b, linestyle="--")
plt.legend()
plt.savefig("figura.pdf")
plt.show()
