import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    year = df['Year']
    sea_level = df['CSIRO Adjusted Sea Level']

    df_2000 = df[df['Year'] >= 2000]
    year_2000 = df_2000['Year']
    sea_level_2000 = df_2000['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(year, sea_level, c = 'lightsteelblue')

    # Create first line of best fit
    slope, yint, r, p, stderr = linregress(year, sea_level)
    plt.plot(year, yint + slope * year, c = 'cornflowerblue')

    # Create second line of best fit
    slope_2000, yint_2000, r, p, stderr = linregress(year_2000, sea_level_2000)
    plt.plot(year_2000, yint_2000 + slope_2000 * year_2000, c = 'orangered')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
