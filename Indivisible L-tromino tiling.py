import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [15,15]

# Settings
def settings():
    plt.axis('equal')
    plt.axis('off')
    plt.show()

# Case 1 :(2,3)
def Case1() :
    from matplotlib.patches import Rectangle
    plt.plot((0,3,3,0,0),(0,0,2,2,0),'k')
    plt.plot((2,2,1,1),(0,1,1,2),'k')


# Case 2 : (6,2n),n ≥ 2
def Case2(n):
    plt.plot((-n, n, n, -n, -n), (-3, -3, 3, 3, -3), 'k')
    plt.plot((-n + 1, n - 1), (0, 0), 'k')

    for x in range(-n + 3, n - 2, 2):
        plt.plot((x, x), (-2, 2), 'k')
        plt.plot((x, x + 1), (1, 1), 'k')
        plt.plot((x + 1, x + 2), (2, 2), 'k')
        plt.plot((-x, -x - 1), (-1, -1), 'k')
        plt.plot((-x - 1, -x - 2), (-2, -2), 'k')
        plt.plot((x + 1, x + 1), (1, 3), 'k')
        plt.plot((-x - 1, -x - 1), (-1, -3), 'k')
    plt.plot((n - 1, n - 1), (0, 2), 'k')
    plt.plot((-n + 1, -n + 1), (0, -2), 'k')
    plt.plot((n - 2, n - 2, n), (0, -1, -1), 'k')
    plt.plot((-n + 2, -n + 2, -n), (0, 1, 1), 'k')
    plt.plot((n - 2, n - 2), (-2, -3), 'k')
    plt.plot((-n + 2, -n + 2), (2, 3), 'k')
    plt.plot((n - 1, n - 1, n - 3), (-1, -2, -2), 'k')
    plt.plot((-n + 1, -n + 1, -n + 3), (1, 2, 2), 'k')
    plt.plot((n - 1, n), (1, 1), 'k')
    plt.plot((-n + 1, -n), (-1, -1), 'k')

# Case 3 : (6n,2m+4), n ≥ 2 , m ≥ 2
def Case3(n,m) :

    # Drawing rectangle
    plt.plot([-4,2*m,2*m,-4,-4],[0,0,6*n,6*n,0],'k')

    # Drawing an outline

    for i in range(6,6*n,6):
        plt.plot([2,2*m],[i,i],'k')
        plt.plot([-4,-2],[i,i],'k')

    plt.plot([0,0],[0,4],'k')
    plt.plot([0,0],[6*n,6*n-4],'k')

    for i in range(8,6*(n-1),6):
        plt.plot([0,0],[i,i+2],'k')

    # Drawing (partial) Flowers

    for y in range(6,6*n,6) :
        plt.plot([-1,-1,1,1],[y-1,y,y,y+1],'k')
        plt.plot([-1,0,0,1],[y+1,y+1,y-1,y-1],'k')

    # Completing the left part

    for y in range(3,6*n,6) :
        plt.plot([-4,-2,-2,0],[y+1,y+1,y-1,y-1],'k')
        plt.plot([-3,-3,-1,-1,-3,-3,-1,-1],[y+1,y+2,y+2,y,y,y-2,y-2,y-1],'k')
        plt.plot([-2,-2],[y+2,y+3],'k')
        plt.plot([-2,-2],[y-2,y-3],'k')
        plt.plot([-1,0],[y+1,y+1],'k')
        plt.plot([-3,-4],[y-1,y-1],'k')

    # Completing the right part

    for y in range(3,6*n,6) :
        plt.plot((1,2*m-1),(y,y),'k')
        for x in range(3,2*m-2,2):
            plt.plot((x,x),(y-2,y+2),'k')
            plt.plot((x,x+1),(y+1,y+1),'k')
            plt.plot((x+1,x+2),(y+2,y+2),'k')
            plt.plot((2*m-x,2*m-x-1),(y-1,y-1),'k')
            plt.plot((2*m-x-1,2*m-x-2),(y-2,y-2),'k')
            plt.plot((x+1,x+1),(y+1,y+3),'k')
            plt.plot((2*m-x-1,2*m-x-1),(y-1,y-3),'k')
        plt.plot((2*m-1,2*m-1),(y,y+2),'k')
        plt.plot((1,1),(y,y-2),'k')
        plt.plot((2*m-2,2*m-2,2*m),(y,y-1,y-1),'k')
        plt.plot((2,2,0),(y,y+1,y+1),'k')
        plt.plot((2*m-2,2*m-2),(y-2,y-3),'k')
        plt.plot((2,2),(y+2,y+3),'k')
        plt.plot((2*m-1,2*m-1,2*m-3),(y-1,y-2,y-2),'k')
        plt.plot((1,1,3),(y+1,y+2,y+2),'k')
        plt.plot((2*m-1,2*m),(y+1,y+1),'k')
        plt.plot((1,0),(y-1,y-1),'k')

# The final compilation

m = int(input('m : '))
n = int(input('n : '))

if {m,n} == {2,3} :
    Case1()
    settings()
elif (m % 2 == 0) and (n % 2 == 0) :
    if m == 6 :
        Case2(int(n/2))
        settings()
    elif n == 6 :
        Case2(int(m/2))
        settings()
    elif (m % 3 == 0) and (n > 6) :
        Case3(int(m/6),int(n/2-2))
        settings()
    elif (n % 3 == 0) and (m > 6) :
        Case3(int(n/6),int(m/2-2))
        settings()
    else :
        print('Nope, there does not exist such a tiling.')
else :
    print('Nope, there does not exist such a tiling.')