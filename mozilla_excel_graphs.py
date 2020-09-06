import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as plticker


# Follower Growth
def follower_graph():
    insights = pd.read_csv("D:\\Dropbox\\Python DataScraping\\Insights_Files\\overall_details.csv")
    fig, ax = plt.subplots()
    fig.set_size_inches(22, 8)
    plt.scatter(insights.date_posted, insights.follows, c='lightblue')
    degrees = 70
    plt.xticks(insights.date_posted, rotation=degrees)
    plt.xlabel('Date Posted')
    plt.ylabel('Follows Gained')
    plt.plot(insights.date_posted, insights.follows, c='lightblue')
    plt.savefig("D:\\Dropbox\\Python DataScraping\\Insights_Files\\fig1")


def impressions_growth():
    insights = pd.read_csv("C:\\Users\\Brianna's HP17\\Desktop\\Insights_Files\\overall_details.csv")
    fig, ax = plt.subplots()
    fig.set_size_inches(22, 8)
    ax.plot(insights.date_posted, insights.impressions, c='coral')
    degrees = 70
    plt.xticks(insights.date_posted, rotation=degrees)
    plt.xlabel('Date Posted')
    plt.ylabel('Impressions')
    loc = plticker.MultipleLocator(base=10.0)
    ax.yaxis.set_major_locator(loc)
    plt.savefig("D:\\Dropbox\\Python DataScraping\\Insights_Files\\fig2")


def main():
    follower_graph()
    impressions_growth()


if __name__ == '__main__':
    main()
