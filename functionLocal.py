def hourToMinut(seconds, minut=90):
    hours = minut/60 + seconds/3600
    return hours

print(hourToMinut(890))