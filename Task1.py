import numpy as np

def generate1():
    a = np.random.uniform(0, 1)
    b = np.random.uniform(0, 1)
    return (a * np.cos(2 * np.pi * b), a * np.sin(2 * np.pi * b))

def generate2():
    while True:
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if x ** 2 + y ** 2 > 1:
            continue
        return (x, y)

x1 = []
y1 = []
for el in range (1,1000):
    x1_,y1_ = generate1()
    x1.append(x1_)
    y1.append(y1_)
x2=[]
y2=[]
for el2 in range (1,1000):
    x2_,y2_ = generate2()
    x2.append(x2_)
    y2.append(y2_)

# import matplotlib.pyplot as plt
# fig, ax = plt.subplots()
#
# ax.scatter(x1, y1,
#            c = 'red')    #  цвет точек
# ax.scatter(x2, y2,
#            c = 'blue')
# ax.set_facecolor('white')     #  цвет области Axes
#
# fig.set_figwidth(8)     #  ширина и
# fig.set_figheight(8)    #  высота "Figure"
#
# plt.show()

# import pandas as pd
# cols = ['x', 'y', 'label']
# points = pd.DataFrame(columns=cols)
# points['x'] = x1
# points['y'] = y1
# points['label'] = 0
# points2 = pd.DataFrame(columns=cols)
# points2['x'] = x2
# points2['y'] = y2
# points2['label'] = 1
# allpoints = pd.concat([points, points2], axis=0)
# print(allpoints.tail())
# from sklearn.model_selection import train_test_split
# X = allpoints.drop(columns='label')
# y = allpoints['label']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# from sklearn.ensemble import GradientBoostingClassifier
# gb = GradientBoostingClassifier()
# gb.fit(X_train, y_train)
# preds = gb.predict(X_test)
# from sklearn.metrics import accuracy_score
# acc = accuracy_score(y_test, preds)
#
# print(acc)
lines = []
for line in range (1,201):
    line1 = []
    line2 = []
    for el in range (1,1000):
        x1_,y1_ = generate1()
        line1.append(x1_)
        line1.append(y1_)
        x2_,y2_ = generate2()
        line2.append(x2_)
        line2.append(y2_)
    lines.append(line1)
    lines.append(line2)

for line in lines:
    x = []
    y = []
    ind = 0
    while ind < len(line)-1:
        x.append(line[ind])
        y.append(line[ind + 1])
        ind +=2
    if np.var(x) > 0.2 and np.var(y) > 0.2:
        print(2)
    else:
        print(1)

print(np.var(x1))
print(np.var(y1))
print(np.var(x2))
print(np.var(y2))
