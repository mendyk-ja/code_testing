from name_function import get_formatted_name

print("Insert 'q' to quit program.")
while True:
    first = input("\nInsert first name: ")
    if first == 'q':
        break
    last = input("\nInsert last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\nElegantly formatted full name: {formatted_name}.")