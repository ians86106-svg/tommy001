has_completed_homework = True
has_parents_permission = True

if has_completed_homework and has_parents_permission:
    print("You can go to the party!")
else:
    print("You cannot go to the party.")

    speed =45

    if speed > 60:
        print("Fast")
    elif speed > 30:
        print("Moderate")
    else:
        print("Slow")

    has_library_card = True
    has_overdue_books = False

    if has_library_card and not has_overdue_books:
        print("You can borrow books from the library.")
    else:
        print("You cannot borrow books from the library.")

        age =16
        has_ticket = True

        if age >= 18 and has_ticket:
            print("You can attend the concert.")
        else:
            print("You cannot attend the concert.")

        temperature = 28
        if temperature > 25:
            print("It's hot outside.")
        else:
            print("It's not too hot outside.")

        def multiply_numbers(a, b):
            return a * b

        result = multiply_numbers(5, 3)
        print("The result of multiplication is:", result)


def welcome_user(name):
    print("Welcome,", name)


welcome_user("Alice")
def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    print("The number is:", is_even_or_odd(7))