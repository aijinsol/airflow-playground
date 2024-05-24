def get_sftp():
    print("sftp START")


def register(name, gender, *args):
    print(f"Name: {name}")
    print(f"Gender: {gender}")
    print(f"ETC: {args}")
    
    
def register2(name, gender, *args, **kwargs):
    print(f'Name: {name}')
    print(f'Gender: {gender}')
    print(f'ETC: {args}')
    email = kwargs['email'] or None
    phone = kwargs['phone'] or None
    if email:
        print(f'Email: {email}')
    if phone:
        print(f'Phone: {phone}')
