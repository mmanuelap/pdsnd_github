import time
import pandas as pd
import numpy as np
import calendar
#importing calendar module to get month name on time_stats

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city_names = ['chicago', 'new york city', 'washington']
month_names = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
day_names = ['all', 'sunday', 'monday', 'tuesday',
             'wednesday', 'thrusday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    try:
        city = input('Which city should we begin with? Chicago, New York City, or Washington?\n').lower()
        while city not in city_names:
            print('That\'s not a valid city!\n')
            city = input('Type \"Chicago\", \"New York\", or \"Washington\": ').lower()
        print('You selected', city.title(),', thank you!\n')
    except e:
        print('The exception \"{}\" occurred'.format(e))
        
    # TO DO: get user input for month (all, january, february, ... , june)
    try:
        month = input('What about a timeframe? You can filter by a month (January to June) or type \"all\" to see everything: \n').lower()
        while month not in month_names:
            print('That\'s not a valid filter!\n')
            month = input('Type a month from January to June, or \"all\" to see the data unfiltered: \n').lower()
        print('You selected', month.title(),', thank you!')
    except e:
        print('The exception \"{}\" occurred'.format(e))
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    try:
        day = input('\nLastly, you can filter by day of the week (e.g. Sunday), or type \"all\" to see everything: \n').lower()
        while day not in day_names:
            print('That\'s not a valid filter!\n')
            day = input('Type a day of the week or type \"all\" to see the data unfiltered: \n').lower()
        print('You selected ', day.title(),', thank you!')
    except e:
        print('The exception \"{}\" occurred'.format(e))
            
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
    # convert the Start and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    common_month = calendar.month_name[common_month]
    print('Most Frequent Month: ', common_month)

    # TO DO: display the most common day of week
    common_weekday = df['day_of_week'].mode()[0]
    print('Most Frequent Day of Week: ', common_weekday)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("Most Popular Start Station: ", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("\nMost Popular End Station: ", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print("\nMost Popular Trip: \n{}".format(popular_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = int(df['Trip Duration'].sum() / 60 / 60 / 24)
    print('Total Travel Time is {} days.'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = (df['Trip Duration'].mean()) / 60
    mean_travel_time = mean_travel_time.round(2)
    print('Average travel time is {} minutes.'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    try:
        # TO DO: Display counts of user types
        user_types = df['User Type'].value_counts()
        print('Users by Type:\n', user_types)

        # TO DO: Display counts of gender
        users_by_gender = df['Gender'].value_counts()
        print('\nUsers by Gender:\n', users_by_gender)
        
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print('\nEarliest Birth Year:', earliest_year)
        print('\nMost Recent Birth Year:', most_recent_year)
        print('\nMost Common Birth Year:', most_common_year)
    
    except KeyError:
        print('\nNo other data available for the selected city.')
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays rows of raw data if the users chooses to."""
    i = 0
    raw = input('\nWould you like to see rows of raw data? Type \"yes\" or \"no\"\n').lower()
    pd.set_option('display.max_columns',200)
    while True:
        if raw not in ['yes', 'no']:
            print('\nNot a valid input! Try again.')
            raw = input('Would you like to see rows of raw data? Type \"yes\" or \"no\"\n').lower()
            continue
        elif raw == 'no':
            break
        else:
            print(df[i:i+5])
            raw = input('\nWould you like to see the next rows of raw data? Type \"yes\" or \"no\"\n').lower()
            i += 5

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
