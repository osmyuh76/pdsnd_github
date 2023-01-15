import time
import pandas as pd
import numpy as np

path = ''

CITY_DATA = { 'Chicago':  'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

#All valid entries
months = ('All','January', 'February', 'March','April','May','June')

cities = ('Chicago', 'New York City', 'Washington')

week_days = ('All','Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday','Sunday')

yes_no = ('Yes','No')


# Validate all the user inputs
def valid_entry(msg, valid_ans):
    while True:
        try:
            user_input = input(msg + ' '+ str(valid_ans) + ': ')
            if user_input.title() in valid_ans:
                return user_input.title()
            print("\nThe option {} is not valid, let's try again!".format(user_input))
        except ValueError:
            print("\nInvalid input, please enter a valid option.")

# user input (cities selection)
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city = ''
    month = ''
    day= ''

    print('\nHello! Let\'s explore some US bikeshare data!')

    # Validate the city of study
    userInput = valid_entry("\nEnter the name of the city of Study ", cities)
    city = userInput.title()
    print("\nYou select {}, let's select the month\n".format(city))


    # Validate the months of study
    userInput = valid_entry("\nEnter the month of Study ", months)
    month = userInput.title()
    print("\nYou select {}, let's select the week day now\n".format(month))


    # Validate the day of the week
    userInput = valid_entry("\nEnter the day of week ", week_days)
    day = userInput.title()
    print("\nYou select {}, let's select see the results now\n".format(day))


    print('-'*40)
    return city, month, day

# take the user input and load the file matching the selection from user
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
# query the city based on the user input
    file = CITY_DATA[city]
    df = pd.read_csv(file)

    # convert hour from collum 'Start Time'
    df['Hour'] = pd.to_datetime(df['Start Time']).dt.hour

    # filter month based on user input
    if month == 'All':
        df['Month'] = pd.to_datetime(df['Start Time']).dt.month_name()

    else:
        df['Month'] = pd.to_datetime(df['Start Time']).dt.month_name()
        df = df[df['Month'] == month]

    # filter week day based on user input
    if day == 'All':
        df['Weekday'] = pd.to_datetime(df['End Time']).dt.day_name()
    else:
        df['Weekday'] = pd.to_datetime(df['End Time']).dt.day_name()
        df = df[df['Weekday']==day]

    print('You select data for {} month {} and day of the week:{}'.format(city,month,day))


    return df

# Receives pandas dataframe as argument and display some qustions
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['Month'].mode()[0]
    print('Most common month:', popular_month)

    # TO DO: display the most common day of week
    popular_day_week = df['Weekday'].mode()[0]
    print('Most common day of week:', popular_day_week)

    # TO DO: display the most common start hour
    popular_hour = df['Hour'].mode()[0]
    print('Most common start hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# receives pandas dataframe and display some station qustions
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most popular used start station:', popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most popular used end station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_end_station_comb = (df['Start Station'] + " to " + df['End Station']).mode()[0]
    print('Most frequent combination of start station and end station trip:', popular_end_station_comb)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Receives pandas dataframe and display some trip question
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total travel time:', total_travel)

    # TO DO: display mean travel time
    average_travel = df['Trip Duration'].mean()
    print('Average travel time:', average_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Receives pandas dataframe and display some user qustions
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    df.groupby(['User Type'])['Start Time'].count()
    user = df.groupby(['User Type'])['Start Time'].count()
    print('\n',user)

    # TO DO: Display counts of gender
    try:
        df.groupby(['Gender'])['Start Time'].count()
        gender = df.groupby(['Gender'])['Start Time'].count()
        print('\n',gender)

    except KeyError:
        print('\nDo not have gender data for this city!')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        common_birth_year = df['Birth Year'].mode()[0]
        print('\nMost common year of birth:', common_birth_year)

        min_birth_year = df['Birth Year'].min()
        print('Earliest year of birth:', min_birth_year)

        max_birth_year = df['Birth Year'].max()
        print('Most recent year of birth:', max_birth_year)

    except KeyError:
        print('Do not have birth year data for this city!')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Display data from the panda series
def show_data(df):

    view_data = valid_entry('\nWould you like to view 5 rows of individual trip data? Enter from: ', yes_no)

    loc = 0

    while view_data == 'Yes':
        print('\n',df.iloc[loc : loc+5])

        view_data = valid_entry('\nWould you like to view 5 rows of individual trip data? Enter from: ', yes_no)
        loc += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = valid_entry('\nWould you like to restart? Enter', yes_no)
        if restart.lower() != 'yes':
            print('\n\nThank you to use this little program!')
            break


if __name__ == "__main__":
	main()
