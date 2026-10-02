student = {
    "name": "Ana",
    "contacts": {
        "email": "ana@gmail.com",
        "phone": "555123456"
    },
    "courses": {
        "python": {"score": 92, "passed": True},
        "web": {"score": 55, "passed": False}
    }
}


print(student["contacts"]["email"])

print(student["courses"]["python"]["score"])

student["courses"]["web"]["passed"] = True
student["courses"]["web"]["score"] = 65
print(student["courses"]["web"])

del student["contacts"]["phone"]
print(student["contacts"])



# frontend_skills = {"HTML", "CSS", "JavaScript", "React"}
# backend_skills = {"Python", "JavaScript", "SQL", "React"}
# print("Union:", frontend_skills | backend_skills)
# print("Intersection:", frontend_skills & backend_skills)
# print("Difference:", frontend_skills - backend_skills)
# print("Symmetric difference:", frontend_skills ^ backend_skills)



# words = ["apple", "banana", "apple", "cherry", "banana", "apple", "orange"]

# word_counts = {}

# for w in words:
#     word_counts[w] = word_counts.get(w, 0) + 1

# print(word_counts)

# for key, value in word_counts.items():
#     if value > 1:
#         print(f"{key}: {value}")