import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# load example tips dataset
tips = sns.load_dataset("tips")
print("Showing first 5 rows of example dataset...")
print(tips.head()) 
