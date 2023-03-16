def AutoPartes(ventas:list):
    return dict(zip(range(len(ventas)), ventas))


def consultaRegistro(ventas, idProducto):
    x= False
    for valor in ventas.values():
        if idProducto == valor[0]:
            print(f"Producto consultado : {valor[0]}  Descripción  {valor[1]}  #Parte  {valor[2]}  Cantidad vendida  {valor[3]}  Stock  {valor[4]}  Comprador {valor[5]}  Documento  {valor[6]}  Fecha Venta  {valor[7]}")
            x= True
    if x== False:
       print("No hay registro de venta de ese producto")
            

consultaRegistro(AutoPartes([
 (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
 (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
 (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
 (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
 (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)

