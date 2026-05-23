import pandas as pd
import matplotlib.pyplot as plt
#Load the sales data
df = pd.read_csv(r'C:\Users\Akshara\Documents\sales_analysis\sales_analysis.csv') 
#Showing first 10 rows of the data
print(df.head(10))
#Checking for missing values
print(df.isnull().sum())
#Calculating total sales
df['Total Sales']=df['Quantity']*df['Price']
#Calculating total sales by product
sales_by_product=df.groupby('Product')['Total Sales'].sum().head(10)
print("\nSales by Product:\n")
print(sales_by_product)
#Finding best selling product
best_selling_product=sales_by_product.idxmax()
print('\nBest selling product:',best_selling_product)
#Category wise performance
sales_by_category=df.groupby('Category')['Total Sales'].sum()
print('\nCategory wise performance:\n')
print(sales_by_category)
#Calculating daily sales trend
df['Date'] = pd.to_datetime(df['Date'])
daily_sales = df.groupby('Date')['Total Sales'].sum()
print('\nDaily sales trend:\n')
print(daily_sales)
#Visualizing sales trends over time
plt.figure(figsize=(10,5))
plt.plot(daily_sales,marker='o',color='blue')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.title('Sales Trends Over Time')
plt.grid(True)
plt.savefig('sales_trends.png') #Save the plot as an image file
plt.show()
#Visualizing top products
plt.figure(figsize=(12,5))
plt.bar(sales_by_product.index,sales_by_product.values,color='green')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.title('Top Selling Products')
plt.xticks(rotation=20)
plt.savefig('top_products.png') 
plt.show()
#Category wise distribution chart
plt.figure(figsize=(7,7))
plt.pie(sales_by_category, labels=sales_by_category.index, autopct='%1.1f%%')
plt.title('Category Wise Distribution')
plt.savefig('category_distribution.png')
plt.show()
