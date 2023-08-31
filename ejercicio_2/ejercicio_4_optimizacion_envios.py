from docplex.mp.model import Model


model = Model(name='Optimización envíos')
PA = model.integer_var(name='PA') #unidades transportadas de la fábrica P al deposito A
PB = model.integer_var(name='PB') #unidades transportadas de la fábrica P al deposito B
PC = model.integer_var(name='PC') #unidades transportadas de la fábrica P al deposito C
QA = model.integer_var(name='QA') #unidades transportadas de la fábrica Q al deposito A
QB = model.integer_var(name='QB') #unidades transportadas de la fábrica Q al deposito B
QC = model.integer_var(name='QC') #unidades transportadas de la fábrica Q al deposito C


#Dado que lo que quiero minimizar son los costos, 
# defino la suma de los gastos como función objetivo

model.minimize(160*PA + 100*PB + 150*PC + 100*QA + 120*QB + 100*QC)

# Agrego las restricciones de cada fábrica 
model.add_constraint(PA+PB+PC ==8)

model.add_constraint(QA+QB+QC ==6)

# Agrego las restricciones de los depositos
model.add_constraint(PA+QA == 5)
model.add_constraint(PB+QB == 5)
model.add_constraint(PC+QC == 4)


solucion = model.solve()
print('\n', '*'*40, '\n')
print(solucion)
print('*'*40, '\n')
print('Cantidad de unidades transportadas de la fábrica P al deposito A:', round(PA.solution_value))
print('Cantidad de unidades transportadas de la fábrica P al deposito B:', round(PB.solution_value))
print('Cantidad de unidades transportadas de la fábrica P al deposito C:', round(PC.solution_value))
print('Cantidad de unidades transportadas de la fábrica Q al deposito A:', round(QA.solution_value))
print('Cantidad de unidades transportadas de la fábrica Q al deposito B:', round(QB.solution_value))
print('Cantidad de unidades transportadas de la fábrica Q al deposito C:', round(QC.solution_value))

print("Costo mínimo del transporte: $", solucion.objective_value)