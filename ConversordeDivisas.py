'''
Created on 4 dic. 2017

@author: Rebcesp

'''



def menu():
    print("############CONVERSOR DE DIVISAS############")
    print("1.Dolar")
    print("2.Dolarn Canadiense")
    print("3.Euro")
    print("############CONVIERTE RAPIDO############")
    print("Cuanto tienes en Pesos Bolivianos")

    
    global bs
    bs = float(input()) #De tipo float
    
    print("Que tipo de cambio deseas realizar")
    
    cambio = int(input())
    
    if(cambio==1):
        dolares() #Llamamos a la funcion dolares()
    elif(cambio==2):
        dolares_can()
    elif(cambio==3):
        euros()
    else:
        print("Has seleccionado un numero no VALIDO")
        print("Quieres volver a convertir (si/no)")
    
    global resp
    resp = input()
    otravez()
        
    
#Defininimos funcion dolares 
def dolares():
    print("Cual es el precio del dolar de Hoy")#7
    precio_dolar = float(input())
    global dinero #Declaramos GLOBAL para poder usarla fuera de la funcion
    dinero = bs/precio_dolar
    
    print("Tienes "+str(dinero)+" Dolares")
     
#Definiendo dolares canadienses 
def dolares_can():
    print("Cual es el precio del dolar Canadiense de Hoy")#5,44
    precio_can = float(input())
    dinero = bs/precio_can
    
    print("Tienes "+str(dinero)+" Dolares Canadienses")
    
def euros():
    print("Cual es el precio del euro de Hoy")#9
    euro = float(input())
    dinero = bs/euro
    
    print("Tienes "+str(dinero)+" Euros")
    
def otravez():
    
    while(resp!="no"): #Si la respuesta es diferente a no 
        menu()

#Llamando a la funcion Menu 
menu()