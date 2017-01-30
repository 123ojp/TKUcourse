import requests
import sys

from bs4 import BeautifulSoup
head = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
s = requests.Session()
ad = s.get('http://delhi-court-4677.pancakeapps.com',verify=False,headers=head)
ad1 = ad.text
soup1 = BeautifulSoup(ad1, "html.parser")

ad2 = soup1.find('input', {'name': "__VIEWSTATEGENERATOR"})['value']
print ad2
print "本系統不幫忙檢查課程代號是否正確"
print "若選課失敗，本系統不負任何責任"
print "作者：逢甲大學的某個人呵 by123"
print "按ctrl+c結束程式"


#帳密----------------------------------------------


id1=input("請輸入學號")

pas1=raw_input("請輸入密碼")

#建立選課清單 corse0 -----------------------------

corsenum=int(input("請輸入要選幾項課程"))
corse0=[]
for x in range (corsenum):
 print "請輸入第",
 print x+1,
 print "個選課代碼"
 corsetemp = raw_input()
 corse0.append(corsetemp)

#登入----------------------------------------------
rtrue1=4001 #此為未到選課時間變數
logcont = 0 #重試次數變數

payload={
     '__EVENTTARGET':'btnLogin',
     '__EVENTARGUMENT':'',
     '__VIEWSTATE':'/wEPDwULLTE0ODk3NTI0NDMPZBYCAgMPZBYSAgMPDxYCHgRUZXh0BS4xMDUg5a245bm05bqm56ysIDEg5a245pyfIC0g5pyf5Lit6ICD5b6M6YCA6YG4ZGQCBA8PFgIfAGVkZAIMDw9kFgIeB29uY2xpY2sFOWphdmFzY3JpcHQ6dGhpcy5kaXNhYmxlZD10cnVlO19fZG9Qb3N0QmFjaygnYnRuTG9naW4nLCcnKWQCDg8WAh8ABboBIOiri+i8uOWFpeWtuOiZn+WPiuWvhueivC4uLjxmb250IHN0eWxlPSJDT0xPUjogcmVkOyBmb250LXdlaWdodDogYm9sZCI+KOOAjOa3oeaxn+Wkp+WtuOWWruS4gOeZu+WFpShTU08p44CN5Zau5LiA5biz5a+G6amX6K2J5a+G56K8O+mgkOioreeCuui6q+WIhuitieaIluWxheeVmeitieW+jO+8lueivCkgPGJyLz48L2ZvbnQ+ZAIQDxYCHwAFtQE8Zm9udCBmYWNlPSLmqJnmpbfpq5QiIHNpemU9IjQiPjcu5pyf5Lit6YCA6YG45q+P5a245pyf5Lul5LqM56eR54K66ZmQ77yM5LiU6YCA6YG45b6M5LiN5b6X5L2O5L+uKOiri+ips+acrOagoeWtuOeUn+acn+S4remAgOmBuOWvpuaWveimgem7ninvvIzoq4vlr6nmhY7opo/lioPpgbjoqrLjgII8L2ZvbnQ+PGJyIC8+ZAISDxYCHwAFpAE8Zm9udCBmYWNlPSLmqJnmpbfpq5QiIHNpemU9IjQiPjgu6YC+5a245pyf5LiK6Kqy6YGU5LiJ5YiG5LmL5LiA5pmC5aeL6YCA6YG477yM5L6d6KaP5a6a5oeJ57mz5Lqk5LmL5a245YiG6LK75LiN5LqI6YCA6YKE77yM5pyq57mz5a245YiG6LK76ICF5oeJ5LqI6KOc57mz44CCPC9mb250PmQCFA8WAh8AZWQCFg8WAh8ABY4BPGZvbnQgZmFjZT0i5qiZ5qW36auUIiBzaXplPSI0Ij4zLuacrOezu+e1seWPquaPkOS+m+acn+S4remAgOmBuOiqsueoi+aJgOmcgCzlhbblroPpgbjoqrLnm7jpl5zlip/og70s6KuL6Iez55u46Zec57ay56uZ5L2/55So44CCPC9mb250PjxiciAvPmQCGA8PFgIfAAUOMTE5Ljc3LjI0Ny4xODFkZGRtjXYQQTWum7JanefGKqjqhvxCBg==',
     '__VIEWSTATEGENERATOR':'F118B446',
     '__EVENTVALIDATION':'/wEWBAKJ8KGcBQKA7M65CgL79NvIBAKC3IeGDI/697GiPetWz2VTDQssweceNGjX',
     'txtStuNo':(id1),
     'txtPSWD':(pas1)
     }

while rtrue1 >= 4000:
 d = s.post("http://www.ais.tku.edu.tw/elecos/login.aspx",verify=False, data=payload)
 #print(d.text)
 h = d.text#.encode('utf-8')
 #print h.find("E9")
 rtrue = int(h.find("E9"))
 rtrue1 = int(h.find("E051"))
 rture2 = int(h.encode('utf-8').find("請重新輸入"))
 #print  rtrue1
 
    
    #判定 登入失敗-------------------------------------------
 if rtrue > 0 and rtrue1<4000 and rture2>0:
  errorcode = h[rtrue]+h[rtrue+1]+h[rtrue+2]+h[rtrue+3]
  print "登入錯誤代碼：",
  print errorcode

  input("輸入任意值結束程式")
  sys.exit(0)
  
  
 if rtrue1 >= 4000:
  
  print "未到選課時間 系統正在為您重新登入 重試次數",
  print logcont
  logcont = logcont+1
 #找不到就會結束迴圈


 #尋找登入成功的關鍵字
 logsucess = h.encode('utf-8').find("一經退選")
 if logsucess > 0 :
  print "登入成功"
#此開始寫搶客



soup = BeautifulSoup(h, "html.parser")

VIEWSTATE = soup.find('input', {'name': "__VIEWSTATE"})['value']
VIEWSTATEGENERATOR = soup.find('input', {'name': "__VIEWSTATEGENERATOR"})['value']
EVENTVALIDATION = soup.find('input', {'name': "__EVENTVALIDATION"})['value']





for x in range (corsenum):  
 print "正在進行代號"+(corse0[x])+"課程"
 payloadgo={
     '__EVENTTARGET':'btnAdd',
     '__EVENTARGUMENT':'',
     '__VIEWSTATE':(VIEWSTATE),
     '__VIEWSTATEGENERATOR':(VIEWSTATEGENERATOR),
     '__EVENTVALIDATION':(EVENTVALIDATION),
     'txtCosEleSeq':(corse0[x])
     }
 corget = s.post("http://www.ais.tku.edu.tw/elecos/action.aspx",verify=False, data=payloadgo) #開搶
 coryes = corget.text.encode('utf-8').find("加選成功")
 if coryes > 1 :
  print "搶課成功"
 else :
  print "搶課失敗"
 #print "進行下一項課程"
 
print "搶課系統結束 請至網站再次確認您的課程"
input("輸入任意值離開")
