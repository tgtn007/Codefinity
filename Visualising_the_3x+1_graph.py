from math import log10
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
def log(n):
    return log10(n)
def backend(n):
    # return the 3x+1 series of a number
    result = [n]
    while n!=1:
        if n%2 != 0:
            n = n*3+1
            result.append(n)
            n = n/2
            
            result.append(n)


        if n%2==0:
            n = n/2
            
            result.append(n)

    
    return list(map(int, result))


def unit(n):
    # return the list of unit digit of the occuring number in the 3x+1 form of that
    result = []
    for i in n:
        i = list(str(i))
        i = i[0]
        result.append(i)
    return list(map(int, result))

def calc(n):
    # return the sum of the unit digit of the series of the number
    return sum(unit(backend(n)))

x1 = [calc(i) for i in range(1,101)]
x2 = [len(backend(i)) for i in range(1,101)]
y = np.array([i for i in range(1,101)]).reshape(-1,1)
x = []
for i in range(len(x1)):
    x.append([log(x1[i]*x2[i])])
x = np.array(x).reshape(-1,1)
print(f"x is {x[0]}")
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)
model = LinearRegression()
model.fit(x_train,y_train)
print(model.score(x_test, y_test))

plt.plot(x,y)
plt.title("log of product of sum of unit digit and length of series vs number")
# plt.plot(np.linspace(0,5,100).reshape(-1,1), model.predict(np.linspace(0,5,100).reshape(-1,1)), 'r')
plt.show() 
testing = log(calc(15)*len(backend(15)))
print(testing)
print(model.predict(np.array(testing).reshape(-1,1)))
