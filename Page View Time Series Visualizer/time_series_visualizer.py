import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("dfs/fcc-forum-pageviews.csv", index_col="date", parse_dates=["date"])

# Clean data
df = df[df["value"].between(df["value"].quantile(0.025), df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize= (18, 8))
    plt.plot(
        df.index,
        df["value"],
        color = "red"
    )
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.pivot_table(values="value", index=df.index.month_name(), columns=df.index.year, aggfunc="mean", fill_value=0)
    df_bar = df_bar.reindex(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    df_bar.index = df_bar.index.rename("Months")

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12,8)) 
    df_bar.T.plot(
        kind="bar", 
        xlabel="Years",
        ylabel="Average Page Views",
        ax=ax)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize = (18, 8))
    sns.boxplot(
        data = df_box,
        x = "year",
        y = "value",
        hue = "year",
        flierprops = dict(marker="D", markersize = 2, markerfacecolor= "black"),
        ax=ax[0]
    )
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Page Views")
    ax[0].set_title("Year-wise Box Plot (Trend)")

    sns.boxplot(
        data = df_box,
        x = "month",
        y = "value",
        order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        hue = "month",
        flierprops = dict(marker="D", markersize = 2, markerfacecolor= "black"),
        ax=ax[1]
    )
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Page Views")
    ax[1].set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
