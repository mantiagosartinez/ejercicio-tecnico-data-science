from docplex.mp.model import Model


model = Model(name='Aplicación Herbicidas')

#Tenemos dos tipos de cultivo: Cultivo X y Cultivo Y
X = model.integer_var(name='X')
Y = model.integer_var(name='Y')

model.maximize(10500*X + 9000*Y)

# Las restricciones dependen de:
# que no se pueda usar más de 800 litros de herbicida

model.add_constraint(20*X + 10*Y <= 800)

# de que en total hay 50 hectareas
model.add_constraint(X+Y<=50)

model.add_constraint(Y>=0)
model.add_constraint(X>=0)

solucion = model.solve()
print('\n', '*'*40, '\n')
print(solucion)
print('*'*40, '\n')
print('Cantidad de cultivo X:', round(X.solution_value))
print('Cantidad de cultivo Y:', round(Y.solution_value))
print("Cantidad de ganancia máxima: $", round(solucion.objective_value))