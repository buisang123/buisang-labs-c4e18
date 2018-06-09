import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

# 1. prepare data
labels = ["ios","android","web","react native"] 
values = [20,15,40,25]
color = ["red","green","gold","purple"]
explode = [0,0,0,0.2]
# 2. plot
pyplot.pie(values, labels = labels,colors = color,explode= explode, shadow= True )
pyplot.axis("equal")
# 3. show
pyplot.show()