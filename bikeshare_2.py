import time
import pandas as pd
import numpy as np

CITY_DATA = { 'ch': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'wa': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("Kindly specify a city by typing: (ch) for chicago or (ny) for new york city or (wa) for washington: \n\n").lower()
        if city in CITY_DATA.keys():
            break
        else:
            print("That's invalid input...")

    # get user input for month (all, january, february, ... , june)

    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'all']
    while True:
        month = input('\n\nTo filter data by a particular month, please type the month:\n- (jan) for January\n- (feb) for February\n- (mar) for March\n- (apr) for April\n- (may) for May\n- (jun) for June\n- (all) for all months\n\n').lower()
        if month in months:
            break
        else:
            print("That's invalid input...")

    # get user input for day of week (all, monday, tuesday, ... sunday)

    days = ['sat', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'all']
    while True:
        day = input('\n\nTo filter data by a particular day, please type the day:\n- (sat) for Saturday\n- (sun) for Sunday\n- (mon) for Monday\n- (tue) for Tuesday\n- (wed) for Wednesday\n- (thu) for Thursday\n- (fri) for Friday\n- (all) for all days\n\n').lower()
        if day in days:
            break
        else:
            print("That's invalid input...")

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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':

        # filter by month to create the new dataframe
        df = df[df['month'].str.startswith(month.title())]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'].str.startswith(day.title())]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city):
    """Displays raw data base on user inputs."""

    df = pd.read_csv(CITY_DATA[city])
    print('\nRaw data is available to check...\n')
    start_loc = 0
    while True:
        display_opt = input('To view the available raw data in chunks of 5 rows type yes \n').lower()
        if display_opt not in ['yes' , 'no']:
            print("That's invalid choice, please type yes or no")

        elif display_opt == 'yes':
            print(df.iloc[start_loc : start_loc + 5])
            start_loc += 5

        elif display_opt == 'no':
            print('\nExisting...')
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(city, month, day)
        print(df)
        #time_stats(df)
        #station_stats(df)
        #trip_duration_stats(df)
        #user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
