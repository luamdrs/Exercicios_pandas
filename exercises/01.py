# Criando uma Series chamada temp com temperaturas de cada dia da semana.

import pandas as pd

temp = pd.Series([20, 22, 21, 19, 24, 26, 23],
                index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

print(temp)