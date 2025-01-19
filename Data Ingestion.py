import pandas as pd 

df = pd.read_csv('data.csv')
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
print(df.info())
# Remove negative values
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
# Create TotalPrice
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
# Extract date parts
df['Year'] = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month
df['Day'] = df['InvoiceDate'].dt.day

print(df.head())



