horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
horas_e = float(input("Introduce tus horas extras: "))
horas_e = horas_e * 2
paga = (horas * coste)+horas_e
print("Tu paga es", paga)