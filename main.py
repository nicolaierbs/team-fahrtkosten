import datareader
import pandas as pd
import geo


if __name__ == '__main__':
    df = datareader.read_sheet('Fahrer', refresh=False)
    df['Distanz'] = df['Ort'].apply(lambda x: geo.distance('Darmstadt', x))
    df['Distanz'] = df['Distanz']/1000
    df['Faktor'] = df['Faktor']*2

    km_preis = 0.23
    df['Erstattung'] = df['Faktor'] * km_preis * df['Distanz']
    print(df)

    print()
    df = df.groupby('Name').agg('sum')
    print(df[['Erstattung']])

    print()
    print(f'Gesamtersattung {df["Erstattung"].sum()}')
