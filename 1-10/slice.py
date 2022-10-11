email = input('Enter your Email: ')
username = email[:email.index('@')]
domain_name = email[email.index('@')+1:]
format = f'your user name is {username} and your domain is {domain_name}'
print(format)