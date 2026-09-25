correct_pin="1234"
max_attempts=3
attempts=0
while attempts<max_attempts:
    pin=input("Enter your 4-digit Pin: ")
    attempts+=1
    if pin==correct_pin:
       print("Access granted")
       break
    else:
        remaining=max_attempts-attempts
        if remaining>0:
            print(f"Incorrect Pin. Remaining attempts:{remaining}")
        else:
            print("card blocked")