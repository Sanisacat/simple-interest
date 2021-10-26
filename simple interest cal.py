def si(p,t,r):
    print("The principle is ", p)
    print("The amount is ", t)
    print("The rate of interest is ", r)

    si = (p * t * r)/100

    print('The simple Interest is Rs.', si)

p = float(input("Enter the principle amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time period: "))
si(p, r, t)
