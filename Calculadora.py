print ("Bienvenido a la Calculadora")
operacion_elegida = input("¿Que operación quieres realizar? Sumar /Restar / Multiplicar / Dividir:")

resultado_final = 0
primer_numero = 0
segundo_numero= 0

primer_numero = int(input("Eliga el primer número:"))
segundo_numero = int (input("Eliga el segundo número:"))


if operacion_elegida == "Sumar":
    resultado_final = primer_numero + segundo_numero
    print("Calculando... ")
    print("Tu resultado es {}" .format(resultado_final))
elif operacion_elegida == "Restar":
    resultado_final= primer_numero - segundo_numero
    print("Calculando... ")
    print("Tu resultado es {}".format(resultado_final))
elif operacion_elegida == "Multiplicar":
    resultado_final = primer_numero * segundo_numero
    print("Calculando... ")
    print("Tu resultado es {}".format(resultado_final))
elif operacion_elegida == "Dividir":
    resultado_final = primer_numero / segundo_numero
    print("Calculando... ")
    print("Tu resultado es {}".format(resultado_final))

