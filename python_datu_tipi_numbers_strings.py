#15/01/2026

#Viena rinda
"""
Vairāku rindu
komentārs
"""

# Teksts komentārā automātiski - ctrl+k+c

#Python datu tipi: Numbers un String

#Numbers - skaitļi

"""
✍️ Praktiskais uzdevums
Definē divus skaitļus
Veic četras matemātiskās darbības ar tiem - +,-,/,*
Izvadi katru rezultātu, 
"""


#Nosaukumi mainīgajiem - vienmēr latviski (bez garumzīmēm, bet mīkstinājuma zīmēm)


#Definē divus skaitļus
skaitlis1 = 5 #integer - vesels skaitlis
skaitlis2 = 4.5 #float - decimālskaitlis
#funkcija print()
print(skaitlis1)
print(skaitlis2)

# Veic četras matemātiskās darbības ar tiem - +,-,/,*
darbiba1 = skaitlis2+skaitlis1 #float
print(darbiba1)
print(skaitlis1-skaitlis2)
print(skaitlis1/skaitlis2)
print(skaitlis1*skaitlis2)

#String - teksts/simbolu virkne

"""
✍️ Praktiskais uzdevums
Definē divus teksta mainīgos
Izvadi tos atsevišķi un kopā
Nosaki simbolu skaitu
Apgriez tekstu otrādāk
Izvadīt 1 teksta simbolu
Izvadīt 2 un 3 teksta simbolu
"""

# Definē divus teksta mainīgos
teksts1 = "7"
teksts2 = "gadi"

#Izvadi tos atsevišķi un kopā
print(teksts1)
print(teksts2)
#teksta savienošana: + un ,
print(teksts1+teksts2)
print(teksts1+" "+teksts2)
print(teksts1,teksts2)

# Nosaki simbolu skaitu
print(len(teksts1)) #funkcija len
print(len(teksts2))

#Izvadīt 1 teksta simbolu
#gadi
#indeksi
#gadi
#0123 #indeksi
print(teksts2[0])

#Izvadīt 2 un 3 teksta simbolu
print(teksts2[1:3]) #3=i 1,2

# Apgriez tekstu otrādāk
print(teksts2[::-1])
