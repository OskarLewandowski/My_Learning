import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import beta

sns.set(style="darkgrid")

leptokurtyczna = np.random.normal(5, 0.5, 10000)
mesokurtyczna = np.random.normal(5, 1, 10000)
platokurtyczna = beta.rvs(2, 2, size=10000) * 6 + 2

df_kurtoza = pd.DataFrame({
    'Leptokurtyczna': leptokurtyczna,
    'Mesokurtyczna': mesokurtyczna,
    'Platokurtyczna': platokurtyczna
})

x_lim = (0, 10)
y_lim = (0, 0.9)

#Leptokurtyczna
plt.figure(figsize=(8, 5))
sns.histplot(df_kurtoza['Leptokurtyczna'], kde=True, color="gray", stat="density", bins=30)
plt.gca().get_lines()[0].set_color('red')
plt.xlim(x_lim)
plt.ylim(y_lim)
plt.title("Rozkład leptokurtyczny - Kurtoza jest dodatnia")
plt.xlabel("Wartości zmiennej")
plt.ylabel("Gęstość rozkładu")
plt.savefig(f"leptokurtyczna.png")
plt.close()

#Mesokurtyczny
plt.figure(figsize=(8, 5))
sns.histplot(df_kurtoza['Mesokurtyczna'], kde=True, color="gray", stat="density", bins=30)
plt.gca().get_lines()[0].set_color('red')
plt.xlim(x_lim)
plt.ylim(y_lim)
plt.title("Rozkład mesokurtyczny - Kurtoza jest równa 0")
plt.xlabel("Wartości zmiennej")
plt.ylabel("Gęstość rozkładu")
plt.savefig(f"mesokurtyczny.png")
plt.close()

#Platokurtyczny
plt.figure(figsize=(8, 5))
sns.histplot(df_kurtoza['Platokurtyczna'], kde=True, color="gray", stat="density", bins=30)
plt.gca().get_lines()[0].set_color('red')
plt.xlim(x_lim)
plt.ylim(y_lim)
plt.title("Rozkład platokurtyczny - Kurtoza jest ujemna")
plt.xlabel("Wartości zmiennej")
plt.ylabel("Gęstość rozkładu")
plt.savefig(f"platokurtyczny.png")
plt.close()
