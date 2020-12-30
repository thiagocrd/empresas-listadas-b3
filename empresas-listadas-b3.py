import pandas as pd

# Usamos apenas as colunas em que precisamos aplicar filtros
# O arquivo .csv não vem formatado em utf-8, então usamos o encoding = 'latin'
# Definimos o dtype da coluna CorpGovnLvlNm como string para não termos problema com a memória
df = pd.read_csv(
    'InstrumentsConsolidatedFile_20201229_1.csv',
    usecols= ['RptDt','TckrSymb', 'SgmtNm', 'SctyCtgyNm', 'TradgStartDt', 'CorpGovnLvlNm'],
    sep=';',
    encoding = 'latin',
    dtype={'CorpGovnLvlNm': 'str'})

# Filtramos SctyCtgyNm por ações e units (SHARES e UNIT)
# Filtramos SgmtNm por ações do mercado à vista (CASH)
# Filtramos os ativos cuja data de início da negociação seja anterior à data de publicação do arquivo .csv
# Filtramos as ações que não sejam negociadas no mercado de balcão
df = df[ ( (df['SctyCtgyNm'] == 'SHARES') | (df['SctyCtgyNm'] == 'UNIT') ) & (df['SgmtNm'] == 'CASH') & (df['RptDt'] > df['TradgStartDt']) & (df['CorpGovnLvlNm'] != 'MERCADO DE BALCÃO') ]

df_listed_stocks = pd.DataFrame()
df_listed_stocks['Ticker'] = df['TckrSymb']

print(df_listed_stocks['Ticker'])