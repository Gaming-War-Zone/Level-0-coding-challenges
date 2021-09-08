def number_to_hrs_and_min(num):
    hours = 0
    while num >=60:
        hours += 1
        num -=60

    minutes = num
    if minutes!=1:
        min_string = 'minutes'
    else:
        min_string = 'minute'

    if hours!=1:
        hr_string = 'hours'
    else:
        hr_string = 'hour'

    print(f"{hours} {hr_string}, {minutes} {min_string}")

number_to_hrs_and_min(154)
