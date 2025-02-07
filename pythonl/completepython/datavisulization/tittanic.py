import seaborn as sea
import matplotlib.pyplot as mtl
sea.set_theme(style="ticks",color_codes=True)
myData= sea.load_dataset("titanic")
sea.catplot(x="sex", y="survived",kind="bar", hue="class", data=myData)
mtl.show()