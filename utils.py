import pandas as pd 
from unidecode import unidecode
import json
from urllib.request import urlopen


def delitos(input):
    dic = {'Amenazas':'amenazas',
            'Abigeato':'abigeato',
            'Delitos Sexuales':'delitos_sexuales',
            'Extorsión':'extorsion',
            'Homcicidios en Accidentes de Transito':'homicidios_accidente_transito',
            'Homicidios':'homicidios',
            'Hurto a Comercio':'hurto_a_comercio',
            'Hurto a Motocicletas':'hurto_a_motocicletas',
            'Hurto a Personas':'hurto_a_personas',
            'Hurto a Pirateria Terrestre':'hurto_a_pirateria_terrestre',
            'Hurto a Residencias':'hurto_a_residencias',
            'Hurto a Automotores':'hurto_automotores',
            'Hurto a Entidades Financieras':'hurto_entidades_financieras',
            'Lesiones en Accidentes de Transito':'lesiones_accidente_transito_',
            'Lesiones Personales':'lesiones_personales',
            'Secuestro':'secuestro',
            'Terrorismo':'terrorismo',
            'Violencia Intrafamiliar':'violencia_intrafamiliar'}
            
    return dic[input]
    

def data_compiler(data):
    df = pd.read_excel(f'data/{data}2021.xlsx')
    df.columns = [(i.lower()).strip() for i in df.columns]

    df = df[['departamento','municipio',]]
    dptos = ['SANTAFE DE BOGOTA D.C' if (df.loc[i]['departamento']=='CUNDINAMARCA' and df.loc[i]['municipio'] == 'BOGOTÁ D.C. (CT)') else df.loc[i]['departamento'] for i in range(len(df))]

    df['departamento'] = dptos
    df['departamento'].replace({'GUAJIRA':'LA GUAJIRA','VALLE':'VALLE DEL CAUCA',
                            'SAN ANDRES':'ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA'},inplace=True)
    df['departamento'].replace({old:unidecode(old) for old in df['departamento'].unique()},inplace=True)
    df['departamento'].replace({'NARINO':'NARIÑO'},inplace=True)
    
    df = df['departamento'].value_counts()
    return df


def geo_data_compiler():
    geo_json_colombia = 'https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json' 
    with urlopen(geo_json_colombia) as response:
        counties = json.load(response)
    return counties

