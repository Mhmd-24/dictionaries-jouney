# Example dictionaries:
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 10, "d": 4}

print(f"Dict1 is {dict1}\n")
print(f"Dict1 is {dict2}\n")

merged_dict = dict1.copy()  # Create a copy of dict1 to avoid modifying the original
merged_dict.update(dict2)   # Update with dict2, overriding duplicate keys

# Create a variable named output to put the updated dictionary in it and print it
output = merged_dict
print(f"The merged dictionary is: {output}")

# Ask if there the user wants to update the dictionary more and validate the answer using strip() and upper()
answer = input("\nDo you want to update it more? Y/N \n").strip().upper()

while answer not in ("Y", "N"):
    answer = input("Please enter Y or N \n").strip().upper()

if answer == "Y":
    new = input("How many letters you want to update?:\n")

    while not new.isdigit() or int(new) <= 0:
        new = input("Please enter a proper number for the letters you want to update:\n")

    new = int(new)  # Convert input to an integer

    for i in range(new):  
        letter = input("Enter a letter (old or new): \n")
        value = input("Enter a value for it: \n")
        merged_dict[letter] = value 
    
    print("Updated Dictionary:", merged_dict)  # Display the updated dictionary

  
elif answer == "N":
    print("Good Bye.\n")
