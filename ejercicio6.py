from arbol_binario import BinaryTree, get_value_from_file

# 6. Dado un archivo con todos los Jedi, de los que se cuenta con: nombre, especie, año de naci-
# miento, color de sable de luz, ranking (Jedi Master, Jedi Knight, Padawan) y maestro, los últimos
# tres campos pueden tener más de un valor. Escribir las funciones necesarias para resolver las
# siguientes consignas:





file_jedi = open('arbol/jedis.txt')
read_lines = file_jedi.readlines()
file_jedi.close()

name_tree = BinaryTree()
specie_tree = BinaryTree()
ranking_tree = BinaryTree()


# a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
def threeTrees(read_lines):
    read_lines.pop(0)
    for index, linea_jedi in enumerate(read_lines):
        jedi = linea_jedi.split(';')
        jedi.pop() 
        name_tree.insert_node(jedi[0], index+2)
        specie_tree.insert_node(jedi[2], index+2)
        ranking_tree.insert_node(jedi[1], index+2)
    
    
    
# b. realizar un barrido inorden del árbol por nombre y ranking;
def inordenTrees(name_tree, ranking_tree):
    print('inorden de nombre')
    name_tree.inorden()
    print()
    print('inorden del ranking')
    ranking_tree.inorden()
    print()

# c. realizar un barrido por nivel de los árboles por ranking y especie;
def byLevelRankingEspecie(specie_tree, ranking_tree):
    print('ByLevel del ranking')
    ranking_tree.by_level()
    print()
    print('ByLevel del especie')
    specie_tree.by_level()

# d. mostrar toda la información de Yoda y Luke Skywalker;
def infoByYodaAndLuke(name_tree):
    value = name_tree.search('yoda')
    if value is not None:
        print('info de yoda')
        print(get_value_from_file('jedis.txt', value.other_values))
    value1 = name_tree.search('luke skywalker')
    if value1 is not None:
        print('info de luke skywalker')
        print(get_value_from_file('jedis.txt', value1.other_values)) 
   
# e. mostrar todos los Jedi con ranking “Jedi Master”;
def mostrarJediMaster(ranking_tree):
    print('Estos son los Jedi Master')
    ranking_tree.mostrarJedisMaster('jedis.txt')

# f. listar todos los Jedi que utilizaron sabe de luz color verde;

def callMethodLightGreen(name_tree):
    print()
    print('Jedis con sable de luz verde')
    print()
    name_tree.listarLightGreen('jedis.txt')

# g. listar todos los Jedi cuyos maestros están en el archivo;

def mostrarMasterJedis(name_tree):
    print('JEDI CON MAESTROS ')
    name_tree.agregoMaestros('jedis.txt')
   
 



# # name_tree.inorden()
# print()

# ranking_tree.inorden_file('jedis.txt')
# print(get_value_from_file('jedis.txt', index))
# print()
# ranking_tree.by_level()
# print()
# specie_tree.by_level()

# pos = name_tree.search('yoda')
# if pos:
#     print(get_value_from_file('jedis.txt', pos.other_values))
# else:
#     print('no esta en la lista')

# print()

# # name_tree.inorden_file_lightsaber('jedis.txt', 'green')

# name_tree.inorden_start_with_jedi('A')


threeTrees(read_lines)

inordenTrees(name_tree, ranking_tree)

byLevelRankingEspecie(specie_tree, ranking_tree)

infoByYodaAndLuke(name_tree)

mostrarJediMaster(ranking_tree)

callMethodLightGreen(name_tree)
print()
mostrarMasterJedis(ranking_tree)
print()
# h. mostrar todos los Jedi de especie “Togruta” o “Cerean” ;
print('Jedi de especie “Togruta” o “Cerean”')
name_tree.especieTogrutaCerean('jedis.txt')
print()
# i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.
print('Empieza con A o contiene -')
name_tree.conAoConGuion('jedis.txt')



