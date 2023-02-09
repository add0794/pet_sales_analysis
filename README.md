# Pet Sales Analysis

PetMind is a nationwide pet product retailer in the United States. With inflation hitting 41-year highs, the company is planning to reduce the cost of customer retention by improving brand loyalty. The first strategy is to launch a monthly pet box subscription in three months.

The marketing team is preparing a list of popular products for the pet box subscription. The chief marketing officer wants to know whether the list should only include the products being purchased more than once.

The marketing team would like to answer the following questions to help with the decision:

- How many products are being purchased more than once?
- Do the products being purchased again have better sales than others?
- What products are more likely to be purchased again for different types of pets?

## **Data Validation**

The original data is comprised of 879 rows and 9 columns. To validate the data, I went through each column to check that the data matches the criteria in the data dictionary.

The first thing I did was remove rows that should be excluded. The easiest approach was to remove those rows that didn't match the pet types explicitly defined (i.e. must be fish, cat, dog, or bird). Then, I changed values that didn't match specified requirements. For sales, this required removing any formatting (e.g. "$"), and for rebuy, switching 0's and 1's to boolean values of True and False. I now had 833 rows. 

Looking at the remaining columns, I now had the following:

1. Each product ID and vendor ID is unique.
2. There are 11 unique product categories, as expected.
3. There are 5 unique pet sizes, as expected.
4. There are 10 customer ratings, on a 1-10 point scale.

**How many products are being purchased more than once?**

All products are sold more than once. It's important to keep in mind that, overall, products still have greater counts of being sold once: 390, sold more than once; 443, sold once. This can be well represented in a stacked bar graph.

![Overall Count of Products Sold](https://github.com/add0794/pet_sales_analysis/blob/e0e572698563b3501f7fb1de50ca236c126cc8a9/images/output_1.png)

Equipment, snack, and toys are sold more than once the most, with 69, 59, and 58 units sold, respectively. The pet store should prioritize these items rather than the least resold item, grooming, which resold 17 units. In fact, equipment was resold 3.5-times as much as grooming.

![Count of Products Sold More Than Once](https://github.com/add0794/pet_sales_analysis/blob/e0e572698563b3501f7fb1de50ca236c126cc8a9/images/output_2.png)

**Do the products being purchased again have better sales than others?**

As a whole, products sold more than once have lower sales than products sold once: &dollar;45.6 million relative to &dollar;51.1 million. In other words, products sold once not only accounted for more sales but by a considerable margin: 11.5%.

In fact, of the products sold once, supplements, toys, snack, clothes, and grooming have sales as much as 25% higher. On the other hand, housing and bedding sold higher when being sold more than once, with both selling at around 25% higher. With equipment, snacks, and toys, those differences can rack up considerable sales' differences. For equipment, which is sold more than once, that's &dollar;973,000. For snacks and toys, that's &dollar;2,443,000 and &dollar;2,285,000, respectively.

![Sales of Products Sold More Than Once](https://github.com/add0794/pet_sales_analysis/blob/e0e572698563b3501f7fb1de50ca236c126cc8a9/images/output_3.png)

**What products are more likely to be purchased again for different types of pets?**

To determine what products are more likely to be purchased again, I wanted to visualize whether and how frequently each product is sold once and more than once for each pet. It's critical to see product counts for each pet when sold once relative to more than once, and which product has counts that are greater for the latter. 

I found that for the following pets, these products had higher counts when being sold more than once:

- Cat: **equipment, food**
- Dog: **accessory, bedding, equipment, food, grooming, medicine**
- Fish: **housing**

For birds, there is no such product.

![Cat Product Sold More Than Once](https://github.com/add0794/pet_sales_analysis/blob/e0e572698563b3501f7fb1de50ca236c126cc8a9/images/output_4.png)
![Dog Product Sold More Than Once](https://github.com/add0794/pet_sales_analysis/blob/e0e572698563b3501f7fb1de50ca236c126cc8a9/images/output_5.png)
![Fish Product Sold More Than Once](https://github.com/add0794/pet_sales_analysis/blob/e0e572698563b3501f7fb1de50ca236c126cc8a9/images/output_6.png)
![Bird Product Sold More Than Once](https://github.com/add0794/pet_sales_analysis/blob/e0e572698563b3501f7fb1de50ca236c126cc8a9/images/output_7.png)

The pet store should prioritize, however, one product for each pet. Because dogs have 6 products on that list, it would be inefficient to do otherwise.

The pet store can focus on the following products for each pet, with the net in counts being sold more than once relative to once in parentheses:

- Fish: **Housing** (2 counts)
- Cat: **Equipment** (3 counts)
- Dog: **Bedding** (9 counts)

For birds, it should consider how to increase counts of products sold more than once, particularly for equipment, snack, and toys.

