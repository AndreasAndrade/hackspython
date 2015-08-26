# coding: utf-8
import sys

print sys.stdout.encoding # mostra qual o encoding utilizado pelo shell

s = 'ã'
enc = s.decode('utf-8') # transforma a string em unicode e salva na variável enc
# enc = s.encode('latin-1') 
enc = enc.encode('cp850') # passa de unicode para o encoding cp850
#enc = enc.encode('cp850') # encoding do prompt

print s
# print ord(s)

print enc