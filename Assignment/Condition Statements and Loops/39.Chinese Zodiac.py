'''Write a Python program to display the sign of the 
Chinese Zodiac for the given year in which you were born.
Expected Output:

Input your birth year: 1973                                             
Your Zodiac sign : Ox  '''

rooster_year=[2017,2005,1993,1981]
dog_year=[2018,2006,1994,1982]
pig_year=[2019,2007,1995,1983]
rat_year=[2020,2008,1996,1984]
ox_years=[2021,2009,1997,1985]
tiger_year=[2022,2010,1998,1986]
rabbit_year=[2023,2011,1999,1987]
dragon_year=[2024,2012,2000,1988]
snake_year=[2025,2013,2001,1989]
horse_year=[2026,2014,2002,1990]
goat_year=[2027,2015,2003,1991]
monkey_year=[2028,2016,2004,1992]

x=int(input("Enter your birth year: "))
if x in rooster_year:
    print("Your Zodiac sign : rooster")
elif x in dog_year:
    print("Your Zodiac sign : dog")
elif x in pig_year:
    print("Your Zodiac sign : pig")
elif x in rat_year:
    print("Your Zodiac sign : rat")
elif x in ox_years:
    print("Your Zodiac sign : Ox")
elif x in tiger_year:
    print("Your Zodiac sign : Tiger")
elif x in rabbit_year:
    print("Your Zodiac sign : rabbit")
elif x in dragon_year:
    print("Your Zodiac sign : dragon")
elif x in snake_year:
    print("Your Zodiac sign : snake")
elif x in horse_year:
    print("Your Zodiac sign : horse")
elif x in goat_year:
    print("Your Zodiac sign : goat")
elif x in monkey_year:
    print("Your Zodiac sign : monkey")


