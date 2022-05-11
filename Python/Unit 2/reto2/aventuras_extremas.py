informacion = {"id_cliente" : 1, "nombre" : "", "edad" : 5, "primer_ingreso" : True}   

def cliente (informacion:dict)->dict:
	nombre = informacion['nombre']
	edad = informacion['edad']
	primer_ingreso = informacion['primer_ingreso']
	apto = True
	if not(type(edad) is int) or not(type(primer_ingreso) is bool) or edad<7:
		total_boleta ="N/A" 
		apto= False  
		atraccion = "N/A"
		return  {'nombre': nombre, 'edad': edad, 'atraccion': atraccion,'apto':apto, 'primer_ingreso': primer_ingreso, 'total_boleta': total_boleta}
	if edad > 18:
		atraccion = "X-Treme"
		total_boleta = 20000
		if primer_ingreso:
			total_boleta -= (20000*0.05)	
	if edad >= 15 and edad <= 18:
		atraccion = "Carroschocones"
		total_boleta = 5000  
		if primer_ingreso:
			total_boleta -= (5000*0.07)                        
	if edad >= 7 and edad < 15:
		atraccion = "Sillas voladoras"
		total_boleta = 10000
		if primer_ingreso:
			total_boleta -= (10000*0.05)                                                         
	return {'nombre': nombre, 'edad': edad, 'atraccion': atraccion,'apto':apto, 'primer_ingreso': primer_ingreso, 'total_boleta': total_boleta}

print(cliente(informacion))
