#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('car_refueling_data.csv')
df['Date'] = pd.to_datetime(df['Date'], format='%d.%m.%Y')
df['Fuel consumption (L/100km)'] = (df['Liters'] / df['Kilometers Traveled']) * 100



average_fuel_consumption = df['Fuel consumption (L/100km)'].mean()

# print(df['Fuel Consumption (L/100km)'].mean())
# print(average_fuel_consumption)
# print(df['Fuel Efficiency (L/100km)'])

# plt.style.use('seaborn-darkgrid')

# seaborn-v0_8-darkgrid
plt.style.use('seaborn-v0_8-darkgrid')

plt.figure(figsize=(14, 7))
plt.plot(df['Date'], df['Fuel consumption (L/100km)'], marker='o', label='Fuel Consumption (L/100km)', color='b')
plt.axhline(y=average_fuel_consumption, color='r', linestyle='--', label=f'Average: {average_fuel_consumption:.2f} L/100km')
plt.title("Fuel consumption Over Time", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Fuel consumption (L/100km)", fontsize=14)
plt.legend(fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['Kilometers Traveled'], df['Liters'], alpha=0.7, c='g', edgecolors='k', label='Data Points')

z = np.polyfit(df['Kilometers Traveled'], df['Liters'], 1)
p = np.poly1d(z)
plt.plot(df['Kilometers Traveled'], p(df['Kilometers Traveled']), "r--", label='Trend Line')


plt.title("Liters Consumed vs. Kilometers Traveled", fontsize=16)
plt.xlabel("Kilometers Traveled", fontsize=14)
plt.ylabel("Liters Consumed", fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()


# In[ ]:





# In[17]:


# print(plt.style.available)


# In[ ]:




