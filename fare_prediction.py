import pandas as pd
import numpy as np
import scipy.stats as stats
import seaborn as sns
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df=pd.read_excel(r'C:\Users\ASUS\Desktop\Projects\UsDomesticFlights\UsDomesticFlights\average_fare_sql.xlsx')
df=df.iloc[:-3]

df.info()

df['2025_Passengers_Sample10'] = df['2025_Passengers_Sample10'].astype(float)
df['Average_Fare'] = df['Average_Fare'].astype(float)

x = df[['2025_Passengers_Sample10']]
y = df['Average_Fare']

model = LinearRegression()
model.fit(x,y)
model_score = round(model.score(x,y),4)
model_coef = round(model.coef_[0],6)
print(f"R^2 = : {model_score}")
print(f"Coefficient = {model_coef}")

if model_coef <= 25:
    print(f"We can't say that there is relation between ticket prices and passenger number."
          f"Increasing passenger count by 1% will increases the ticket price only by {model_coef} dollars.")
else:
    print(f"There is a meaningful linear relation between ticket prices and passenger number."
          f"Increasing the passenger count by 1% increases the ticket price by {model_coef} dollars.")


plt.scatter(df['2025_Passengers_Sample10'],df['Average_Fare'])
plt.title('Regression Model')
plt.ylabel('Average Fare [$]')
plt.xlabel('2026 Passengers Sample')
plt.show()

df['Log_Passengers'] = np.log1p(df['2025_Passengers_Sample10'])
x= df[['Log_Passengers']]
y = df['Average_Fare']
model_log = LinearRegression()
model_log.fit(x,y)
model_log_score = round(model_log.score(x,y),4)
model_log_coef = round(model_log.coef_[0],6)
print(f"R^2 = : {model_log_score}")
print(f"Coefficient = {model_log_coef}")

if model_log_coef/100 <=25:
    print(f"We still can't say that there is relation between ticket prices and passenger number after Logarithmic Transformation."
          f"Increasing passenger count by 1% will increases the ticket price only by {round(model_log_coef/100,2)} dollars.")
else:
    print(f"There is a meaningful linear relation after Logarithmic Transformation."
          f"Increasing the passenger count by 1% increases the ticket price by {round(model_log_coef/100, 2)} dollars.")

##even the coefficient response 13.83 because of the tranformation rule changed to B/100 so increasing volume of
##passenger %1 will increase the ticket price only  13.83/100 = 0.13 dollars.

plt.scatter(df['Log_Passengers'],df['Average_Fare'])
plt.title('Log Transformed Regression Model')
plt.ylabel('Average Fare [$]')
plt.xlabel('Log Transformed 2026 Passengers Sample')
plt.show()





