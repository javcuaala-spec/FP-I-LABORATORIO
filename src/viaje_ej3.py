edad=int(input("Introduce tu edad"))
fisic=int(input("Introduce tu nivel fisico del 1 al 10"))
while fisic<0 or fisic>10:
    fisic=int(input("Introduce tu nivel fisico en el rango indicado"))
if edad<18:
        print("Debe ser mayor de edad")
elif fisic<5:
        print("Debes estar mejor en forma")
else:
    print("Listo para despegar")
