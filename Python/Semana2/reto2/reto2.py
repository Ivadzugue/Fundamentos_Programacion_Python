testCases[1] = {"id_cliente" : 1, "nombre" : "a", "edad" : 20, "primer_ingreso" : True}   
testCases[2] = {"id_cliente" : 1, "nombre" : "b", "edad" : 20, "primer_ingreso" : False}   
testCases[3] = {"id_cliente" : 1, "nombre" : "c", "edad" : 3, "primer_ingreso" : True}   
testCases[4] = {"id_cliente" : 1, "nombre" : "d", "edad" : 17, "primer_ingreso" : True}   
testCases[5] = {"id_cliente" : 1, "nombre" : "e", "edad" : 17, "primer_ingreso" : False}   
testCases[6] = {"id_cliente" : 1, "nombre" : "f", "edad" : 8, "primer_ingreso" : True}   
testCases[7] = {"id_cliente" : 1, "nombre" : "g", "edad" : 8, "primer_ingreso" : False}   
testCases[8] = {"id_cliente" : 1, "nombre" : "h", "edad" : 0, "primer_ingreso" : True}   
testCases[9] = {"id_cliente" : 1, "nombre" : "i", "edad" : -1, "primer_ingreso" : True}   
testCases[10] = {"id_cliente" : 1, "nombre" : "", "edad" : -1, "primer_ingreso" : True}   
testCases[11] = {"id_cliente" : 1, "nombre" : "", "edad" : 20, "primer_ingreso" : False}  

def cliente (informacion:dict)->dict:
    nombre = informacion['nombre']
    edad = int(informacion['edad'])
    primer_ingreso = bool(informacion['primer_ingreso'])
    apto = True
    if edad > 18:
        atraccion = "X-Treme"
        total_boleta = 20000
        if primer_ingreso:
            total_boleta -= (20000*0.05)	
    if edad >= 15 and edad <= 18:
        atraccion = "Carros chocones"
        total_boleta = 5000  
        if primer_ingreso:
            total_boleta -= (5000*0.07)                        
    if edad >= 7 and edad < 15:
        atraccion = "Sillas voladoras"
        total_boleta = 10000
        if primer_ingreso:
            total_boleta -= (10000*0.05)
    if edad < 7 and edad >=0:
        total_boleta ="N/A" 
        apto= False  
        atraccion = "N/A"                                                           
    return {'nombre': nombre, 'edad': edad, 'atraccion': atraccion,'apto':apto, 'primer_ingreso': primer_ingreso, 'total_boleta': total_boleta}

for i in testCases:
	print(cliente(testCases[i]))
