restaurants = pd.read_csv('restaurants.csv')
print(restaurants.head())

cuisine_options_count = restaurants.cuisine.nunique()

cuisine_counts = restaurants.groupby('cuisine').name.count().reset_index()

print(cuisine_counts)



cuisines = cuisine_counts.cuisine.values
counts = cuisine_counts.name.values

plt.pie(counts, labels=cuisines, autopct='%d%%') 
plt.title('Counts of Cuisines')
plt.axis('equal')
plt.show()


orders = pd.read_csv('orders.csv')

print orders.head()

orders['month'] = orders.date.apply(lambda x: x.split('-')[0])

print orders.head()

avg_order = orders.groupby('month').price.mean().reset_index()

std_order = orders.groupby('month').price.std().reset_index()


months = avg_order.month
months = pd.to_numeric(months)

bar_heights = avg_order.price
bar_errors = std_order.price

ax= plt.subplot()
plt.bar(range(len(months)), bar_heights, yerr=bar_errors, capsize=5)
ax.set_xticks(range(len(months)))
ax.set_xticklabels(['April', 'May', 'June', 'July', 'August', 'September'])
plt.ylabel('Average Order Price')
plt.title('Order Price by Month')

#How much has each customer on FoodWheel spent over the past six months? What can this tell us about the average FoodWheel customer?#

orders = pd.read_csv('orders.csv')

customer_amount = orders.groupby('customer_id').price.sum().reset_index()

print(customer_amount.head())

plt.hist(customer_amount.price, range=(0,200), bins=40)
plt.xlabel('Total Spent')
plt.ylabel('Number of Customers')
plt.title('Bla')

plt.show()
