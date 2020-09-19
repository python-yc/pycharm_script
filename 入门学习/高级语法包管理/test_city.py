# def get_formatted_information(city,country):
#     '''Generate a neatly formatted full name'''
#     full_information = city+','+country
#     return full_information.title()
from city_coutry import get_formatted_information

print("Enter 'q' at any time to quit.")
while True:
    city = input("Please give me your city_name:")
    if city == 'q':
        break
    country = input("Please give me your country_name:")
    if country == 'q':
        break

    formatted_information = get_formatted_information(city,country)
    print("your information is :"+ formatted_information)






