# def even_numbers():
#     num=0
#     while True:
#         yield num
#         num+=2

# func=even_numbers()
# count=0
# for num in func:
#     print(num)
#     count+= 1
#     if count ==10:
#         break




# words= ["Python","generator","yield","code","ai", "developer"]
# filtered_words= ( word.upper() for word in words if len(word) >4 )
# for word in filtered_words:
#     print(word)


def greenter_bot():
    name= yield "enter your  name, please !"
    while True:
        name = yield f"hello,  {name}"
bot= greenter_bot()
print(next(bot))
print(bot.send("Nino"))
print(bot.send("Giorgi"))
print(bot.send("Ana"))
