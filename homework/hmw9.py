# def create_user_profile(first_name, last_name, role="Student", is_active=True):
#     return {
#         "first_name": first_name,
#         "last_name": last_name,
#         "role": role,
#         "is_active": is_active
#     }

# profile1 = create_user_profile("Nino", "Gogotchuri")
# print(profile1)

# profile2 = create_user_profile("Nino", "Gogotchuri", role="Teacher", is_active=False)
# print(profile2)


# def add_task(task_name, task_list=[]):
#     task_list.append(task_name)
#     return task_list

# print(add_task("Buy groceries"))
# print(add_task("Do homework"))
# print(add_task("Go to gym"))
#ფუნქციის განსაზღვრისას ლისტი ერთხელ იქმნება და ყოველი გამოძახებისას იგივე ლისტს იყენებს

# def add_task(task_name, task_list=None):
#     if task_list is None:
#         task_list = [] 

#     task_list.append(task_name)
#     return task_list

# print(add_task("Buy groceries"))
# print(add_task("Do homework"))
# print(add_task("Go to gym"))

# my_list = ["Existing task"]
# print(add_task("New task", my_list))



def analyze_text(text, min_length=3, ignore_stopwords=None):

    if ignore_stopwords is None:
        ignore_stopwords = []

    words = text.split()

    count = 0
    for word in words:
        if len(word) >= min_length and word.lower() not in ignore_stopwords:
            count += 1

    return count
text = "I am student and learning Python"
print(analyze_text(text))

print(analyze_text(text, min_length=5))

stopwords = ["and", "is", "it", "the"]
print(analyze_text(text, min_length=3, ignore_stopwords=stopwords))