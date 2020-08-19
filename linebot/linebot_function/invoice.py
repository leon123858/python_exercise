# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 17:14:00 2020

@author: a0970
"""
import requests
import xml.etree.cElementTree as ET

class invoice():
 def __init__(self,uri):
     content = requests.get(uri)
     tree = ET.fromstring(content.text)
     self.now = [];
     self.before1 = [];
     self.before2 = [];
     items = list(tree.iter(tag = 'item'))
     self.now.append(items[0][0].text)
     self.before1.append(items[1][0].text)
     self.before2.append(items[2][0].text)
     string = items[0][2].text.replace('</p><p>','：').replace('、', '：').replace('</p>', '：').split('：')
     tmp = [string[1],string[3],string[5],string[6],string[7],string[9]]
     self.now.extend(tmp)
     string = items[1][2].text.replace('</p><p>','：').replace('、', '：').replace('</p>', '：').split('：')
     tmp = [string[1],string[3],string[5],string[6],string[7],string[9]]
     self.before1.extend(tmp)
     string = items[2][2].text.replace('</p><p>','：').replace('、', '：').replace('</p>', '：').split('：')
     tmp = [string[1],string[3],string[5],string[6],string[7],string[9]]
     self.before2.extend(tmp)
 def getstr(self,list):
     string = '期數: ' + list[0] + '\n特別獎: ' + list[1] + '\n特獎: ' + list[2] + '\n頭獎: ' + list[3] +'、' +list[4]+'、' +list[5]+ '\n增開6獎: ' +list[6]
     return string
 def On_invoice(self,num,which):
     for i in range(1,7):
         if which[i].find(num) == 5 or (which[i].find(num) == 0 and len(which[i]) == 3):
             return '你在這期有後三碼一樣喔,請你自己對一下\n' + self.getstr(which) + '\n'
     return ''
 def On_invoices(self,num):
     op = ''+self.On_invoice(num,self.now) + self.On_invoice(num,self.before1) + self.On_invoice(num,self.before2);
     if  op == '':
         return '你沒中獎!'
     else :
         return op
