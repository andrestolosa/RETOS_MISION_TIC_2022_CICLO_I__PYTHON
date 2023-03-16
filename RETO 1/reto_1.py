

def CDT(usuario, cantidad, tiempo):
    if tiempo<=2:
        valor_perder=cantidad*0.02
        valor_total_perder=cantidad-valor_perder
        return "Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}".format(usuario,cantidad,tiempo,valor_total_perder)
    else: 
        valor_interes=(cantidad*0.03*tiempo)/12
        valor_total_ganar=valor_interes+cantidad
        return "Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}".format(usuario,cantidad,tiempo,valor_total_ganar)
           

	
    

CDT( 'AB012', 1000000, 3)
CDT ('ER3366', 650000, 2)

print(CDT("AB1012",1000000,3)) 
print (CDT('ER3366', 650000, 2))