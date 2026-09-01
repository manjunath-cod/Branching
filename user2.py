 # User Details Program

def get_user_details():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    city = input("Enter your city: ")

    print("\n--- User Details ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"City: {city}")

# Run the function
get_user_details()
