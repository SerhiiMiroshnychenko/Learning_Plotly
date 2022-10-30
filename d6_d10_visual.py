from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Створити кубики D6 та D10
die_1 = Die()
die_2 = Die(10)

# Зробити декілька кидків та зберегти результати в список
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Проаналізуємо результати
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Візуалізувати результати
x_values = list(range(2, max_result+1))  # Список, що зберігає всі стовпчики
data = [Bar(x=x_values, y=frequencies)]  # Клас Bar представляє набір даних
# на базі якого будується стовпчикова діаграма

# Конфігурування осей
x_axis_config = {'title': 'РЕЗУЛЬТАТ', 'dtick': 1}  # Додаємо назву для осі x, 'dtick' -- ширина розмітки на осі х;
# 'dtick': 1 -- підписати кожну рисочку розмітки
y_axis_config = {'title': 'ЧАСТОТА ВИПАДІННЯ'}  # Додаємо назву для осі y

title_text = 'РЕЗУЛЬТАТИ КИДКІВ ДВОХ КУБИКІВ З 6 ТА 10 ГРАНЯМИ 50 000 РАЗІВ'
my_layout = Layout(title=title_text, xaxis=x_axis_config, yaxis=y_axis_config)
# ^ Layout -- повертає об'єкт, що містить компонування(layout) та налаштування графіка загалом:
# title -- назва діаграми, xaxis та yaxis -- словники з налаштуваннями осей
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')  # Генеруємо візуалізацію:
# 'data' -- набір даних, 'layout' -- компонування, filename -- ім'я файла, де міститиметься гістограма


