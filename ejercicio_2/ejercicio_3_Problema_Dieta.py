from docplex.mp.model import Model

# Este ejercicio cuenta con un error en el enunciado.
# Dice que cada paquete pesa 30g. El paquete Q si suma 30g entre todos sus componentes
# Pero el paquete P solo suma 28g.

# De todas formas esto no cambia la resolución del ejercicio. Solo habria que modificar 
# el valor de la restricción según el valor correcto


model = Model(name='Problema Dieta')
X = model.integer_var(name='P') # Paquete de alimentos P
Y = model.integer_var(name='Q') # Paquete de alimentos Q

'''
|Paquete |Calcio|Hierro|Colesterol|Vita A|
|   P    |  12  |  4   |    6     |   6  |
|   Q    |  3   |  20  |    4     |   3  |


'''
# La función objetivo se basará en la columna de Vitamina A de la tabla de arriba: 
model.minimize(6*X + 3*Y)

# Las restricciones se basarán en los otros elementos de los alimentos, todos ellos están en 
model.add_constraint(12*X + 3*Y >= 240) # Restricción de calcio

model.add_constraint(4*X + 20*Y >= 460) # Restricción de hierro

model.add_constraint(6*X + 4*Y <= 300) # Restricción de colesterol


model.add_constraint(X>=0)
model.add_constraint(Y>=0)

solucion = model.solve()
print('\n', '*'*40, '\n')
print(solucion)
print('*'*40, '\n')
print('Cantidad de alimento P:', round(X.solution_value))
print('Cantidad de alimento Q:', round(Y.solution_value))
print("Cantidad mínima de vitamina A: ", solucion.objective_value)