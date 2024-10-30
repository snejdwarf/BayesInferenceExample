from pylab import *
import matplotlib.pyplot as plt
import pyAgrum as gum
import pandas as pd
import pyAgrum.lib.bn2graph  # For converting the Bayesian Network to DOT format
from graphviz import Source


bn = gum.BayesNet("WaterSprinkler")

bn.add(gum.LabelizedVariable('c', 'Cloudy?', 2))
bn.add(gum.LabelizedVariable('s', 'Sprinkler?', 2))
bn.add(gum.LabelizedVariable('r', 'Rain?', 2))
bn.add(gum.LabelizedVariable('w', 'Wet Grass?', 2))
bn.addArc('c','s')
bn.addArc('c', 'r')
bn.addArc('r', 'w')
bn.addArc('s', 'w')


bn.generateCPTs()

dot = pyAgrum.lib.bn2graph.BN2dot(bn)
dot.plot()

data = pd.DataFrame({
    'c':[1,1,0,0],
    's':[0,1,1,0]
})

learner = gum.BNLearner(data)




print("Done")