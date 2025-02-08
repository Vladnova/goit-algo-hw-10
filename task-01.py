from pulp import LpMaximize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD

# Створюємо модель оптимізації
model = LpProblem(name="maximize_drinks_production", sense=LpMaximize)

# Змінні рішення
lemonade = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")

# Функція цілі: максимізація загальної кількості вироблених напоїв
model += lemonade + fruit_juice, "Total_Production"

# Обмеження ресурсів
model += (2 * lemonade + fruit_juice <= 100, "Water_Constraint")  # Вода
model += (1 * lemonade <= 50, "Sugar_Constraint")  # Цукор
model += (1 * lemonade <= 30, "Lemon_Juice_Constraint")  # Лимонний сік
model += (2 * fruit_juice <= 40, "Fruit_Puree_Constraint")  # Фруктове пюре

# Розв'язуємо задачу без виводу додаткової інформації
model.solve(PULP_CBC_CMD(msg=False))

# Виводимо результати
print(f"Оптимальна кількість Лимонаду: {lemonade.varValue}")
print(f"Оптимальна кількість Фруктового соку: {fruit_juice.varValue}")
