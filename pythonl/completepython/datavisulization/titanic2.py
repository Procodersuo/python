import seaborn as sea
import matplotlib.pyplot as mtl
sea.set_theme(style="ticks",color_codes=True)
myData= sea.load_dataset("titanic")
myBar=sea.countplot(x="sex", hue="class", data=myData)
myBar.set_title("TITAINCI MAIN ZINDA BCHE LOGON KA DATA")
mtl.show()