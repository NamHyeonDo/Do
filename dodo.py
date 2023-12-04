""" import matplotlib.pyplot as plt """

""" value = [1, 2, 3, 4]
res = plt.plot(value)
plt.show """

""" x_value = [2, 3, 6, 7, 10 ]
y_value = [1, 4, 5, 8, 9]

res = plt.plot(x_value, y_value)
print(res)
"""

""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val) """

""" plt.xlabel("x_data")
plt.ylabel("y_data")

plt.xlabel("x_data", labelpad=15)
plt.ylabel("y_data", labelpad=50)

plt.xlabel("x_data", loc="right")
plt.ylabel("y_data", loc="top") """

""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val)
plt.plot("x1_data", "y1_data", data=dic1_val) """

""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
plt.legend()

plt.legend(loc=(1, 1))

plt.legend(loc="lower right") """

""" import matplotlib.pyplot as plt

#plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")

#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="solid", label="PData(km)")

# linestyle(0, (픽셀크기, 여백간격))
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (1, 0)), label="PData(km)") 
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C1", label="Value(m)")
~
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C6", label="Value(m)")
plt.xlabel("x축")
plt.ylabel("y축")
"""

""" import matplotlib.pyplot as plt
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10, solid_capstyle="round", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=10, solid_capstyle="round", label="Value(m)"
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "cd", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="H", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker=11, label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="s", label="PData(km)")
plt.xticks()
plt.yticks()

# 임의 데이터 지정
plt.xticks([0,1,2,3,4,5,6,7,8,9,10])

# 라벨 지정
plt.xticks([1,2,3,4,5,6,7,8,9,10], labels=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"])
plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11], labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# 눈금 안쪽/바깥쪽 지
plt.tick_params(axis="x", direction="in")
plt.xlabel("x축")
plt.ylabel("y축") """

""" import matplotlib.pyplot as plt

x_years = ['2020', '2021', '2022']
y_data = [100, 400, 900]
clr = ["r", "g", "b"]



#plt.bar(x_years, y_data)
#plt.bar(x_years, y_data, color="g")
plt.bar(x_years, y_data, color="c7")
plt.bar(x_years, y_data, color=clr)
plt.bar(x_years, y_data, color=clr, width=2)
plt.bar(x_years, y_data, color=clr, align="edge", width=0.5)
plt.bar(x_years, y_data, color=clr, align="edge", width=0.5)
plt.show() """

import matplotlib.pyplot as plt
plt.barh(x_years, y_data)