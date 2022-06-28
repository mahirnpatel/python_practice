user_Email = input("Enter your email : ")

user_name = user_Email[:user_Email.index('@')]
user_domain = user_Email[user_Email.index('@')+1 :]

print(f"User Email : {user_name} and User Domain : {user_domain}")