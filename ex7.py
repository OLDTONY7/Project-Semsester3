studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]


for name in studentNames:
    print(f"{name} Evans")


new_name = input("Enter a new name to add to the list: ")
studentNames.append(new_name)

print("\nUpdated list:")
for name in studentNames:
    print(f"{name} Evans")
