
apetece_helado_input = input("¿te apetece un helado? (Si/ No:")
tiene_dinero_input = input("¿Tienes dinero para un helado? (Si / No):")
esta_el_senor_helados_input = input("¿Esta el señor de los helados? (Si / No")
esta_su_tia_input = input("¿Estás con tu tía?")

apetece_helado = apetece_helado_input == "Si"
puede_permitirselo = tiene_dinero_input == "Si" or esta_su_tia_input == "Si"
esta_el_senor_helados = esta_el_senor_helados_input == "Si"

if apetece_helado and puede_permitirselo and esta_el_senor_helados:
    print("Pues comete un helado")
else:
    print("Pues nada")









