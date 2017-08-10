from function import qfunction

if __name__ == "__main__":
    #define the function
    Pr= "((r**2)*(m.e**(4*m.pi)) / (( 1- (r**2)) + ((r**2)*(m.e**(4*m.pi)))))"

    minv = 0.0
    maxv = 1.0
    step = 0.0001
    x0 = 0.1

    qfunction(Pr, minv, maxv, step, x0)
