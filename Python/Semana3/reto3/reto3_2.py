def AutoPartes(ventas: list):
    result={}
    for x in range(len(ventas)):
        result[x]=[ventas[x]]
    return result    

def consultaRegistro(ventas, idProducto):
    result2 = {}
    for i in ventas:
        if idProducto==ventas[i][0][0]:
            result2[i]=ventas[i]
    result3=''
    if len(result2)==0:
        result3='No hay registro de venta de ese producto\n'    
    else:
        for i in result2:
            result3 += 'Producto consultado : {}  Descripción  {}  #Parte  {}  Cantidad vendida  {}  Stock  {}  Comprador {}  Documento  {}  Fecha Venta  {}\n'.format(ventas[i][0][0],ventas[i][0][1],ventas[i][0][2],ventas[i][0][3],ventas[i][0][4],ventas[i][0][5],ventas[i][0][6],ventas[i][0][7])
    return(print(result3))     
   

consultaRegistro(AutoPartes([(9852,'Culata', 'XC9875',2,165,'Luis Molero',3455846,'14/06/2020'),
(9852,'Culata', 'XC9875',2,165,'Jose Mejia',1355846,'14/06/2020'),
(2564,'Cárter', 'PT29872',2,32,'Peter Cerezo',8545436,'14/06/2020'),
(5412,'válvula', 'AZ8798',2,11,'Juan Peña',568975,'14/06/2020')]), 9852)