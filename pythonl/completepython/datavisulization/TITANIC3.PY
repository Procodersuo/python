import seaborn as sea
import matplotlib.pyplot as mtl
sea.set_theme(style="ticks", color_codes=True)
myData=sea.load_dataset("titanic")
g=sea.FacetGrid(myData, row="sex", hue="alone")
g=(g.map(mtl.scatter, "age", "fare").add_legend())
mtl.show()