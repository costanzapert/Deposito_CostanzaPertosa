#punto 1
import numpy as np, pandas as pd, matplotlib.pyplot as plt, seaborn as sns
media = 1200
devizione_standard = 900
giorni = 305
visit = np.random.normal(loc=media, scale=devizione_standard, size = giorni)
visit= np.clip(visit, a_min=0, a_max=None)

#punto 2
date = pd.date_range(start="2024-01-01", end="2024-12-31", periods=305).date
patologie = np.random.choice(['ossa', 'cuore', 'testa'], size=giorni)
d = {'col1': visit, 'col2': patologie}
df = pd.DataFrame(data=d , index = date)

#punto3
df.index = pd.to_datetime(df.index)
calcolo_media = df.groupby(df.index.month)["Visite"].mean()
calcola_dev_st = df.groupby(df.index.month)["Visite"].std()
df["Patologie"].value_counts()

#punto4
plt.figure(figsize=(8, 5))
sns.scatterplot(x= date, y='Visite', data=df, hue='Patologie', style='Patologie', palette='coolwarm', alpha=0.7)
plt.xlabel('Data')
plt.ylabel('Patologie')
plt.title('Data e Patologie (Scatter Plot)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()