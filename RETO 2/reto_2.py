



def cliente(informacion:dict):
    if informacion['edad'] >18 :
        atraccion='X-Treme'
        valor_boleta=20000
        if informacion ['primer_ingreso']==True:
            descuento=valor_boleta*0.05
            total_boleta=valor_boleta-descuento
            respuesta= {'nombre': informacion['nombre'], 'edad': informacion['edad'], 'atraccion': atraccion,'apto': True, 'primer_ingreso':informacion['primer_ingreso'], 'total_boleta':total_boleta }
        else:        
            respuesta= {'nombre': informacion['nombre'], 'edad': informacion['edad'], 'atraccion': atraccion,'apto': True, 'primer_ingreso':informacion['primer_ingreso'], 'total_boleta':valor_boleta }
        return respuesta
    elif informacion['edad'] >=15 and informacion['edad'] <=18:
        atraccion='Carros chocones'
        valor_boleta=5000
        if informacion ['primer_ingreso']==True:
            descuento=valor_boleta*0.07
            total_boleta=valor_boleta-descuento
            respuesta= {'nombre': informacion['nombre'], 'edad': informacion['edad'], 'atraccion': atraccion,'apto': True, 'primer_ingreso':informacion['primer_ingreso'], 'total_boleta':total_boleta }
        else:        
            respuesta= {'nombre': informacion['nombre'], 'edad': informacion['edad'], 'atraccion': atraccion,'apto': True, 'primer_ingreso':informacion['primer_ingreso'], 'total_boleta':valor_boleta }
        return respuesta
    elif informacion['edad']  >=7 and informacion['edad']  <15:
        atraccion='Sillas voladoras'
        valor_boleta=10000
        if informacion ['primer_ingreso']==True:
            descuento=valor_boleta*0.05
            total_boleta=valor_boleta-descuento
            respuesta= {'nombre': informacion['nombre'], 'edad': informacion['edad'], 'atraccion': atraccion,'apto': True, 'primer_ingreso': informacion['primer_ingreso'], 'total_boleta':total_boleta }
        else:        
            respuesta= {'nombre': informacion['nombre'], 'edad': informacion['edad'], 'atraccion': atraccion,'apto': True, 'primer_ingreso':informacion['primer_ingreso'], 'total_boleta':valor_boleta }
        return respuesta
    else:
        respuesta= {'nombre': informacion['nombre'], 'edad': informacion['edad'], 'atraccion': 'N/A', 'apto': False, 'primer_ingreso':informacion['primer_ingreso'], 'total_boleta':'N/A' }
    return respuesta



informacion={'id cliente':2,
'nombre': 'gloria suarez', 
'edad':1, 
'primer_ingreso': False

}



informacion1 = {'id_cliente' : 1, 'nombre' : "Johana Fernandez", 'edad': 20, 'primer_ingreso': True }
informacion2 = {'id_cliente' : 1, 'nombre' : "Johana Fernandez", 'edad': 20, 'primer_ingreso': False }
informacion3 = {'id_cliente' : 1, 'nombre' : "Gloria Suarez", 'edad': 3, 'primer_ingreso': True }
informacion4 = {'id_cliente' : 1, 'nombre' : "Tatiana Suarez", 'edad': 17, 'primer_ingreso': True }
informacion5 = {'id_cliente' : 1, 'nombre' : "Tatiana Suarez", 'edad': 17, 'primer_ingreso': False }
informacion6 = {'id_cliente' : 1, 'nombre' : "Tatiana Ruiz", 'edad': 8, 'primer_ingreso': True }
informacion7 = {'id_cliente' : 1, 'nombre' : "Tatiana Ruiz", 'edad': 8, 'primer_ingreso': False }

print(cliente(informacion1))
print(cliente(informacion2))
print(cliente(informacion3))
print(cliente(informacion4))
print(cliente(informacion5))
print(cliente(informacion6))
print(cliente(informacion7))

