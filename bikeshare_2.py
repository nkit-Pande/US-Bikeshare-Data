import time
import pandas as pd
import numpy as np
from util import loading_animation

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print("\n\033[1;35mWelcome! Let's explore US BikeShare data! 🚴‍♂️\033[0m\n")

    cities = ['chicago', 'new york city', 'washington']
    city_options = {'1': 'chicago', '2': 'new york city', '3': 'washington'}

    while True:
        opt = input("\033[1;34mEnter the city name (Chicago, New York City, Washington)\n"
                    "or select a number (1: Chicago, 2: New York City, 3: Washington): \033[0m").strip().lower()

        if opt in cities:
            city = opt
            break
        elif opt in city_options:
            city = city_options[opt]
            break
        else:
            print("\n\033[1;31mInvalid input. Please select a valid city option.\033[0m\n")

    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month_options = {str(i + 1): months[i] for i in range(len(months))}

    while True:
        opt = input("\n\033[1;32mEnter a month (January - June) or select a number:\n"
                    "1: January | 2: February | 3: March | 4: April | 5: May | 6: June | 7: All months\n"
                    "Your choice: \033[0m").strip().lower()

        if opt in months:
            month = opt
            break
        elif opt in month_options:
            month = month_options[opt]
            break
        else:
            print("\n\033[1;31mInvalid input. Please select a valid month option.\033[0m\n")

    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day_options = {str(i + 1): days[i] for i in range(len(days))}

    while True:
        opt = input("\n\033[1;36mEnter a day of the week (Monday - Sunday) or select a number:\n"
                    "1: Monday | 2: Tuesday | 3: Wednesday | 4: Thursday | 5: Friday | 6: Saturday | 7: Sunday | 8: All days\n"
                    "Your choice: \033[0m").strip().lower()

        if opt in days:
            day = opt
            break
        elif opt in day_options:
            day = day_options[opt]
            break
        else:
            print("\n\033[1;31mInvalid input. Please select a valid day option.\033[0m\n")

    print("\n\033[1;33m" + "-" * 40 + "\033[0m")
    return city, month, day

def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time']) #✅
    df['month'] = df['Start Time'].dt.month_name() #✅  
    df['day_of_week'] = df['Start Time'].dt.day_name() #✅

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month in months:
            df = df[df['month'] == month.title()]
            
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):

    """
    Displays statistics on the most frequent times of travel.
    Args:
        (DataFrame)df: Dataframe containing data for the selected city and filters(months/days).
    """

    print("\n📅 Fetching the most common travel times", end="")
    loading_animation()
    print('\n📅 Most Frequent Travel Times:\n')
    start_time = time.time()

    print(f'\033[1;32m🔹 Most Common Month:\033[0m {df["month"].mode()[0]}') #✅
    print(f'\033[1;34m🔹 Most Common Day:\033[0m {df["day_of_week"].mode()[0]}') #✅
    print(f'\033[1;36m🔹 Most Common Start Hour:\033[0m {df["Start Time"].dt.hour.mode()[0]}') #✅

    print(f"\n✅ Computed in {time.time() - start_time:.2f} seconds.")
    print('-'*50)

def station_stats(df):

    """
    Displays statistics on the most popular stations and trip.
    Args:
        (DataFrame)df: Dataframe containing data for the selected city and filters(months/days).
    """


    print("\n⏳ Fetching the most popular stations and routes...", end="")
    loading_animation()

    print('\n🚏 Popular Stations & Routes:\n')
    start_time = time.time()

    print(f'\033[1;32m🔹 Most Common Start Station:\033[0m {df["Start Station"].mode()[0]}') #✅
    print(f'\033[1;34m🔹 Most Common End Station:\033[0m {df["End Station"].mode()[0]}') #✅

    df['Trip'] = df['Start Station'] + " to " + df['End Station'] #✅
    print(f'\033[1;36m🔹 Most Frequent Trip:\033[0m {df["Trip"].mode()[0]}') #✅

    print(f"\n✅ Computed in {time.time() - start_time:.2f} seconds.")
    print('-'*50)

def trip_duration_stats(df):

    """
    Displays statistics on the total and average trip duration.
    Args:
        (DataFrame)df: Dataframe containing data for the selected city and filters(months/days).
    """

    print("\n⏳ Calculating total and average trip duration...", end="")
    loading_animation()

    print('\n⏳ Trip Duration Stats:\n')
    start_time = time.time()

    total_duration = df['Trip Duration'].sum() 
    avg_duration = df['Trip Duration'].mean()

    print(f'\033[1;32m🔹 Total Travel Time:\033[0m {total_duration / 3600:.2f} hours') #✅
    print(f'\033[1;34m🔹 Average Travel Time:\033[0m {avg_duration / 3600:.2f} hours') #✅

    print(f"\n✅ Computed in {time.time() - start_time:.2f} seconds.")
    print('-'*50)

def user_stats(df):

    """
    Displays statistics on bikeshare users.
    Args:
        (DataFrame)df: Dataframe containing data for the selected city and filters(months/days).
    """


    print("\n📊 Gathering user demographic insights...", end="")
    loading_animation()

    print('\n👥 User Demographics:\n')
    start_time = time.time()

    print('\033[1;32m🔹 User Type Counts:\033[0m')
    print(df['User Type'].value_counts().to_string(index=True), '\n')  # ✅

    if 'Gender' in df.columns:
        print('\033[1;34m🔹 Gender Distribution:\033[0m')
        print(df['Gender'].value_counts().to_string(index=True), '\n')  # ✅
    else:
        print('\033[1;34m🔹 Gender Distribution:\033[0m Data not available for this city.\n')  # ✅

    if 'Birth Year' in df.columns:
        print(f'\033[1;36m🔹 Earliest Birth Year:\033[0m {int(df["Birth Year"].min())}')  # ✅
        print(f'\033[1;36m🔹 Most Recent Birth Year:\033[0m {int(df["Birth Year"].max())}')  # ✅
        print(f'\033[1;36m🔹 Most Common Birth Year:\033[0m {int(df["Birth Year"].mode()[0])}')  # ✅
    else:
        print('\033[1;36m🔹 Birth Year Data:\033[0m Not available for this city.')  # ✅

    print(f"\n✅ Computed in {time.time() - start_time:.2f} seconds.")
    print('-' * 50)

def display_raw_data(df):

    """
    Displays raw data for the user to explore.
    Args:
        (DataFrame)df: Dataframe containing data for the selected city and filters(months/days).
    """

    i = 0
    while True:
        show_data = input("\nWould you like to see raw data? Enter 'yes' to continue or anything else to skip: ").strip().lower()
        if show_data != 'yes':
            break

        if i >= len(df):  #✅ 
            print("\n🚨 No more data to display!")
            break

        print("\n📄 Displaying raw data (5 rows):\n")
        print(df.iloc[i:i+5].to_string(index=False))  #✅ 
        i += 5

def main():
    while True:
        print("\n\033[1;35m🔎 Gathering your data, please hold on...\033[0m")
        city, month, day = get_filters()
        df = load_data(city, month, day)

        print("\n\033[1;34m🚀 Analyzing statistics for your selected filters...\033[0m\n")
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_raw_data(df)

        print("\n\033[1;33m" + "="*50 + "\033[0m") 
        print("\n\033[1;32m🎯 Hope you found the insights you were looking for! 🚲💨\033[0m")  

        restart = input("\n\033[1;36m🔄 Would you like to explore more data? Type 'yes' or 'y' to continue: \033[0m").strip().lower()
        if restart not in ['yes', 'y']:
            print("\n\033[1;31m🌟 Thank you for exploring US BikeShare data! Stay safe & ride on! 🚴‍♂️✨\033[0m\n")
            break

if __name__ == "__main__":
	main()
