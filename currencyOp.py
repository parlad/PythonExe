def curencuyOpeartors(rate, euros):
    dollars = euros * rate
    return dollars

r =eval(input("enter rate"))
e= eval(input("enter euros"))

print(curencuyOpeartors(r,e))
