def bonus(years):
    dod=0
    if years<=5:
        dod+=100*years   
    elif years<=8:
        dod+=100*5+200(years-5)
    elif years>8:
        dod+=100*5+200*3+50*(years-8)
    print(dod)

years=int(input())
bonus(years)
