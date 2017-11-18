'''
Created on 18 nov. 2017

@author: Rebcesp
'''

#Validacion de Usuarios 
usuario=False
validar = True


print("Validar Usuario")

print("Introduce un usuario\n")


usuario = input()

if(len(usuario) < 6):
    usuario = True
    print("Necesita que sea mayor a 6 caracteres")
    
elif(len(usuario) > 12):
    usuario = True
    print("No puede conetener mas de de 12 caracteres")

elif(usuario.isalpha()):
    usuario = True
    print("El nombre debe contener numeros y letras")
    
else:
    while (validar):
        print("Usuario Valido")
        break
     
#Ejerciccio validacionde contraseña

mayuscula=False
minuscula= False
noalpha= False
espacio=False
numero=False

password=False

print("Validacion para contraseñas")

print("Introduce una contraseña, debe contener mayuscula, minuscula , alfanmerico, y que no contenga espacio")

password = input()
if(len(password)<8):
    print("El nombre debe contener mas de 8 caracteres")
    

#elif(' ' in password):
 #   print("la contraseña no puede contener espacios")

else:
    for i in password:
        if(i.isupper()): 
           mayuscula = True #Tiene que haber una mayuscula
        elif(i.islower()):
            minuscula = True  
        elif(i.isspace()):
            espacio = True
        elif(i.isdigit()):
            numero   = True
        elif(i.isalpha() == False):
            noalpha  = True

    if(mayuscula == True and minuscula == True and espacio == False and numero == True and noalpha == True):
        print("Contraseña valida")
    else:
        print("No valida")
        if(mayuscula == False):
            print("Debe contener mayuscula")
        elif(minuscula == False):
            print("Debe contener minuscula")
        elif(espacio == True):
            print("No debe contener espacio")
        elif(numero == True):
            print("Tiene que contener numero")
        elif(noalpha == True):
            print("Debe contener algun caracter alfanumerico")
        
        
        
   
    
    
    




            
        
  
    

