import nltk, re, pprint
from nltk.tokenize import word_tokenize
from urllib import request
from bs4 import BeautifulSoup
import pandas as pd
import random
import requests
import re    # to extract table with regex
from selenium import webdriver
import time

datelist = ['2019/03/01', '2019/09/01', '2020/03/01', '2020/09/01']
per_company = []

def sele (link):
    browser = webdriver.Chrome('/Users/na/Downloads/chromedriver')
    browser.get(link)
    
    time.sleep(3) # 페이지 로딩 먼저 5초 대기

    thead = browser.find_elements_by_tag_name('thead')
    print (thead[0].text.split()[2:])
    sub = lambda x : float(x[:-1])
    per_options = list(map(sub,thead[0].text.split()[2:]))
    print (per_options)
    rows = browser.find_elements_by_tag_name('tr')
    for index, value in enumerate(rows):
        if index == 0:
          continue # pass for the top header

        # now collect data
        date=value.find_elements_by_tag_name("th")[0].text
        # print (date.text)
        body=value.find_elements_by_tag_name("td")
        if (len(body) < 6):
          print ("data not enough!")
          continue
        # print (body[0].text)
        try: price = int(body[0].text.replace(',','')) #수정주가
        except Exception as e:
          print (e)
          continue
        # print (body[1].text)
        try: op1 = float(body[1].text.replace(',',''))
        except Exception as e:
          print (e)
          continue
        try: op2 = float(body[2].text.replace(',',''))
        except Exception as e:
          print (e)
          continue
        try: op3 = float(body[3].text.replace(',',''))
        except Exception as e:
          print (e)
          continue
        try: op4 = float(body[4].text.replace(',',''))
        except Exception as e:
          print (e)
          continue
        try: op5 = float(body[5].text.replace(',',''))
        except Exception as e:
          print (e)
          continue
        # print(price.text, op1.text, op2.text, op3.text, op4.text, op5.text )

        
        # next, check for date we want
        if (date == '2019/03/01'):
          per = 0
          if (price < op1):
            per = per_options[0] * price / op1
          elif (price < op2):
            per = (per_options[1] - per_options[0]) * (price - op1) / (op2 - op1) + per_options[0]
          elif (price < op3):
            per = (per_options[2] - per_options[1]) * (price - op2) / (op3 - op2) + per_options[1]
          elif (price < op4):
            per = (per_options[3] - per_options[2]) * (price - op3) / (op4 - op3) + per_options[2]
          elif (price < op5):
            per = (per_options[4] - per_options[3]) * (price - op4) / (op5 - op4) + per_options[3]
          else:
            per = per_options[4] * price / op5
          
          per_company.append(per)

        if (date == '2019/09/01'):
          per = 0
          if (price < op1):
            per = per_options[0] * price / op1
          elif (price < op2):
            per = (per_options[1] - per_options[0]) * (price - op1) / (op2 - op1) + per_options[0]
          elif (price < op3):
            per = (per_options[2] - per_options[1]) * (price - op2) / (op3 - op2) + per_options[1]
          elif (price < op4):
            per = (per_options[3] - per_options[2]) * (price - op3) / (op4 - op3) + per_options[2]
          elif (price < op5):
            per = (per_options[4] - per_options[3]) * (price - op4) / (op5 - op4) + per_options[3]
          else:
            per = per_options[4] * price / op5
          per_company.append(per)
          

        if (date == '2020/03/01'):
            per = 0
            if (price < op1):
              per = per_options[0] * price / op1
            elif (price < op2):
              per = (per_options[1] - per_options[0]) * (price - op1) / (op2 - op1) + per_options[0]
            elif (price < op3):
              per = (per_options[2] - per_options[1]) * (price - op2) / (op3 - op2) + per_options[1]
            elif (price < op4):
              per = (per_options[3] - per_options[2]) * (price - op3) / (op4 - op3) + per_options[2]
            elif (price < op5):
              per = (per_options[4] - per_options[3]) * (price - op4) / (op5 - op4) + per_options[3]
            else:
              per = per_options[4] * price / op5
            per_company.append(per)

        if (date == '2020/09/01'):
            per = 0
            if (price < op1):
              per = per_options[0] * price / op1
            elif (price < op2):
              per = (per_options[1] - per_options[0]) * (price - op1) / (op2 - op1) + per_options[0]
            elif (price < op3):
              per = (per_options[2] - per_options[1]) * (price - op2) / (op3 - op2) + per_options[1]
            elif (price < op4):
              per = (per_options[3] - per_options[2]) * (price - op3) / (op4 - op3) + per_options[2]
            elif (price < op5):
              per = (per_options[4] - per_options[3]) * (price - op4) / (op5 - op4) + per_options[3]
            else:
              per = per_options[4] * price / op5
            per_company.append(per)
    
    
    browser.quit() # 브라우저 종료
    return per_company

link = "https://comp.fnguide.com/SVO2/common/chartListPopup2.asp?oid=perBandCht&cid=01_06&gicode=A243070&filter=D&term=Y&etc=E&etc2=0&titleTxt=PER%20Band&dateTxt=undefined&unitTxt="
percompany = sele(link)
print ("---------------------------")
for each in percompany:
  print (each)

print ("---------------------------")
