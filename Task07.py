def celsius_to_fahrenheit(temp):
    temp_in_celsius = (temp * 9/5) + 32
    return  str(temp_in_celsius) + '°F'

def fahrenheit_to_celsius(temp):
    temp_in_fahrenheits = (temp - 32) * 5/9
    return str(temp_in_fahrenheits) + '°C'

celsius_to_fahrenheit(32)
fahrenheit_to_celsius(89.6)



