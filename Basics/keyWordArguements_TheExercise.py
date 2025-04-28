def get_Phone(country, area, first, last):
    return F"{country} - {area} - {first} - {last}"

phone_num = get_Phone(country=63, area=1234, first=5678, last=9012)

print(phone_num)