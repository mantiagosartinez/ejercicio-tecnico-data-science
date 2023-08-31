from docplex.mp.model import Model


model = Model(name='Aplicación Herbicidas')
X = model.integer_var(name='X')
Y = model.integer_var(name='Y')
model.maximize(10500*X + 9000*Y)
model.add_constraint(20*X + 10*Y <= 800)

# Se deben producir al menos 100 kilogramos de filete.
model.add_constraint(X+Y==50)

# El número de kilogramos de rib-eye producido no debe exceder el doble del número de kilogramos de chuletón producido
model.add_constraint(Y>=0)
model.add_constraint(X>=0)

solucion = model.solve()
print('\n', '*'*40, '\n')
print(solucion)
print('*'*40, '\n')
print('Cantidad de cultivo X:', X.solution_value)
print('Cantidad de cultivo Y:', Y.solution_value)
print("Cantidad de ganancia máxima: $", solucion.objective_value)