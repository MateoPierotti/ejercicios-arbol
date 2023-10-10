# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:


from arbol_binario import BinaryTree
criaturas = BinaryTree()

lista = [
# Criaturas "Derrotado por" 
{'Criaturas': 'Ceto',"Derrotado por": "-"},{"Criaturas": "Cerda de Cromión","Derrotado por":"Teseo"},
{'Criaturas':"Tifón" ,"Derrotado por":"Zeus"},{"Criaturas": "Ortro" ,"Derrotado por":"Heracles"},
{'Criaturas':"Equidna" ,"Derrotado por":"Argos Panoptes" },{"Criaturas":"Toro de Creta" ,"Derrotado por":"Teseo"},
{'Criaturas':"Dino" ,"Derrotado por":"-" },{"Criaturas":"Jabalí de Calidón" ,"Derrotado por":"Atalanta"},
{'Criaturas':"Pefredo" ,"Derrotado por":"-" },{"Criaturas":"Carcinos" ,"Derrotado por":"-"},
{'Criaturas':"Enio" ,"Derrotado por":"-" },{"Criaturas":"Gerión" ,"Derrotado por":"Heracles"},
{'Criaturas':"Escila" ,"Derrotado por":"-"},{"Criaturas": "Cloto" ,"Derrotado por":"-"},
{'Criaturas':"Caribdis" ,"Derrotado por":"-" },{"Criaturas":"Láquesis" ,"Derrotado por":"-"},
{'Criaturas':"Euríale","Derrotado por": "-" },{"Criaturas":"Átropos" ,"Derrotado por":"-"},
{'Criaturas':"Esteno" ,"Derrotado por":"-" },{"Criaturas":"Minotauro de Creta" ,"Derrotado por":"Teseo"},
{'Criaturas':"Medusa","Derrotado por": "Perseo" },{"Criaturas":"Harpías" ,"Derrotado por":"-"},
{'Criaturas':"Ladón" ,"Derrotado por":"Heracles",},{"Criaturas":"Argos Panoptes" ,"Derrotado por":"Hermes"},
{'Criaturas':"Águila del Cáucaso" ,"Derrotado por":"-" },{"Criaturas":"Aves del Estínfalo" ,"Derrotado por":"-"},
{'Criaturas':"Quimera" ,"Derrotado por":"Belerofonte" },{"Criaturas":"Talos" ,"Derrotado por":"Medea"},
{'Criaturas':"Hidra de Lerna" ,"Derrotado por":"Heracles" },{"Criaturas":"Sirenas" ,"Derrotado por":"-"},
{'Criaturas':"León de Nemea" ,"Derrotado por":"Heracles" },{"Criaturas":"Pitón" ,"Derrotado por":"Apolo"},
{'Criaturas':"Esfinge" ,"Derrotado por":"Edipo" },{"Criaturas":"Cierva de Cerinea" ,"Derrotado por":"-"},
{'Criaturas':"Dragón de la Cólquida" ,"Derrotado por":"-" },{"Criaturas":"Basilisco" ,"Derrotado por":"-"},
{'Criaturas':"Cerbero","Derrotado por": "-" },{"Criaturas":"Jabalí de Erimanto","Derrotado por":"-"}]



for i in lista:
    criaturas.insert_node(i['Criaturas'], i['Derrotado por'], None, None)

# a. listado inorden de las Criaturas y quienes la derrotaron;
print("Punto A")
print('Inorden de las Criaturas y quienes la derrotaron')
print()
criaturas.inordenCriaturasDerrotados()
print()
# b. se debe permitir cargar una breve descripción sobre cada criatura;
def agregarDescripcion(criaturas, quien, mensaje):
    value1 = criaturas.search(quien)
    value1.tercer_values = mensaje
    criaturas.inordenCriaturasDerrotados()

# c. mostrar toda la información de la criatura Talos;
def infoDeTalos(criaturas):
    value1 = criaturas.search("Talos")
    print(f'Criatura: {value1.value} Derrotado por: {value1.other_values} descripcion: {value1.tercer_values} Capturado Por: {value1.cuarto_values}')

# h. modifique los nodos de las Criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
def agregarCapturado(criaturas):
    value = criaturas.search("Cerbero")
    value.cuarto_values = "Heracles"
    # 
    value1 = criaturas.search("Toro de Creta")
    value1.cuarto_values = "Heracles"
    # 
    value2 = criaturas.search("Cierva de Cerinea")
    value2.cuarto_values = "Heracles"
    # 
    value3 = criaturas.search("Jabalí de Erimanto")
    value3.cuarto_values = "Heracles"
    criaturas.inordenCriaturasDerrotados()


def buscarPorConcidencia(criaturas,quien):
    criaturas.search_by_quien(quien)




print("Punto B")
print('ingrese quien buscar')
hola= input()
print('ingrese descripcion para agregar')
hola1=input()
agregarDescripcion(criaturas, quien= hola, mensaje=hola1)
print("Punto C")
print('informacion de Talos')
infoDeTalos(criaturas)

#! d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de Criaturas;
print("Punto D")
dic_ranking = {}
criaturas.inorden_ranking(dic_ranking)
# print(dic_ranking)

def order_por(item):
    # print(item)
    return item[1]

ordenados = list(dic_ranking.items())
ordenados.sort(key=order_por, reverse=True)
print(ordenados[1:4])

# e. listar las Criaturas derrotadas por Heracles;
print("Punto E")
print("Criaturas derrotadas por Heracles")
criaturas.criaturasDerrotoHeracles()
# f. listar las Criaturas que no han sido derrotadas;}
print("Punto F")
print("Crituras no derrotadas")
criaturas.criaturasNoDerrotadas()
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
print("Punto G y H")
print('Se agrego los capturados por')
agregarCapturado(criaturas)
# i. se debe permitir búsquedas por coincidencia;
print("Punto I")
print('A quien desea Buscar?')
quienBusco = input()
buscarPorConcidencia(criaturas, quienBusco)
# j. eliminar al Basilisco y a las Sirenas;
print("Punto J")
criaturas.delete_node('Basilisco')
criaturas.delete_node('Sirenas')

# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
print("Punto K")
value = criaturas.search("Aves del Estínfalo")
value.cuarto_values = "Heracles"

# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
print("Punto L")
value1 = criaturas.search("Ladón")
value1.value = "Dragón Ladón"

# m. realizar un listado por nivel del árbol;
print("Punto M")
print("Listado by level")
criaturas.by_level()

# n. muestre las Criaturas capturadas por Heracles. 
print("Punto N")
print("Criaturas atrapadas por Heracles")
criaturas.search_capturados_Heracles()






