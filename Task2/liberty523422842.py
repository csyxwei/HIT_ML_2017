<<<<<<< HEAD
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
# 使用c++对数据进行了排序
x = array([(1.000000 ,-4.97795850),
(1.000000 ,-4.88058910),
(1.000000 ,-4.39759510),
(1.000000 ,-4.22604370),
(1.000000 ,-4.07055100),
(1.000000 ,-3.98832700),
(1.000000 ,-3.54271740),
(1.000000 ,-3.49337000),
(1.000000 ,-3.43749840),
(1.000000 ,-2.81744770),
(1.000000 ,-2.60695340),
(1.000000 ,-2.34292460),
(1.000000 ,-1.87078540),
(1.000000 ,-1.74808430),
(1.000000 ,-1.50736730),
(1.000000 ,-1.49378560),
(1.000000 ,-1.21655850),
(1.000000 ,-0.95217727),
(1.000000 ,-0.72123756),
(1.000000 ,-0.62859563),
(1.000000 ,-0.62500378),
(1.000000 ,-0.53982031),
(1.000000 ,-0.28015898),
(1.000000 ,-0.10117321),
(1.000000 ,-0.01077714),
(1.000000 ,0.13264331),
(1.000000 ,0.34811345),
(1.000000 ,0.37525605),
(1.000000 ,0.73450428),
(1.000000 ,0.86214789),
(1.000000 ,0.90916205),
(1.000000 ,1.24214310),
(1.000000 ,1.44329910),
(1.000000 ,1.75726820),
(1.000000 ,1.79808960),
(1.000000 ,1.80480510),
(1.000000 ,2.00934480),
(1.000000 ,2.15697600),
(1.000000 ,2.33480460),
(1.000000 ,2.34699880),
(1.000000 ,2.54248010),
(1.000000 ,2.91413330),
(1.000000 ,3.27983630),
(1.000000 ,3.37842430),
(1.000000 ,3.44272460),
(1.000000 ,3.44920850),
(1.000000 ,3.45663720),
(1.000000 ,3.54586390),
(1.000000 ,3.70888730),
(1.000000 ,3.72346010),
(1.000000 ,3.78346240),
(1.000000 ,4.00177890),
(1.000000 ,4.09790500),
(1.000000 ,4.23116130),
(1.000000 ,4.48005540),
(1.000000 ,4.48287420),
(1.000000 ,4.49702490),
(1.000000 ,4.50245900),
(1.000000 ,5.23748460),
(1.000000 ,5.73515640),
(1.000000 ,6.19280450),
(1.000000 ,6.35892850),
(1.000000 ,6.73890560),
(1.000000 ,6.91264570),
(1.000000 ,6.93323720),
(1.000000 ,6.97629650),
(1.000000 ,7.16226560),
(1.000000 ,7.31761140),
(1.000000 ,7.49118340),
(1.000000 ,7.49270890),
(1.000000 ,7.55308270),
(1.000000 ,7.55443770),
(1.000000 ,7.83055540),
(1.000000 ,7.86266910),
(1.000000 ,8.13534180),
(1.000000 ,8.30622750),
(1.000000 ,8.42106600),
(1.000000 ,8.43571080),
(1.000000 ,8.62593900),
(1.000000 ,8.65319120),
(1.000000 ,8.72561750),
(1.000000 ,9.05954160),
(1.000000 ,9.15162440),
(1.000000 ,9.27778950),
(1.000000 ,9.31844950),
(1.000000 ,9.62835900),
(1.000000 ,9.64246760),
(1.000000 ,9.83587660),
(1.000000 ,9.87564530),
(1.000000 ,10.35868400),
(1.000000 ,10.37841800),
(1.000000 ,11.03228500),
(1.000000 ,11.10075400),
(1.000000 ,11.17163500),
(1.000000 ,11.34210500),
(1.000000 ,11.47034600),
(1.000000 ,11.55224400),
(1.000000 ,11.65283000),
(1.000000 ,11.69403000),
(1.000000 ,11.85335000)

])
y = array([-1.69422510,
-1.48605700,
-1.59901280,
-1.41928460,
-1.60387570,
-1.52087240,
-1.50115270,
-1.28288810,
-1.37217980,
-1.37013970,
-0.99119802,
-1.18136510,
-0.79712021,
-0.56510510,
-0.71916443,
-0.30838877,
-0.43840920,
-0.45044438,
-0.04170426,
0.12501713,
0.14789525,
-0.13282607,
0.40247523,
0.39212724,
0.42413595,
0.34282705,
0.64654095,
0.81341626,
0.85151329,
1.21782350,
0.94870075,
1.17176290,
1.43196920,
1.47095480,
1.54009720,
1.73045810,
1.92217030,
2.06663310,
1.88235540,
2.10565120,
2.08848990,
2.26439260,
1.97953130,
2.46106720,
2.33772980,
2.15081260,
1.70800610,
1.97444020,
2.36237650,
2.12004650,
2.09582370,
1.96718080,
2.32890200,
2.08588340,
2.04568730,
2.26827100,
2.38814140,
2.03109510,
2.20811530,
2.01263730,
1.77790950,
1.50303520,
1.64765880,
1.74719080,
1.31579360,
1.56545090,
1.45174930,
1.44943070,
1.39491970,
1.25717670,
1.57146590,
1.40839260,
1.15786300,
1.36655590,
1.14145460,
1.36822970,
1.38077040,
1.32423540,
0.92077948,
0.90302504,
1.16201960,
1.12028520,
1.17181420,
1.22755550,
1.02873040,
1.41288710,
1.05014040,
1.59503210,
1.12138070,
1.32429550,
1.35960560,
1.76510260,
1.78385350,
1.91300430,
2.03437780,
1.98189280,
2.00777170,
2.12153610,
2.13469280,
2.12117660
])

# 对某一点进行局部加权回归


def lwr(point, x_array, y_array, tau):
    x_matrix = mat(x_array)
    y_matrix = mat(y_array).T
    w_matrix = mat(eye(N=100))
    for i in range(0, 100):
        diff_matrix = point - x_matrix[i, :]
        w_matrix[i, i] = exp((diff_matrix * diff_matrix.T)/(-2 * tau ** 2))
    xTwx = x_matrix.T * w_matrix * x_matrix
    Theta = xTwx.I * x_matrix.T * w_matrix * y_matrix
    return linalg.det(Theta.T * mat(point).T)


# 对x数组进行拟合


def lwr_all(x_array, y_array, tau, color, ls, lb):
    X = x_array[:, 1]
    Y = []
    for i in range(0, 100):
        Y.append(lwr(x_array[i], x_array, y_array, tau))
    plot(X, Y, c=color, linestyle=ls,label=lb)

# 散点图
scatter(x[:, 1:2], y, c='k', marker='x', label='training data')
# tau = 0.1
lwr_all(x, y, 0.1, 'r', '--','tau = 0.1')
# tau = 0.3
lwr_all(x, y, 0.3, 'c','-','tau = 0.3')
# tau = 1
lwr_all(x, y, 1, 'm','-','tau = 1')
# tau = 3
lwr_all(x, y, 3, 'y', '-.','tau = 3')
# tau = 10
lwr_all(x, y, 10, 'r','--','tau = 10')
# tau = 30
lwr_all(x, y, 30, 'g','-','tau = 30')
# tau = 100
lwr_all(x, y, 100, 'b', ':','tau = 100')
plt.legend()
show()

=======
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
# 使用c++对数据进行了排序
x = array([(1.000000 ,-4.97795850),
(1.000000 ,-4.88058910),
(1.000000 ,-4.39759510),
(1.000000 ,-4.22604370),
(1.000000 ,-4.07055100),
(1.000000 ,-3.98832700),
(1.000000 ,-3.54271740),
(1.000000 ,-3.49337000),
(1.000000 ,-3.43749840),
(1.000000 ,-2.81744770),
(1.000000 ,-2.60695340),
(1.000000 ,-2.34292460),
(1.000000 ,-1.87078540),
(1.000000 ,-1.74808430),
(1.000000 ,-1.50736730),
(1.000000 ,-1.49378560),
(1.000000 ,-1.21655850),
(1.000000 ,-0.95217727),
(1.000000 ,-0.72123756),
(1.000000 ,-0.62859563),
(1.000000 ,-0.62500378),
(1.000000 ,-0.53982031),
(1.000000 ,-0.28015898),
(1.000000 ,-0.10117321),
(1.000000 ,-0.01077714),
(1.000000 ,0.13264331),
(1.000000 ,0.34811345),
(1.000000 ,0.37525605),
(1.000000 ,0.73450428),
(1.000000 ,0.86214789),
(1.000000 ,0.90916205),
(1.000000 ,1.24214310),
(1.000000 ,1.44329910),
(1.000000 ,1.75726820),
(1.000000 ,1.79808960),
(1.000000 ,1.80480510),
(1.000000 ,2.00934480),
(1.000000 ,2.15697600),
(1.000000 ,2.33480460),
(1.000000 ,2.34699880),
(1.000000 ,2.54248010),
(1.000000 ,2.91413330),
(1.000000 ,3.27983630),
(1.000000 ,3.37842430),
(1.000000 ,3.44272460),
(1.000000 ,3.44920850),
(1.000000 ,3.45663720),
(1.000000 ,3.54586390),
(1.000000 ,3.70888730),
(1.000000 ,3.72346010),
(1.000000 ,3.78346240),
(1.000000 ,4.00177890),
(1.000000 ,4.09790500),
(1.000000 ,4.23116130),
(1.000000 ,4.48005540),
(1.000000 ,4.48287420),
(1.000000 ,4.49702490),
(1.000000 ,4.50245900),
(1.000000 ,5.23748460),
(1.000000 ,5.73515640),
(1.000000 ,6.19280450),
(1.000000 ,6.35892850),
(1.000000 ,6.73890560),
(1.000000 ,6.91264570),
(1.000000 ,6.93323720),
(1.000000 ,6.97629650),
(1.000000 ,7.16226560),
(1.000000 ,7.31761140),
(1.000000 ,7.49118340),
(1.000000 ,7.49270890),
(1.000000 ,7.55308270),
(1.000000 ,7.55443770),
(1.000000 ,7.83055540),
(1.000000 ,7.86266910),
(1.000000 ,8.13534180),
(1.000000 ,8.30622750),
(1.000000 ,8.42106600),
(1.000000 ,8.43571080),
(1.000000 ,8.62593900),
(1.000000 ,8.65319120),
(1.000000 ,8.72561750),
(1.000000 ,9.05954160),
(1.000000 ,9.15162440),
(1.000000 ,9.27778950),
(1.000000 ,9.31844950),
(1.000000 ,9.62835900),
(1.000000 ,9.64246760),
(1.000000 ,9.83587660),
(1.000000 ,9.87564530),
(1.000000 ,10.35868400),
(1.000000 ,10.37841800),
(1.000000 ,11.03228500),
(1.000000 ,11.10075400),
(1.000000 ,11.17163500),
(1.000000 ,11.34210500),
(1.000000 ,11.47034600),
(1.000000 ,11.55224400),
(1.000000 ,11.65283000),
(1.000000 ,11.69403000),
(1.000000 ,11.85335000)

])
y = array([-1.69422510,
-1.48605700,
-1.59901280,
-1.41928460,
-1.60387570,
-1.52087240,
-1.50115270,
-1.28288810,
-1.37217980,
-1.37013970,
-0.99119802,
-1.18136510,
-0.79712021,
-0.56510510,
-0.71916443,
-0.30838877,
-0.43840920,
-0.45044438,
-0.04170426,
0.12501713,
0.14789525,
-0.13282607,
0.40247523,
0.39212724,
0.42413595,
0.34282705,
0.64654095,
0.81341626,
0.85151329,
1.21782350,
0.94870075,
1.17176290,
1.43196920,
1.47095480,
1.54009720,
1.73045810,
1.92217030,
2.06663310,
1.88235540,
2.10565120,
2.08848990,
2.26439260,
1.97953130,
2.46106720,
2.33772980,
2.15081260,
1.70800610,
1.97444020,
2.36237650,
2.12004650,
2.09582370,
1.96718080,
2.32890200,
2.08588340,
2.04568730,
2.26827100,
2.38814140,
2.03109510,
2.20811530,
2.01263730,
1.77790950,
1.50303520,
1.64765880,
1.74719080,
1.31579360,
1.56545090,
1.45174930,
1.44943070,
1.39491970,
1.25717670,
1.57146590,
1.40839260,
1.15786300,
1.36655590,
1.14145460,
1.36822970,
1.38077040,
1.32423540,
0.92077948,
0.90302504,
1.16201960,
1.12028520,
1.17181420,
1.22755550,
1.02873040,
1.41288710,
1.05014040,
1.59503210,
1.12138070,
1.32429550,
1.35960560,
1.76510260,
1.78385350,
1.91300430,
2.03437780,
1.98189280,
2.00777170,
2.12153610,
2.13469280,
2.12117660
])

# 对某一点进行局部加权回归


def lwr(point, x_array, y_array, tau):
    x_matrix = mat(x_array)
    y_matrix = mat(y_array).T
    w_matrix = mat(eye(N=100))
    for i in range(0, 100):
        diff_matrix = point - x_matrix[i, :]
        w_matrix[i, i] = exp((diff_matrix * diff_matrix.T)/(-2 * tau ** 2))
    xTwx = x_matrix.T * w_matrix * x_matrix
    Theta = xTwx.I * x_matrix.T * w_matrix * y_matrix
    return linalg.det(Theta.T * mat(point).T)


# 对x数组进行拟合


def lwr_all(x_array, y_array, tau, color, ls, lb):
    X = x_array[:, 1]
    Y = []
    for i in range(0, 100):
        Y.append(lwr(x_array[i], x_array, y_array, tau))
    plot(X, Y, c=color, linestyle=ls,label=lb)

# 散点图
scatter(x[:, 1:2], y, c='k', marker='x', label='training data')
# tau = 0.1
lwr_all(x, y, 0.1, 'r', '--','tau = 0.1')
# tau = 0.3
lwr_all(x, y, 0.3, 'c','-','tau = 0.3')
# tau = 1
lwr_all(x, y, 1, 'm','-','tau = 1')
# tau = 3
lwr_all(x, y, 3, 'y', '-.','tau = 3')
# tau = 10
lwr_all(x, y, 10, 'r','--','tau = 10')
# tau = 30
lwr_all(x, y, 30, 'g','-','tau = 30')
# tau = 100
lwr_all(x, y, 100, 'b', ':','tau = 100')
plt.legend()
show()
>>>>>>> 15c2936bd46c4e22cc3d656b0cec0acb9875cc2c
