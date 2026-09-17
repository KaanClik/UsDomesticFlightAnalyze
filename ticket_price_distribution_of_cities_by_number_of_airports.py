import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import ttest_ind_from_stats
import matplotlib.pyplot as plt

df = pd.read_excel(r'path')
df = df.iloc[:-3]
print(df.head())
df.info()
print(round(df.describe(),2))
print(df.columns)

city_count = df['City_Name'].value_counts()
single_airport = city_count[city_count== 1].index
multiple_airports = city_count[city_count > 1].index

group_a_monopol=df[df['City_Name'].isin(single_airport)]['Average_Fare']
group_b_competition=df[df['City_Name'].isin(multiple_airports)]['Average_Fare']

print(f"Group A (Single Airport) Avg Price: {group_a_monopol.mean(): 2f})")
print(f"Group B (Multiple Airport) Avg Price: {group_b_competition.mean(): 2f})")

t_test_result = stats.ttest_ind(group_a_monopol, group_b_competition, equal_var=False)
print(f'T Test Result: {t_test_result[0]} P-Value: {t_test_result[1]} ')

p_value = round(t_test_result[1],2 )
if p_value >= 0.05:
    print(f'Having more than one airport in a city does not have a statistically demonstrable, clear effect on ticket prices. Clearly visible in the table.')
else:
    print(f'Having more than one airport in a city have a statistically demonstrable, clear effect on ticket prices. Clearly visible in the table.')


plt.boxplot([group_a_monopol, group_b_competition],tick_labels=['Single Airport', 'Multiple Airport'])
plt.title('Ticket Price Distribution of Cities by Number of Airports')
plt.ylabel('Ticket Price [$]')
plt.show()





