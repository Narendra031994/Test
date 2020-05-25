import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
data = pd.read_csv(r"C:\Users\Naren\Desktop\test_data.csv")
data_x = data[["age","it_exp"]]
data_y = data["going_to_die"]
data_x
cl = DecisionTreeClassifier(max_depth = 2,random_state = 0)
cl.fit(data_x,data_y)
cl.predict([[100,20]])

# This wil visualize the DecisionTree structure constructed for the training tuples
tree.plot_tree(cl)