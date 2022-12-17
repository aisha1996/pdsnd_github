import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new york', 'washington']

months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

days = ['sunday', 'monday', 'tuesday', 'wednesday',  'thursday', 'friday', 'saturday']

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
        city = input('Select a city do you want to explore Chicago, New York or Washington? \n> ').lower()
        if city not in cities:
            print("Wrong choice, Please choose from the list")
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Select a specific month january, february, march, april, may, june, OR all \n> ').lower()
        if month not in months:
            print("Wrong choice, Please choose from the list")
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Select a day sunday, monday, tuesday, wednesday,thursday, friday, saturday \n> ').lower()
        if day not in days:
           print("Wrong choice, Please choose from the list")
        else:
          break

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
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
    # display the most common month
    print("the most common month is \n{}\n".format(df['month'].mode()[0]))

    # display the most common day of week
    print("The most common day is \n{}\n".format(df['day_of_week'].mode()[0]))

    # display the most common start hour
    print("The most common start hour is \n {}\n".format(df['hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station is\n {}\n".format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print("The most commonly used end station is \n{}\n".format(df['End Station'].mode()[0]))


    # display most frequent combination of start station and end station trip
    combination = df.groupby(['Start Station','End Station'])
    print('The most frequent combination of start station and end station trip\n {}\n'.format(combination.size().sort_values(ascending=False).head(1)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time\n{}\n".format(df['Trip Duration'].sum()))

    # display mean travel time
    print("Mean travel time\n{}\n".format(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)


    # Display counts of gender
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print("counts of gender = " ,gender)
     # Display earliest, most recent, and most common year of birth
        print('Earliest  {}'.format(df['Birth Year'].mode()[0]))
        print('Most recent  {} '.format(df['Birth Year'].max()))
        print('Most common year of birth {} '.format(df['Birth Year'].min()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
    print(df.head())
    start_loc = 0
    while True:
        view_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_data.lower() != 'yes':
            return
        start_loc = start_loc + 5
        print(df.iloc[start_loc:start_loc+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()