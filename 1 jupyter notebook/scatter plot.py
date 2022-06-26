import seaborn as sns
import matplotlib as plt
sns.set_theme(style="tick", color_codes=True)
titanic=sns.load_dataset("titanic")
g=sns.FacetGrid(titanic, row="sex", hue="alone")
g=(g.map(plt.scatter, "age", "fare").add_legend())
plt.show()