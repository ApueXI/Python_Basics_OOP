# arga = allows you to pass multiple non-key arugments
# kwargs = allows you to pass multiple keyword-arugments

# * args is a tupple
# **kwargs is a dictionary

def address(**kwargs):
    for key, values in kwargs.items():
        print(f'{key} : {values}')

(address(street='1234',apartmentnum='5423', city='detroit', state='DC', zipcode='1560'))