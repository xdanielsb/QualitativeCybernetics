import math as m
import numpy as np
import matplotlib.pyplot as plt


def qfunction(Pr, minv, maxv, step, x0, num_iter =10):
    #create values
    x = np.arange(minv, maxv, step)
    auxx = np.arange(0, maxv+0.1, step)
    G = []
    y = []
    for r in x:
        G.append(eval(Pr))
        y.append(r)

    #Plot the function
    plt.plot(x, G, 'b-', ms=1, label='F')

    #Plote the 45* rect
    plt.plot(auxx, auxx, 'r-',  label="R")

    #Now plote the xvalues
    r = x0
    x1= eval(Pr)
    cont = 1

    while x1 != x0 and cont < num_iter :
        #vertical line
        plt.plot([x0, x0], [0, x1], 'g-', ms=1, label='X'+str(cont))

        #Horizontal rect
        plt.plot([x0, x1], [x1, x1], 'g-', ms=1)

        x0 = x1
        r = x0
        x1 = eval(Pr)
        cont += 1

    plt.xlabel('X')  #Label
    plt.legend(loc='best') #Legenda
    plt.show()#Muestra
