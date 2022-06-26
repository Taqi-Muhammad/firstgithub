import seaborn as sns
import matplotlib as plt
phool=sns.load_dataset("iris")
sns.lineplot(x="sepal_lenght", y="sepal_width", data=phool)
plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# # sns.set_theme(style="ticks", color_codes=True)
# kashti=sns.load_dataset("titanic")
# # sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic)
# # plt.show()
# kashti
# sns.barplot(x="sex", y="alone", hue="who", data=kashti)
# plt.show()