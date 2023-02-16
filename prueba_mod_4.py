# -*- coding: utf-8 -*-
""" Script para practicar con listas y diccionarios. Hay que asiganar aleatoriamente un color de la lista
de colores a los usuarios de la lista de usuarios que contiene diccionarios."""

import random
import time


colores= ['amarillo', 'azul', 'verde', 'rojo']
usuarios = [{'Nombre': 'Josep'}, {'Nombre': 'Claudio'}, {'Nombre': 'Isabel'}, {'Nombre': 'Sheila'}]

def añadir_colores():
    """Añade un nuevo color a la lista comprobando que no existe"""
    global colores
    new_color= input("Añade un nuevo color a la lista: ")
    new_color=new_color.lower()
    new_color=new_color.strip()
    new_color_sin_espacios = new_color.replace(" ","")   
    
    if (new_color in colores):
        print("Este color ya existe, elija uno que no esté en la lista")
        añadir_colores()
    elif not(new_color_sin_espacios.isalpha()):
        print("El nombre del nuevo color no debe de contener números")
        añadir_colores()
    else:
        colores.append(new_color)
    
    return True

def mostrar_colores():
    """Imprime la lista de colores"""
    global colores
    print("\nEsta es la lista de colores: ")
    for i in colores:
        print(i)
    print("\n")
    time.sleep(2)
    
    return True

def ordenar_colores():
    """Ordena los colores alfabéticamente"""
    global colores
    colores.sort()
    print("Esta la lista de colores ordenados alfabéticamente:  ")
    
    for i in colores:
        print(i)
        
    time.sleep(1)
    return True

def añadir_usuario():
    """Añade un nuevo usuario a la lista"""
    global colores
    global usuarios
    
    # Verifica si la lista de usuarios y colores coinciden
    if (len(colores)<=len(usuarios)):
        print("Debe de añadir un color antes de añadir un usuario")
        añadir_colores()
        añadir_usuario()
    else:
        new_usuario= input("introduzca el nombre del nuevo usuario: ")
        new_usuario=new_usuario.strip()
        new_usuario_sin_espacios = new_usuario.replace(" ","") 
        if not(new_usuario_sin_espacios.isalpha()):
            print("El nombre del usuario solamente puede tener letras")
            añadir_usuario()
        else:
            new_usuario = new_usuario.title()
            usuarios.append({'Nombre': new_usuario})
    

    return True

def asignar_colores():
    """Hace la asignación aleatoria de colores a ususarios"""
    global usuarios
    global colores
    new_list_usuarios= usuarios

    new_list_colores=[]
    listado_numeros=[]
    contador = 0
    n = len(colores)-1

    while contador<len(colores):
        numero_random = random.randint(0,n)
        if numero_random in listado_numeros:
            pass
        else:
            listado_numeros.append(numero_random)
            contador +=1
            
    for i in listado_numeros:
        new_list_colores.append(colores[listado_numeros[i]])
        
    new_list_dic_colores = []
    
    for i in range(0,len(new_list_colores)):
        dict1= {}
        dict1['Color'] = new_list_colores[i]
        new_list_dic_colores.append(dict1)
        
    for i in range(0,len(new_list_usuarios)):
        new_list_usuarios[i].update(new_list_dic_colores[i]) 

    for elemento in new_list_usuarios:
        print(" \n Colores por usuario", end=" -->")
        for values in elemento.values():
            print(values, end=" ")
            
    print("\n")
    
    return True

def eliminar_usuario():
    """Elimina usuario de la lista"""
    global usuarios
       
    for elemento in usuarios:
        try:
            del elemento['Color']
        except KeyError:
            continue

    print("Elija un número para borrar un usuario: ")
    i=1       
    for elemento in usuarios:
        for v in elemento.values():
            print( i,")", v)
            i +=1
   
    try:
        num=int(input())
        user_borrado = {}
        user_borrado.update(usuarios.pop(num-1))
        for j in user_borrado.values():
            print("El usuario elminado es:", j)
        
    except:
        print("Debe elegir un usuario de la lista")
        eliminar_usuario()

    return True

def mostrar_usuario():
    """Muestra los usuarios de la lista"""
    global usuarios
    
    print("Estos son los nombres de los usuarios: ")
           
    for elemento in usuarios:
        for k,v in elemento.items():
            if k == 'Color':
                continue
            else:
                print(v)
    print("\n")  
    time.sleep(1)    
    
    return True

def salir():
    print("Gracias por jugar. Hasta pronto")
    
    return False 

def switch(opcion):
    menu = {
        '1' : 'añadir_colores()',
        '2' : 'mostrar_colores()',
        '3' : 'ordenar_colores()',
        '4' : 'añadir_usuario()',
        '5' : 'asignar_colores()',
        '6' : 'eliminar_usuario()',
        '7' : 'mostrar_usuario()',
        '8' : 'salir()'
    }
    return eval(menu.get(opcion))

continuar = True

while(continuar):
    print('''Seleccione una opción:
    1) Añadir colores
    2) Mostar listado de colores
    3) Ordenar listado de colores
    4) Añadir usuarios
    5) Asignar colores a usuarios
    6) Eliminar usuarios
    7) Mostar nombre de usuarios
    8) Salir''')
    opcion=input()
    try:
       continuar = switch(opcion)
               
    except Exception as a:
        print(a)
