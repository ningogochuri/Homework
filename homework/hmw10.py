# def sum_of_digits(n):
#     if n < 10:
#         return n
#     return (n % 10) + sum_of_digits(n // 10)

# print(sum_of_digits(1234)) 
# print(sum_of_digits(999))   
# print(sum_of_digits(7))    


#2
# scores = [45, 82, 67, 38, 90, 55, 72]

# passing_scores = list(filter(lambda score: score >= 50, scores))
# print("გამსვლელი ქულები:", passing_scores)

# boosted_scores = list(map(lambda score: min(score + 5, 100), passing_scores))
# print("ბონუსის შემდეგ:", boosted_scores)



#3
names   = ["Laptop", "Phone", "Headphones", "Monitor"]
prices  = [1200, 800, 150, 300]
ratings = [4.8, 4.5, 4.2, 4.9]

catalog = list(zip(names, prices, ratings))
print("კატალოგი:", catalog)
# [('Laptop', 1200, 4.8), ('Phone', 800, 4.5), ('Headphones', 150, 4.2), ('Monitor', 300, 4.9)]


sorted_by_price = sorted(catalog, key=lambda product: product[1], reverse=True)
print("\nფასით (ძვირიდან იაფამდე):")
for name, price, rating in sorted_by_price:
    print(f"  {name}: ${price}, {rating}")


sorted_by_rating = sorted(catalog, key=lambda product: product[2])
print("\nრეიტინგით (დაბლიდან მაღლამდე):")
for name, price, rating in sorted_by_rating:
    print(f"  {name}: ${price}, {rating}")