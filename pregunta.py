"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import numpy as np

def ingest_data():

    #
    # Inserte su código aquí
    #
    
    
    df=pd.read_fwf('clusters_report.txt',
                    on_bad_lines='skip',
                    #colspecs="infer",
                    #names=column_names,
                     widths=[9, 15, 15,70])
    df.columns=('cluster', 'cantidad de palabras clave', 'porcentaje de palabras clave', 'principales palabras clave')
    df=df.drop([0, 1],axis=0).reset_index(drop=True)
    
    df = pd.DataFrame(df)
    for i in range(len(df['cluster'])):
        if df['cluster'][i]== pd.NAn:
            print('null')
    return df.head(5)

print(ingest_data())