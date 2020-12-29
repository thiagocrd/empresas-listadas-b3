import pandas as pd

df = pd.read_csv(
    'InstrumentsConsolidatedFile_20201229_1.csv',
    usecols= ['RptDt','TckrSymb', 'SgmtNm', 'SctyCtgyNm', 'TradgStartDt', 'CorpGovnLvlNm'],
    sep=';',
    encoding = "latin",
    dtype={'CorpGovnLvlNm': 'str'})
df = df[ (df['SctyCtgyNm'] == 'SHARES') & (df['SgmtNm'] == 'CASH') & (df['RptDt'] > df['TradgStartDt']) & (df['CorpGovnLvlNm'] != 'MERCADO DE BALCÃO') ]

df2 = pd.DataFrame()
df2['Ticker'] = df['TckrSymb']
df2['Ticker_Prefix'] = df['TckrSymb'].str[:4]
df2.drop_duplicates('Ticker_Prefix', inplace=True)

print(df2['Ticker'])