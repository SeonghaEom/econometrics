from pandas_datareader import data
# import matplotlib.pyplot as plt
import pandas as pd



tickersKS = ['102110', '047810', '000080', '009240', '001040', '336260', '282330', '004170', '252670', '028670','001450', '005385', '204320', '020150', '185750', '007310', '153130', '138930', '000880', '006260']
#add suffix .ks
suf_tickersKS = [sub + '.ks' for sub in tickersKS] 
print (suf_tickersKS)
tickersKD = ['131290' , '102710', '095610', '348150', '222800', '214450', '068240', '078070', '267980', '200230', '064550', '319660', '332570', '035600', '138080', '032620', '091700', '086390', '050890', '206650']
suf_tickersKD = [sub + '.KQ' for sub in tickersKD] 
# df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]
# print (df.head())


start_date = '2018-09-19'
end_date = '2019-03-18'

kosdaq = data.DataReader('^KQ11', 'yahoo', start_date, end_date)
print (kosdaq)
pctchange = kosdaq.pct_change()
print("percent change between rows(Period=1):")
print(pctchange["Close"])

print (pctchange[1:].var()['Close'])
# User pandas_reader.data.DataReader to load the desired data. As simple as that.
pctchange_panel = data.DataReader('131290.KQ', 'yahoo', start_date, end_date)
pctchange_panel = pctchange_panel.pct_change()
pctchange_panel['pivot'] = pctchange["Close"]

del pctchange_panel['High']
del pctchange_panel['Low']
del pctchange_panel['Open']
del pctchange_panel['Volume']
del pctchange_panel['Adj Close']

print (pctchange_panel.head(5))
print (pctchange_panel.cov())
beta = pctchange_panel.cov()['Close']['pivot']/pctchange_panel.cov()['pivot']['pivot']

print (beta)

def getBeta (code_num, start_date, end_date, index):
    kosdaq = data.DataReader(index, 'yahoo', start_date, end_date)
    pctchange = kosdaq.pct_change()
    # print("percent change between rows(Period=1):")
    # print(pctchange["Close"])

    # print (pctchange[1:].var()['Close'])
    # User pandas_reader.data.DataReader to load the desired data. As simple as that.
    try: pctchange_panel = data.DataReader(code_num, 'yahoo', start_date, end_date)
    except Exception as e:
        print (e)
        return index, code_num, -1
    pctchange_panel = pctchange_panel.pct_change()
    pctchange_panel['pivot'] = pctchange["Close"]

    del pctchange_panel['High']
    del pctchange_panel['Low']
    del pctchange_panel['Open']
    del pctchange_panel['Volume']
    del pctchange_panel['Adj Close']

    # print (pctchange_panel.head(5))
    # print (pctchange_panel.cov())
    beta = pctchange_panel.cov()['Close']['pivot']/pctchange_panel.cov()['pivot']['pivot']
    
    print ("From "+ start_date + " To " + end_date +  " " + code_num + " : ", beta)
    return index, code_num, beta


global df_list
df_list = []

for ticker in suf_tickersKS:
    index, code_num, beta = getBeta(ticker, "2018-09-19", "2019-03-19", '^KS11')
    row = []
    row.append(index)
    row.append(code_num)
    row.append(beta)
    df_list.append(row)

    # 2019-03-20 ~ 2019-09-18
    index, code_num, beta = getBeta(ticker, "2019-03-20", "2019-09-18", '^KS11')
    row = []
    row.append(index)
    row.append(code_num)
    row.append(beta)
    df_list.append(row)

    # 2019-09-19 ~ 2020-03-19
    index, code_num, beta = getBeta(ticker, "2019-09-19", "2020-03-19", '^KS11')
    row = []
    row.append(index)
    row.append(code_num)
    row.append(beta)
    df_list.append(row)

    # 2019-03-20 ~ 2020-09-19
    index, code_num, beta = getBeta(ticker, "2019-03-20", "2020-09-19", '^KS11')
    row = []
    row.append(index)
    row.append(code_num)
    row.append(beta)
    df_list.append(row)


print (df_list)

df = pd.DataFrame(df_list)
# # df.to_csv('./kospi.csv', sep=',', na_rep='NaN')
df.to_csv('./kospi_volume.csv', sep=',', na_rep='NaN')

# # find for KOSDAQ
# df_list = []

# for ticker in suf_tickersKD:
#     index, code_num, beta = getBeta(ticker, "2018-09-19", "2019-03-19", '^KQ11')
#     row = []
#     row.append(index)
#     row.append(code_num)
#     row.append(beta)
#     df_list.append(row)

#     # 2019-03-20 ~ 2019-09-18
#     index, code_num, beta = getBeta(ticker, "2019-03-20", "2019-09-18", '^KQ11')
#     row = []
#     row.append(index)
#     row.append(code_num)
#     row.append(beta)
#     df_list.append(row)

#     # 2019-09-19 ~ 2020-03-19
#     index, code_num, beta = getBeta(ticker, "2019-09-19", "2020-03-19", '^KQ11')
#     row = []
#     row.append(index)
#     row.append(code_num)
#     row.append(beta)
#     df_list.append(row)

#     # 2019-03-20 ~ 2020-09-19
#     index, code_num, beta = getBeta(ticker, "2019-03-20", "2020-09-19", '^KQ11')
#     row = []
#     row.append(index)
#     row.append(code_num)
#     row.append(beta)
#     df_list.append(row)
    
# df = pd.DataFrame(df_list)
# df.to_csv('./kosdaq.csv', sep=',', na_rep='NaN')
# df.to_csv('./kosdaq_volume.csv', sep=',', na_rep='NaN')