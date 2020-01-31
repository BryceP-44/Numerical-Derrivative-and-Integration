#Integral and derrivative calculator 
while True:
    import multiprocessing
    from math import *
    N = 300
    NN = 1000
    v1 = 0
    v2 = 0
    v3 = 0
    v4 = 0
    s = .1
    cont = 1
    current=0
    #a=0
    #b=4
    #xcor = 3
    print(" ")
    print(" ")
    print(" ")
    a = int(input("Lower bound for integral: "))
    b = int(input("Upper bound for integral: "))
    xcor = int(input("X-value for derrivative: "))
    def f(x):
            return 1/x
    if __name__ == '__main__':
        jobs = []
        for n in range(1, N+1):
            p = multiprocessing.Process(target=f)
            jobs.append(p)
            p.start()
            v1 += f(a+((n-(1/2))*((b-a)/N)))
    if __name__ == '__main__':
        jobs = []
        for n in range(1, 3):
            p = multiprocessing.Process(target=f)
            jobs.append(p)
            p.start()
            h = 1/(100000000)
            der = (f(xcor + h) - f(xcor))/h
    v2 = (((b-a)/N)*v1)+.001
    print("Integral: ", v2, "    Derrivative: ", der)
    cont = input("y for more accurate integral or enter to restart: ")
    if cont == "y":
        jobs = []
        for n in range(1, NN+1):
            p = multiprocessing.Process(target=f)
            jobs.append(p)
            p.start()
            v3 += f(a+((n-(1/2))*((b-a)/NN)))
            percent = (n/NN)*100
            percent = round(percent, 3)
            print(percent, "% percent done")
            print(" ")
    v4 = (((b-a)/NN)*v3)
    print("More accurate integral: ", v4)


