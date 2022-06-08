def CDT(nombre, cantidad, tiempo):
    while(tiempo > 0):
        por_interes = 0.03
        por_perdida = 0.02
        if tiempo > 0 and tiempo <= 2:
            valor_perdido = cantidad * por_perdida
            valor_total = cantidad - valor_perdido
        if tiempo > 2:
            valor_interes = (cantidad * por_interes * tiempo) / 12
            valor_total = cantidad + valor_interes
        print("Para el usuario " + nombre + " La cantidad de dinero a recibir, según el monto inicial " + str(cantidad) +  " para un tiempo de " + str(tiempo) + " meses es: " + str(valor_total))
        return "Para el usuario " + nombre + " La cantidad de dinero a recibir, según el monto inicial " + str(cantidad) +  " para un tiempo de " + str(tiempo) + " meses es: " + str(valor_total)

    CDT("Ivonne", 20, 10)