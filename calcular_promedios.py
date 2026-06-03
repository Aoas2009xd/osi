notas = []

while True:
    nota = float(input("digite una nota entre 10 o 70: "))
    if nota == 0:
        break
    elif nota < 10 or nota > 70:
        print("nota invalida. digite una nota entre 10 o 70:")
    else:
        notas.append(nota)

print(notas)

resultados = []  
for nota in notas:
    if nota < 40:
        clasificación_de_la_nota = "desaprobado"
    elif 40 <= nota < 50:
        clasificación_de_la_nota = "aprobado"
    elif 50 <= nota < 60:
        clasificación_de_la_nota = "bueno"
    elif 60 <= nota < 69:
        clasificación_de_la_nota = "muy bueno"
    elif nota >= 69:
        clasificación_de_la_nota = "excelente"  

    resultados.append((nota, clasificación_de_la_nota))
    print(f"La nota {nota} es {clasificación_de_la_nota}")

print(resultados) 