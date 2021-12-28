import matplotlib.pyplot as plt

if __name__ == '__main__':

    plt.plot([-1, -4.5, 3.14, 1])


    x0,x1 = plt.xlim()
    y0,y1 = plt.ylim()
    print(plt.xlim())
    print(plt.ylim())

    import numpy as np

    X,Y = np.meshgrid(np.arange(round(x0), round(x1)+1),
                      np.arange(round(y0), round(y1)+1))

    plt.scatter(X,Y)
    plt.show()