# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set_theme(style="ticks", color_codes=True)
# titanic=sns.load_dataset("titanic")
# sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic)
# plt.show()

import matplotlib.pyplot as plt
x= [0, 5, 10, 15, 20, 25, 30]
y1=[10, 15, 20, 20, 30, 15, 0]
y2=[10, 12, 15, 12, 20, 10 ,0]
plt.plot(x, y1, linestyle="dashed")
plt.plot(x, y2, linestyle="dashed")
plt.show()