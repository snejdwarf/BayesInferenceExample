A demonstration of bayesian networks and inference using PyAgrum.
main.ipynb contains an example bn with parameters being learned from some synthetic data.

The example consist of a model with four binary variables Cloudy, Rain, Sprinkler and Wet. Cloudy indicates wether or not the weather is cloude which in turn affects if there is rain and if the sprinklers will turn on respectively. Both the rain and sprinkler variable affects if the grass will be wet (represented by the Wet variable).

For each variable, there is an associated conditional probability table that specifies the probability distribution over the variable's states given the state of it's parents. These tables (CPTs) can be specified manually or learned from data. 