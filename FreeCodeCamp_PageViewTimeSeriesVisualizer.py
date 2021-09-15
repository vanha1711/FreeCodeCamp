import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean data
df = df[(df['value'] >= (df['value'].quantile(0.025))) &
        (df['value'] <= (df['value'].quantile(0.975)))].reset_index()
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(6, 3))
    df['value'].plot(linewidth=2.5, color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize=14)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Page Views', fontsize=14)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar["Months"] = df_bar.index.month
    df_bar["Years"] = df_bar.index.year

    df_bar = df_bar.groupby([df_bar["Years"], df_bar["Months"]])["value"].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot
    fig = df_bar.plot(kind="bar", legend=True, figsize=(14, 10)).figure
    plt.xlabel('Years', fontsize=14)
    plt.ylabel('Average Page Views', fontsize=14)

    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.legend(fontsize=10, title="Months", labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    df_box = df_box.rename(columns={"value":"Page Views"})
    df_box["month_num"] = df_box["date"].dt.month
    df_box = df_box.sort_values("month_num")

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1,2)

    ax1 = sns.boxplot(x="year", y="Page Views", data=df_box, ax=ax1)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    ax2 = sns.boxplot(x="month", y="Page Views", data=df_box, ax=ax2)
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
