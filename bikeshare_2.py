import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
VALID_MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
VALID_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters(city, month, day):
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!/n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nwould you like see date for Chicago , New york city, or Washington\n').lower()
        if city not in CITY_DATA:
            print("\nInvalid answer\n")
            continue
        else:
            break
    # get user input for month (all, january, february, ... , june)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        time = input("Would you like to filter the data by month ,day , all or none ?\n").lower()
        if time == 'month':
            month = input("Which month? January, February, March, April, May or June\n").lower()
            day = 'all'
            if month not in VALID_MONTHS:
                print("\n Invalid answer. Please type it again.\n ")
                continue
            else:
                break
            break

        elif time == 'day':
            month = 'all'
            day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday\n").lower()
            if day not in VALID_DAYS:
                print("\n Invalid answer. Please type it again.\n ")
                continue
            else:
                break
            break

        elif time == 'all':
            month = input("Which month? January, Feburary, March, April, May or June\n").lower()
            day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday\n").lower()
            if month not in VALID_MONTHS:
                print("\n Invalid answer. Please type it again.\n ")
                continue

            elif day not in VALID_DAYS:
                print("\n Invalid answer. Please type it again.\n ")
                continue
            else:
                break
            break
        elif time == 'none':
            month = 'all'
            day = 'all'
            break
        else:
            input("\n Invalid answer. Please type it again.\n ")
            continue

    print('The city is :', city)
    print('Month of : ', month)
    print('Day of : ', day)
    print('-' * 40)
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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is month number : ', common_month)

    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day is : ', common_day_of_week)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most Popular Start Sation : ', common_start)

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most Popular End Sation : ', common_end)

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print('Most Popular combination Sation : ', common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print('The total travel : ', total_travel)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('The average travel time : ', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("There is no gender information in this city.")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = df['Birth Year'].min()
        print('The oldest customers birth year is : ', earliest)
        recent = df['Birth Year'].max()
        print('The youngest customers birth year is : ', recent)
        common_birth = df['Birth Year'].mode()[0]
        print('The Popular brith year is : ', pocommon_birth)
    else:
        print("There is no birth year information in this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


"""Asking for 5 lines of the raw data"""


def data(df):
    raw_data = 0
    while True:
        answer = input("Do you want to see the raw data? Yes or No\n").lower()
        if answer not in ['yes', 'no']:
            answer = input("You wrote the wrong word. Please type Yes or No.\n").lower()
        elif answer == 'yes':
            raw_data += 5
            print(df.iloc[raw_data: raw_data + 5])
            again = input("Do you want to see more? Yes or No\n").lower()
            if again == 'no':
                break
        elif answer == 'no':
            return


def main():
    city = ""
    month = ""
    day = ""
    while True:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()