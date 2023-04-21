import math as m
import pandas as pd

# Input
albedo = pd.read_csv("C:\Tassio\Trabalho_individual\Dia1.csv", sep=";")
Coleta = sorted(abs(albedo['Time']))
print(Coleta)
lat = -23.20077 * m.pi/180
long = -45.89085
Es = 1367 * 3.6

# Ângulo Solar (Dia Juliano= 22/03 - dia juliano: 81, 13/04 - dia juliano: 103)
t = (2 * m.pi * (81 - 1)) / 365
print("t:",t)

# Equação do tempo
Et = 0.000075 + 0.001868 * m.cos(t)-0.032077*m.sin(t)-0.014615*m.cos(2*t)-0.04089*m.sin(2*t)*(229.18)
print('Et', Et)
teste = 4*(45-(abs(long)))
print(teste)

# Horario Local Aparente(LAT - Local Aparent Time)
h = [x + ((4*(-45-(long))) + Et) for x in Coleta]
dif = [x - 12 for x in h]
print(h)

# Declinação Solar
g = (0.006918 - 0.399912 * (m.cos(t)) + 0.070257 * (m.sin(t)) - 0.006758 * (m.cos(2 * t)) + 0.000907 * (m.sin(2 * t)) -
     0.002697 * (m.cos(3 * t)) + 0.00148 * (m.sin(3 * t)))

# E0
Eo = 1.000110 + (0.034221 * m.cos(t)) + (0.001280 * m.sin(t)) + (0.000719 * m.cos(2 * t)) + (0.000077 * m.sin(2 * t))


for c in dif:
    #Ângulo horário Solar
    w = ((m.pi / 12) * c * (180 / m.pi)) * m.pi / 180
    #Irradiância Solar
    Irradiancia = [(Es * Eo * (m.sin(g) * m.sin(lat) + m.cos(g) * m.cos(lat) * m.cos(w)))]
    #Irradiação
    Irradiacao = [(Es * Eo * (m.sin(g) * m.sin(lat) + (24/m.pi) * m.sin(m.pi/24) * m.cos(g) * m.cos(lat) * m.cos(w)))]
    print(f"1° Coleta - Irradiância {Irradiancia}")
    print(f"1° Coleta - Irradiação {Irradiacao}")


