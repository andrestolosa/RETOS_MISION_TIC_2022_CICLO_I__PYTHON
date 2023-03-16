import pandas as pd


rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022/blob/3f3847bbf2dbe4b2cf4dcceb96a455d92c88f9c5/movies.csv?raw=true' 

def listaPeliculas(rutaFileCsv: str)-> str:
    if rutaFileCsv.split('.')[-1] != 'csv': 
        try:
            csv = pd.read_csv(rutaFileCsv)
 
            subconjuntoColumnas = pd.read_csv(rutaFileCsv, usecols = [1, 2, 3, 4, 5, 6, 7])

            csv["Net Earnings"] = csv["Gross Earnings"] - csv["Budget"]


            ordenarPeliculas = csv[['Net Earnings']].sort_values(['Net Earnings'], ascending=[False])
 
            print(ordenarPeliculas)


        except:  
            print('Error al leer el archivo de datos.')
    else:
        print('Extensión inválida.')
    return
print(listaPeliculas(rutaFileCsv))