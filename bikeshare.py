import time
import pandas as pd
import numpy as np
#import os
#os.getcwd()
#os.chdir("C:\\Users\\Richa\\Desktop\\nanodegree\\Python")
#os.listdir('.')


def get_filters():
    """
    Asks users to specify name of the city, month, and day they want to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to
    #handle invalid inputs
    city= input(f"Enter name of the city.Please choose from {list(CITY_DATA.keys())}: \n")

    while city.lower() not in CITY_DATA.keys():
        print (f"Please choose from available options!")
        city= input("Enter name of the city: \n")

    print(f"You have entered {city} as the city name")

    # get user input for month (all, january, february, ... , june)
    month= input("Enter name of the month between jan to june or enter 'all': \n")
    months= ['all', 'january','february', 'march', 'april', 'may', 'june']
    while month.lower() not in months:
        print(f'The value must be one of all, january, february, march, april, may, june ')
        month= input("Enter name of the month between january to june or enter 'all': \n")

    if month.lower() != "all":
            month= months.index(month.lower())
            print(f'you have selected the month of {months[month]}')
    else:
        print(f'you have selected all')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day= input("Enter the day you want to filter upon else enter all:\n")

    while day.lower() not in ['all','sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday']:
        print(f'The value must be one of all,sunday,monday,tuesday,wednesday,thursday,friday,saturday')
        day= input("Enter the day you want to filter upon else enter all:\n")
    print(f'you have selected the day of {day}')

    print('-'*40)
    return city.lower(), month, day.lower()

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
    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

    df= pd.read_csv(CITY_DATA[city],sep=",",parse_dates=['Start Time', 'End Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != "all":
        df = df[df['month'] == month]

    if day.lower()!="all":
        df = df[df['day_of_week'].str.lower()==day]

    return df

#load_data(*get_filters())

def data_snapshot(df):
    """Gives snapshot of data pulled
    df: name of the dataframe you want to inspect
    output: returns first five observations and based on input will provide additional rows
    """
    answer= input("Do you want to see raw data: yes/no ? ")
    i=0
    while answer.lower()=="yes":
        print(df[i:i+5])
        answer= input("Do you want to see more data: yes/no ? ")
        i+=5




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month= df["month"].mode()[0]
    print(f'Most common month is: {most_common_month}')
    # display the most common day of week
    most_common_dow= df['day_of_week'].mode()[0]
    print(f'Most common day of week is: {most_common_dow}')

    # display the most common start hour
    df["start_hour"]= df['Start Time'].dt.hour
    most_common_st_hr= df["start_hour"].mode()[0]
    print(f'Most common start hour is: {most_common_st_hr}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_startstation= df['Start Station'].mode()[0]
    print(f'most commonly used start station is: {common_startstation}')

    # display most commonly used end station
    common_endstation= df['End Station'].mode()[0]
    print(f'most commonly used end station is: {common_endstation}')

    # display most frequent combination of start station and end station trip
    df["combined"]= df['Start Station']+"-"+ df['End Station']
    combine_start_end=  df["combined"].mode()[0]
    print(f'most frequent combination of start station and end station trip is: {combine_start_end}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df["total_travel_time"]= df['End Time']-df['Start Time']
    tot_time= np.sum(df["total_travel_time"])
    print(f'total travel time is : {tot_time}')

    # display mean travel time
    mean_travel_time= np.mean(df["total_travel_time"])
    print(f'Mean travel time is: {mean_travel_time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Frequency distribution of User types is: \n',df['User Type'].value_counts())

    # Display counts of gender
    if "Gender" in df.columns:
        print('Frequency distribution of Gender is: \n',df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print(f'Earliest year of birth is:\n',np.min(df['Birth Year']) )
        print(f'Recent year of birth is: \n', np.max(df['Birth Year']) )
        print(f"Most common year of birth is: {df['Birth Year'].value_counts().index[0]} with count of {df['Birth Year'].value_counts().values[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        data_snapshot(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
