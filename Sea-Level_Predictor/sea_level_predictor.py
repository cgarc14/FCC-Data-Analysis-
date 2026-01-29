import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("dfs/epa-sea-level.csv")

    # Create scatter plot
    plt.figure()
    plt.scatter(
        data = df,
        x = "Year",
        y = "CSIRO Adjusted Sea Level"
    )

    # Create first line of best fit
    lin_regress = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    projected_years = list(range(int((df["Year"].min())), 2051))
    slope = lin_regress.slope
    intercept = lin_regress.intercept
    predicted_values = [slope * year + intercept for year in projected_years]

    plt.plot(
        projected_years,
        predicted_values,
        "red"
    )

    # Create second line of best fit
    df2 = df[df["Year"] >= 2000]
    lin_regress2 = linregress(df2["Year"], df2["CSIRO Adjusted Sea Level"])
    projected_years2 = list(range(int((df2["Year"].min())), 2051))
    slope2 = lin_regress2.slope
    intercept2 = lin_regress2.intercept
    predicted_values2 = [slope2 * year + intercept2 for year in projected_years2]

    plt.plot(
        projected_years2,
        predicted_values2,
        "green"
    )

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
