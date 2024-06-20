import secrets

def generate_password():
    return secrets.token_urlsafe(16)

def reveal_master_password(user_a_pass, user_b_pass, input_a, input_b):
    if user_a_pass == input_a and user_b_pass == input_b:
        print("Master Password:", master_password)
    else:
        print("Incorrect passwords. Access denied.")

person_a_password = generate_password()
person_b_password = generate_password()

# Print the passwords for demonstration purposes
print("Person A's Password:", person_a_password)
print("Person B's Password:", person_b_password)

master_password = generate_password()

# For demonstration purposes, we'll assume Person A and B have securely received their passwords
input_from_person_a = input("Person A, please enter your password: ")
input_from_person_b = input("Person B, please enter your password: ")

reveal_master_password(person_a_password, person_b_password, input_from_person_a, input_from_person_b)
