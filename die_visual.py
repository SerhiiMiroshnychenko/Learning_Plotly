from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Створити D6
die = Die()

# Зробити декілька кидків та зберегти результати в список
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Проаналізуємо результати
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Візуалізувати результати
x_values = list(range(1, die.num_sides+1))  # Список, що зберігає всі стовпчики
data = [Bar(x=x_values, y=frequencies)]  # Клас Bar представляє набір даних
# на базі якого будується стовпчикова діаграма

# Конфігурування осей
x_axis_config = {'title': 'РЕЗУЛЬТАТ'}  # Додаємо назву для осі x
y_axis_config = {'title': 'ЧАСТОТА ВИПАДІННЯ'}  # Додаємо назву для осі y

my_layout = Layout(title='РЕЗУЛЬТАТИ КИДКІВ ОДНОГО КУБИКА 1000 РАЗІВ', xaxis=x_axis_config, yaxis=y_axis_config)
# ^ Layout -- повертає об'єкт, що містить компонування(layout) та налаштування графіка загалом:
# title -- назва діаграми, xaxis та yaxis -- словники з налаштуваннями осей
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')  # Генеруємо візуалізацію:
# 'data' -- набір даних, 'layout' -- компонування, filename -- ім'я файла, де міститиметься гістограма
