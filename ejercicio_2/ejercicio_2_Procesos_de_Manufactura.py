from docplex.mp.model import Model


model = Model(name='Procesos de Manufactura')

# La empresa fabrica dos modelos distintos. A y B
X = model.integer_var(name='A')
Y = model.integer_var(name='B')

# Quiero maximizar la ganancia. Esta está dada por la ganancia de 
# la primera pieza multiplicado por la ganancia de la segunda pieza
model.maximize(8000 * X + 12000 * Y)

# La restricción está dada por el límite de horas de fabricación y de acabado
# Las horas de fabricación son 180 y las de acabado son 30.

model.add_constraint(9 * X + 12 * Y <= 180)
model.add_constraint(1 * X + 3 * Y <= 30)


model.add_constraint(X>=0)
model.add_constraint(Y>=0)

solucion = model.solve()
print('\n', '*'*40, '\n')
print(solucion)
print('*'*40, '\n')
print('Cantidad de A:', round(X.solution_value))
print('Cantidad de B:', round(Y.solution_value))
print("La ganancia máxima por semana: $", solucion.objective_value)