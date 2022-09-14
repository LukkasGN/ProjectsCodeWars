"""

In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year 
and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater 
or equal to p = 1200 inhabitants?

"""

def nb_year(p0, percent, aug, p):
    
    people = p0
    year = 0

    while people <= p:
        people = people + people * percent + aug
        year = year + 1
    
    return year

print(nb_year(1500, 5, 100, 5000))