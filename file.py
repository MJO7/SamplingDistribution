import plotly.graph_objects as go
import statistics as statistics
import plotly.figure_factory as ff
import random
import pandas as pd
import csv

df = pd.read_csv('data.csv')
data = df["temp"].to_list()
def random_setOfMean(counter) :
    dataSet = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()


def setup():
    mean_list=[]
    for i in range(0,1000):
        setOfMeans = random_setOfMean(100)
        mean_list.append(setOfMeans)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("Mean of Sampling Distribution is" ,mean )
setup()
population_mean = statistics.mean(data)
print("Population Mean:" , population_mean)

# code to find the standard deviation of the sample data
def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        random_setOfMean= random_setOfMean(100)
        mean_list.append(random_setOfMean)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()