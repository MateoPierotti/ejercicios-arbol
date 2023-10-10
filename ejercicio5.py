# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# se (MCU), desarrollar un algoritmo que contemple lo siguiente:











from arbol_binario import BinaryTree

personajesMarvel = BinaryTree()
herotree = BinaryTree()
villainstree = BinaryTree()
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
# leano que indica si es un héroe o un villano, True y False respectivamente;
def carga(personajesMarvel):
    cont = 0
    lista = [{'name': 'iron man', 'heroe': True},
    {'name': 'thanos', 'heroe': False},
    {'name': 'capitan america', 'heroe': True},
    {'name': 'red skull', 'heroe': False},
    {'name': 'hulk', 'heroe': True},
    {'name': 'black widow', 'heroe': True},
    {'name': 'rocket raccon', 'heroe': True},
    {'name': 'dotor strage', 'heroe': True},
    {'name': 'doctor octopus', 'heroe': True},
    {'name': 'deadpool', 'heroe': True},]
    for i in lista:
        personajesMarvel.insert_node(i['name'], i['heroe'])
# d. determinar cuántos superhéroes hay el árbol;
        if i ['heroe'] == True:
            cont += 1
    return cont
        

# b. listar los villanos ordenados alfabéticamente;
def ordenAlfabetico(personajesMarvel): 
    personajesMarvel.soloVillano()
# c. mostrar todos los superhéroes que empiezan con C;
def empiezaConC(personajesMarvel):
    personajesMarvel.alfabetoOrden()
    
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;

def DocStrange(personajesMarvel):
    value = personajesMarvel.search('dotor strage')
    if value:
        print('Se a encontrado la direccion')
        print(value.value, value.other_values)
        es_true = value.other_values
        personajesMarvel.delete_node('dotor strage')     
        personajesMarvel.insert_node('doctor strange', es_true)
        value1 = personajesMarvel.search('doctor strange')
        print('se reemplaso por: ')
        print(value1.value, value1.other_values)
    else:
        print('No se a encontrado la direccion')
    
    
    # 
    # {'nombre':'Doctor Extraño','heroe': True}
    # 
    
    # personajesMarvel.inorden()
# f. listar los superhéroes ordenados de manera descendente;
def list_order_false(personajesMarvel):
   personajesMarvel.postorden()
   
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
   
# I. determinar cuántos nodos tiene cada árbol;

# II. realizar un barrido ordenado alfabéticamente de cada árbol.
# def trees_deparados(personajesMarvel):
    # value = personajesMarvel.search(False)
    # print(value)
def dividirHeroVillano(personajesMarvel):
    personajesMarvel.divide_tree_h_v(herotree, villainstree)
    print('lista de heroes')
    herotree.inorden()
    print()
    print('lista de villanos')
    villainstree.inorden()

hola =  carga(personajesMarvel)
print()
print('----------------------------------------------------------------------')
print('Orden alfabetico de los villanos')
ordenAlfabetico(personajesMarvel)
print()
print('----------------------------------------------------------------------')
print('Super heroes que empiezan con C')
empiezaConC(personajesMarvel)
print()
print('----------------------------------------------------------------------')
print()
print(hola)
print()
print('----------------------------------------------------------------------')
print('doctor strange')
DocStrange(personajesMarvel)
print()
print('----------------------------------------------------------------------')
print()
list_order_false(personajesMarvel)
print()
print('----------------------------------------------------------------------')
print()
dividirHeroVillano(personajesMarvel)