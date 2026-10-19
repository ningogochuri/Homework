# def save_quote():
#     writer = input("Enter your favorite writer: ")
#     quote = input("Enter your favorite quote: ")

#     with open("quotes.txt", "a") as file:
#         file.write(f"Writer: {writer} : {quote}\n")
    

# def read_quotes():
#         with open("quotes.txt", "r") as file:
#             data = file.read()
#             print(data)
# save_quote()        
# read_quotes()
    


# import csv


# def read_survivors():
#     survivors = []


#     with open("titanic.csv", "r", newline="") as file:
#         reader = csv.DictReader(file)

#         for row in reader:
#             if row["Survived"] == "1":
#                 survivors.append(row)

#     return survivors


# def write_survivors():
#     survivors = read_survivors()

#     if not survivors:
#         print("No survivors found.")
#         return

#     with open("survived.csv", "w", newline="") as file:
#         writer = csv.DictWriter(
#             file,
#             fieldnames=survivors[0].keys()
#         )

#         writer.writeheader()
#         writer.writerows(survivors)

#     print("Survivors saved successfully!")


# write_survivors()





import csv


def read_companies():
    companies = []

    with open("ssl_companies.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if int(row["Number of employees"]) > 1000:
                companies.append(row)

    return companies


def write_companies():
    companies = read_companies()

    with open("sorted_companies.csv", "w", newline="") as file:
        fieldnames = ["Name", "Industry", "Number of employees"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for company in companies:
            writer.writerow({
                "Name": company["Name"],
                "Industry": company["Industry"],
                "Number of employees": company["Number of employees"]
            })

    print("Companies saved successfully!")


write_companies()
