from docplex.mp.model import Model


model = Model(name='Problema Dieta')
X = model.integer_var(name='P') #Paquete de alimentos P
Y = model.integer_var(name='Q') #Paquete de alimentos Q

'''
|Paquete |Calcio|Hierro|Colesterol|Vita A|
|   P    |  12  |  4   |    6     |   6  |
|   Q    |  3   |  20  |    4     |   3  |


'''
#La función objetivo se basará en la columna de Vitamina A de la tabla de arriba: 
model.minimize(6*X + 3*Y)

#Las restricciones se basarán en los otros elementos de los alimentos, todos ellos están en 
model.add_constraint(12*X + 3*Y >= 240) #Restricción de calcio

model.add_constraint(4*X + 20*Y >= 460) #Restricción de hierro

model.add_constraint(6*X + 4*Y <= 300) #Restricción de colesterol


solucion = model.solve()
print('\n', '*'*40, '\n')
print(solucion)
print('*'*40, '\n')
print('Cantidad de alimento P:', X.solution_value)
print('Cantidad de alimento Q:', Y.solution_value)
print("Cantidad mínima de vitamina A: ", solucion.objective_value)