def celsius_to_fahrenheit(temp):
    fahrenheit = (temp * 9/5) + 32
    return  str(fahrenheit) + '°F'

def fahrenheit_to_celsius(temp):
    celsius = (temp - 32) * 5/9
    return str(celsius) + '°C'

celsius_to_fahrenheit(32)
fahrenheit_to_celsius(89.6)



