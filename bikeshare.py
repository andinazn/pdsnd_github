"""Bikeshare Project by Udacity for Intro to Python Programming"""

import time
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = str(input('Enter a city: ')).lower()
            break
        except ValueError:
            print('Not a valid city!')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input('Enter a month: ')).lower()
            break
        except ValueError:
            print('Not a valid month!')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = str(input('Enter a day of week: ')).lower()
            break
        except ValueError:
            print('Not a valid day!')

    print('-'*40)
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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df [df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df [df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    #df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    #df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Frequent Start Month: {}'.format(popular_month))


    # TO DO: display the most common day of week
    #df['day_of_week'] = df['Start Time'].dt.day_of_week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Frequent Start Day of Week: {}'.format(popular_day_of_week))

    # TO DO: display the most common start hour
    #df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour: {}'.format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Frequent Start Station: {}'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Frequent End Station: {}'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    popular_combination = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('Most Frequent Trip Combination: {}'.format(popular_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['Trip Duration'] = pd.to_numeric(df['Trip Duration'])

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('\nThe total travel time: {}'.format(total_trip_duration))

    # TO DO: display mean travel time
    mean_trip_duration = df['Trip Duration'].mean()
    print('\nThe average travel time: {}'.format(mean_trip_duration))
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The Count of User Type: {}'.format(user_types))

    # TO DO: Display counts of gender
    gender_types = df['Gender'].value_counts()
    print('The Count of Gender: {}'.format(gender_types))

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year = df['Birth Year'].min()
    most_recent_year = df['Birth Year'].max()
    most_common_year = df['Birth Year'].mode()

    print('\nThe earliest year of birth year: {}'.format(earliest_year))
    print('\nThe most recent birth year: {}'.format(most_recent_year))
    print('\nThe most common birth year: {}'.format(most_common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data for the user."""

    user_input = input('\nWould you like to see the raw data?\nPlease enter yes or no\n').lower()
    if user_input in ('yes', 'y'):
        i = 0
    while True:
        print(df.iloc[i:i+5])
        i += 5
        more_data = input('Would you like to see more data? Please enter yes or no: ').lower()
        if more_data not in ('yes', 'y'):
            break
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

"""
Well done! I think it is quite important to check data manually. However, it would be nice if we can see all columns. When I run the code, columns are collapsed, and only some of them are shown.
You can prevent this situation by adding this to your code:

pd.set_option('display.max_columns',200)
Here is another way to do this:

while True:
    display_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
    if display_data.lower() != 'yes':
        break
    print(tabulate(df_default.iloc[np.arange(0+i,5+i)], headers ="keys"))
    i+=5
As you see, I use a new library here, tabulate. So to use this, please also import the module:

from tabulate import tabulate
"""