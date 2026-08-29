import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.7)

    # 3. Create first line of best fit (using all data from 1880 to 2050)
    # محاسبه شیب و عرض از مبدأ برای کل داده‌ها
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # تعریف سال‌ها از ۱۸۸۰ تا ۲۰۵۰ برای خط پیش‌بینی
    years_extended = pd.Series(range(1880, 2051))
    
    # محاسبه y = mx + c
    line_all = res_all.slope * years_extended + res_all.intercept
    ax.plot(years_extended, line_all, 'r', label='Fits all data')

    # 4. Create second line of best fit (using data from year 2000 onwards)
    # فیلتر داده‌ها از سال ۲۰۰۰ به بعد
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
     
    # تعریف سال‌ها از ۲۰۰۰ تا ۲۰۵۰ برای خط پیش‌بینی جدید
    years_recent = pd.Series(range(2000, 2051))
    
    # محاسبه y = mx + c برای داده‌های اخیر
    line_recent = res_recent.slope * years_recent + res_recent.intercept
    ax.plot(years_recent, line_recent, 'green', label='Fits since 2000')

    # 5. Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
