import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df_sea = pd.read_csv("epa-sea-level.csv")

    x = df_sea["Year"]
    y = df_sea["CSIRO Adjusted Sea Level"]

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x, y, c="blue")
    plt.xlabel("Year")
    plt.ylabel("CSIRO Adjusted Sea Level")

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x,y)

    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = intercept + slope * x_pred

    plt.plot(x_pred, y_pred, 'red', label='Best fit line 1')

    # Create second line of best fit
    df2_sea = df_sea.loc[df_sea["Year"] >= 2000]
    x2 = df2_sea["Year"]
    y2 = df2_sea["CSIRO Adjusted Sea Level"]

    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x2, y2)

    x2_pred = pd.Series([i for i in range(2000, 2051)])
    y2_pred = intercept2 + slope2 * x2_pred

    plt.plot(x2_pred, y2_pred, 'green', label='Best fit line 2')

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
