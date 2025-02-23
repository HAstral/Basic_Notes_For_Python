# for x in range(1,11):
#     print(x , end=" ")

def get_phone(country,area,first,last):
    return f"+{country}-{area}-{first}-{last}"

ph_num=get_phone(country=91,area=80,first=1234,last=5678)

print(ph_num)
