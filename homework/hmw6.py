# scores=[]
# scores.append(45)
# scores.append(88)
# scores.append(92)
# scores.append(60)
# scores.append(75)
# scores.remove(45)
# average=sum(scores)/len(scores)
# print(f"average: {average}")
# print(f"max: {max(scores)}")
# print(f"lowest: {min(scores)}")
# scores.sort()
# print(f"sorted scores: {scores}")
# passed_scores=[i for i in scores if i>=60]
# print(f"passed scores: {passed_scores}")

# inventory=["apple","banana","orange","apple","kiwi","apple"]
# new_items=["mango","grape"]
# print("apple count: " ,inventory.count("apple"))
# print("orange index: ", inventory.index("orange"))
# inventory.extend(new_items)

# print("reversed inventoy: ", inventory[::-1])

locations=[
("Tbilisi",41.71,44.82),
("Batumi",41.64,41.63),
("Kutaisi",42.26,42.71)]
for city, lat,lon in locations:
    print(f"city:{city}, latitude:{lat}, longitude:{lon}")
    city_names=[city for city,lat,lon in locations ]
    print("city names: ", city_names)