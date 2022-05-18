import pandas as pd
import matplotlib.pyplot as plt
read_file = pd.read_csv('zillow.csv', names=['Index', 'LivingSpace (sqft)', 'Beds', 'Baths', 'Zip', 'Year',
                                          'ListPrice ($)'], index_col='Index')
sort = read_file.sort_values(by='Beds').head(20)
df = pd.DataFrame(sort)
print(df)
plt.hist(df['Beds'], bins=20)
plt.savefig('Beds.png')