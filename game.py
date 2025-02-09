import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
a = input('Enter the first name: ')
b = input('Enter the second name: ')
c = np.random.randint(1, 100)
print(f'The love percentage between {a} and {b} is {c}%')
img = Image.open('1.gif')
values = [c, 100 - c]
labels = [f" Love ({c}%)", "Remaining"]
colors = ['Red', 'Black']  
fig, ax = plt.subplots(figsize=(6, 6), facecolour='pink')
ax.pie(values, labels=labels, startangle=140, colors=colors,
       wedgeprops={'edgecolor': 'Pink', 'linewidth': 2},
       textprops={'fontsize': 12, 'fontweight': 'bold', 'color': 'Purple'})
ax.imshow(img, extent=[-2, 2, -2, 2], aspect='auto', alpha=0.3)
plt.title(f" Love Percentage: {a} ❤ {b} ", fontsize=14, fontweight='bold', color='Pink')
plt.show()
