'''
Name: Daniyal Arshad
'''

from textblob import TextBlob as tb
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import json



def get_sentiment(filename):
    with open(filename, mode='r') as fp:
        lst = json.load(fp)

    lst2 = []
    for tw in lst:
        lst2.append(tb(tw))
    blob = []
    for l in lst2:
        if l.polarity != 0.0 or l.subjectivity != 0.0:
            blob.append(l.polarity)
    data = pd.Series(blob)
    return[data.mean(), data.std(ddof = 1)]


def get_ct_sentiment_frame():

    index = ["Sinema", "McSally"]
    columns = ["pre_mean", "pre_std", "post_mean", "post_std"]
    sinema = get_sentiment("sinema_tweets_run437pm.json") + get_sentiment("sinema_tweets_run949pm.json")
    mcsally = get_sentiment("mcsally_tweets_run437pm.json") + get_sentiment("mcsally_tweets_run949pm.json")
    data = [sinema, mcsally]



    return pd.DataFrame(data = data, index = index, columns=columns)


def make_fig(df):
    e = df[['pre_std', 'post_std']].T 
    data = df[['pre_mean', 'post_mean']].T
    e.index = data.index = ['Sinema-McSally 4:37pm', 'Sinema-McSally 9:49pm']
    data.columns = e.columns = [0, 1]
    ax = data.plot.bar(legend =False , yerr = e, capsize = 10, rot = 0, fontsize = 18, color =['b', 'g'], ec = "black", figsize = [10, 6])

   

    ax.set_ylabel("Sentiment", fontsize = 24)
    ax.set_facecolor("red")
    ax.tick_params(axis = "x", colors="red", labelsize = 14)
    ax.tick_params(axis = "y", colors="red", labelsize = 14)
    ax.set_facecolor("#FFF0F5")


    ax.xaxis.label.set_color("blue")
    ax.yaxis.label.set_color("red")

    ax.spines["top"].set_color("red")
    ax.spines["bottom"].set_color("red")
    ax.spines["right"].set_color("red")
    ax.spines["left"].set_color("red")


    plt.xticks(rotation = 360)
    plt.gcf().set_facecolor("black")
   
    return None
    

#======
def main():

    fname = get_ct_sentiment_frame()
    make_fig(fname)
    plt.show()








