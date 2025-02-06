import matplotlib.pyplot as plt
import numpy as np

a = input('Enter the first name: ')
b = input('Enter the name of the second person: ')

c = np.random.randint(1, 100)
print(f'The love percentage between {a} and {b} is {c}%')

values = [c, 100 - c]
labels = [f"Love ({c}%)", "Remaining"]
colors = ['red', 'black']


plt.figure(figsize=(6, 6))
plt.pie(values, labels=labels, startangle=140, colors=colors)
plt.title(f"Love Percentage: {a} ❤ {b}")
plt.show()
