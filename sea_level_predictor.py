import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('sea-level-predictor/data/epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()

    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    regr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = pd.Series([i for i in range(1880, 2051)])
    y = regr.slope * x + regr.intercept
    plt.plot(x, y)

    # Create second line of best fit
    df = df.loc[df['Year'] >= 2000]
    regr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = pd.Series([i for i in range(2000, 2051)])
    y = regr.slope * x + regr.intercept
    plt.plot(x, y)

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea-level-predictor/results/sea_level_plot.png')
    return plt.gca()