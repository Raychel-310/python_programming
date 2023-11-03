from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np

# 積分する関数を定義
def f(x):
    return x**2

def integral_1(f, a, b, n):
    area = 0
    x = a
    w = (b-a)/n
    while x < b:
        area += w*f(x)
        x += w
    return area

def integral_2(f, a, b, n):
    h = (b - a) / n
    area = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        x = a + i * h
        area += f(x)
    area *= h
    return area

result, _ = integrate.quad(f, 1, 2) 

n_values = list(range(1, 1000))  # nの値のリスト
diff_values_1 = [abs(integral_1(lambda x: x**2, 1, 2, n) - result) for n in n_values]  # diffの値のリスト
diff_values_2 = [abs(integral_2(lambda x: x**2, 1, 2, n) - result) for n in n_values]  # diffの値のリスト

plt.plot(n_values, diff_values_1, label='rectangle rule')  # 線グラフを作成
plt.plot(n_values, diff_values_2, label='trapezoidal rule')  # 線グラフを作成
plt.xlabel('n')  # X軸のラベル
plt.ylabel('error')  # Y軸のラベル
# plt.title('difference')  # グラフのタイトル
plt.legend()  # 凡例を表示
plt.show()  # グラフを表示
