import csv

def main():
    # Read the contents of a CSV file named global_data.csv
    # into a compound list named countries. 
    countries = read_dict("global_data.csv")
    # Read the contents of a CSV file named data.csv
    # into a compound list named vaccinations.
    vaccinations = read_dict("data.csv")
    # Correct the list of vaccinated countries by changing the names of some counties 
    # to be the same as in countries list
    vaccinations = correct_vac(vaccinations)
    # Read the contents of a CSV file named us-states.csv
    # into a compound list named states. 
    states = read_dict("us-states.csv")
    #print(states)
    # Read the contents of a CSV file named us-vacs.csv
    # into a compound list named vac_states. 
    state_vaccinations = read_dict("us_vacs.csv")

    print("\nThis program allows you to get the information about number of covid infected \n\
people as well as covid caused deaths, by country or by state in the US. You can also \n\
learn how many people have been vaccinated in the place of your interest.")
    prompt1 = None
    while prompt1 == None:
        prompt1 = input("\nWould you like to see the information about country or state in the US? (C/S): ")
        if prompt1.lower() == "c":
            country_name = input("What country would you like to see the data about? \n\
(please spell the full and correct name): ")
            result = get_data_country(country_name, countries)
            print(result)
            if result != f"{country_name} does not exist or has no data. Please check your spelling.":
                prompt2 = None
                while prompt2 == None:
                    prompt2 = input(f"Would you like to see how many people have been vaccinated in {country_name}? (Y/N): ")
                    if prompt2.lower() == "y":
                        get_data_vac(country_name, vaccinations)
                        prompt3 = None
                        while prompt3 == None:
                            prompt3 = input("\nWould you like to check some other place? (Y/N): ")
                            if prompt3.lower() == "y":
                                prompt1 = None
                            elif prompt3.lower() == "n":
                                print("Ok. Thanks for using this program.")
                            else:
                                print("Incorrect answer...")
                                prompt3 = None
                    elif prompt2.lower() == "n":
                        prompt3 = None
                        while prompt3 == None:
                            prompt3 = input("\nWould you like to check some other place? (Y/N): ")
                            if prompt3.lower() == "y":
                                prompt1 = None
                            elif prompt3.lower() == "n":
                                print("Ok. Thanks for using this program.")
                            else:
                                print("Incorrect answer...")
                                prompt3 = None
                    else:
                        print("Incorrect answer...")
                        prompt2 = None
            else:
                prompt3 = None
                while prompt3 == None:
                    prompt3 = input("\nWould you like to check some other place? (Y/N): ")
                    if prompt3.lower() == "y":
                        prompt1 = None
                    elif prompt3.lower() == "n":
                        print("Ok. Thanks for using this program.")
                    else:
                        print("Incorrect answer...")
                        prompt3 = None
        
        elif prompt1.lower() == "s":
            state_name = input("What state would you like to see the data about? \n\
(please spell the full and correct name): ")
            result = get_data_state(state_name, states)
            print(result)
            if result != f"{state_name} does not exist or has no data. Please check your spelling.":
                prompt2 = None
                while prompt2 == None:
                    prompt2 = input(f"Would you like to see how many people have been vaccinated in {state_name}? (Y/N): ")
                    if prompt2.lower() == "y":
                        get_data_vac_state(state_name, state_vaccinations)
                        prompt3 = None
                        while prompt3 == None:
                            prompt3 = input("\nWould you like to check some other place? (Y/N): ")
                            if prompt3.lower() == "y":
                                prompt1 = None
                            elif prompt3.lower() == "n":
                                print("Ok. Thanks for using this program.")
                            else:
                                print("Incorrect answer...")
                                prompt3 = None
                    elif prompt2.lower() == "n":
                        prompt3 = None
                        while prompt3 == None:
                            prompt3 = input("\nWould you like to check some other place? (Y/N): ")
                            if prompt3.lower() == "y":
                                prompt1 = None
                            elif prompt3.lower() == "n":
                                print("Ok. Thanks for using this program.")
                            else:
                                print("Incorrect answer...")
                                prompt3 = None
                    else:
                        print("Incorrect answer...")
                        prompt2 = None
            else:
                prompt3 = None
                while prompt3 == None:
                    prompt3 = input("\nWould you like to check some other place? (Y/N): ")
                    if prompt3.lower() == "y":
                        prompt1 = None
                    elif prompt3.lower() == "n":
                        print("Ok. Thanks for using this program.")
                    else:
                        print("Incorrect answer...")
                        prompt3 = None
        else:
            print("Incorrect answer...")
            prompt1 = None


def get_data_country(country_name, countries):
    """ Function that retrieves and returns data from 
    the compound list of countries about the number of 
    cases of and deaths due to covid-19 by the country """
    try:
        # Indexes of some of the columns
        # in the global_data.csv file.
        date_index = 0
        country_index = 2
        cumulative_cases_index = 5
        cumulative_death_index = 7
        
        cumulative_cases = 0
        cumulative_cases_date = None
        cumulative_deaths_date = None
        cumulative_deaths = 0 

        #country_name = country_name.capitalize()
        
        # Loop through the list of countries and retrieve the data about country of choice
        for country in countries:
            if country[country_index] == country_name :
                country[cumulative_cases_index] = float(country[cumulative_cases_index])
                if country[cumulative_cases_index] >= cumulative_cases:
                    cumulative_cases = country[cumulative_cases_index]
                    cumulative_cases_date = country[date_index]
                
                country[cumulative_death_index] = float(country[cumulative_death_index])
                if country[cumulative_death_index] >= cumulative_deaths:
                    cumulative_deaths = country[cumulative_death_index] 
                    cumulative_deaths_date = country[date_index]

        # all counties have covid cases. If they have not been indicated, the name of
        # country was misspelled
        if cumulative_cases == 0:
            result = f"{country_name} does not exist or has no data. Please check your spelling."
        else:
            result = f"For {country_name} by {cumulative_cases_date}: \n\
{cumulative_cases:.0f} cumulative cases of Covid-19. \n\
{cumulative_deaths:.0f} cumulative deaths caused by Covid-19."

    except KeyError as key_err:
        print(type(key_err).__name__, key_err)    

    except IndexError as index_err:
        print(index_err)

    except ValueError as val_err:
        print(val_err)

    return result
    
    
def get_data_vac(country_name, vaccinations):
    """ Function that retrieves and returns data from 
    the compound list of countries and vaccinations about the number of 
    vaccinated people by country """
    try:
        # Indexes of some of the columns
        # in the global_data.csv file.
        vac_index = 4 
        country_index = 0
        date_index = 2
        vac_number = 0 
        date = None
        #create a list of all countries 
        country_names = []
        for i in vaccinations:
            country_name1 = i[country_index]
            country_names.append(country_name1)

        # Loop through the list of countries and vacs and retrieve the data about country of choice
        for i in vaccinations:
            if i[country_index] == country_name :
                if not i[vac_index].isdigit():
                    i[vac_index] = 0
                if float(i[vac_index]) >= vac_number:
                    vac_number = float(i[vac_index])
                    date = i[date_index]

        if country_name not in country_names:
            print(f"{country_name} not in list of vaccinated countries")
        else:
            print(f"In {country_name} by {date} {vac_number:.0f} people have been vaccinated.")        
    
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)    

    except IndexError as index_err:
        print(index_err)

    except ValueError as val_err:
        print(val_err)


def read_dict(filename):
    """Read the contents of a CSV file into a compound list
    and return the compound list.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
        
    Return: a compound list that contains
        the contents of the CSV file.
    """
    try:
        # Create an empty list that will
        # store the data from the CSV file.
        list = []

        # Open the CSV file for reading and store a reference
        # to the opened file in a variable named csv_file.
        with open(filename, "rt") as csv_file:

            # Use the csv module to create a reader object
            # that will read from the opened CSV file.
            reader = csv.reader(csv_file)
            
            # The first line of the CSV file contains column
            # headings and not information, so this statement
            # skips the first line of the CSV file.
            next(reader)
            
            # Read the rows in the CSV file one row at a time.
            # The reader object returns each row as a list.
            for row in reader:
                
                list.append(row)
        
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)

    except FileNotFoundError as not_found_err:
        print(f"Error: cannot open csv file"
                " because it doesn't exist.") 

    except PermissionError as perm_err:
        print(f"Error: cannot read from csv file"
                " because you don't have permission.")    

    except IndexError as index_err:
        print(index_err)
    
    # Return the compound list.
    return list


def correct_vac(vaccinations):
    """Function that corrects the names of some counties in vaccinations compound list
    parameters: 
        vaccinations: compound list to correct
    return:
        corrected list"""
    
    for i in vaccinations:
        if i[0] == "Russia":
            i[0] = "Russian Federation"
        if i[0] == "United States":
            i[0] = "United States of America"
    
    return vaccinations


def get_data_state(state_name, states):
    """ Function that retrieves and returns data from 
    the compound list of states about the number of 
    cases of and deaths due to covid-19 by the state in the US """
    try:
        # Indexes of some of the columns
        # in the us-states.csv file.
        date_index = 0
        state_index = 1
        cases_index = 3
        death_index = 4
        
        cumulative_cases = 0
        date = None
        cumulative_deaths = 0 

        #create a list of all states
        state_names = []
        for state in states:
            state_name1 = state[state_index]
            state_names.append(state_name1) 

        # Loop through the list of states and retrieve the data about state of choice
        for state in states:
            if state[state_index] == state_name :
                if not state[cases_index].isdigit():
                    state[cases_index] = 0
                state[cases_index] = float(state[cases_index])
                if state[cases_index] >= cumulative_cases:
                    cumulative_cases = state[cases_index]
                    date = state[date_index]
                
                if not state[death_index].isdigit():
                    state[death_index] = 0
                state[death_index] = float(state[death_index])
                if state[death_index] >= cumulative_deaths:
                    cumulative_deaths = state[death_index]
                    

        # all counties have covid cases. If they have not been indicated, the name of
        # country was misspelled
        if state_name not in state_names:
            result = f"{state_name} does not exist or has no data. Please check your spelling."
        else:
            result = f"For the state of {state_name} by {date}: \n\
{cumulative_cases:.0f} cumulative cases of Covid-19. \n\
{cumulative_deaths:.0f} cumulative deaths caused by Covid-19."

    except KeyError as key_err:
        print(type(key_err).__name__, key_err)    

    except IndexError as index_err:
        print(index_err)

    except ValueError as val_err:
        print(val_err)

    return result


def get_data_vac_state(state_name, state_vaccinations):
    """ Function that retrieves and returns data from 
    the compound list of states and vaccinations about the number of 
    vaccinated people by state.
    Parameters:
        state_name: the name of state we are searching the data of.
        state_vaccinations: compound list containing information about vaccinations for all atates """
    try:
        # Indexes of some of the columns
        # in state_vaccinations.
        vac_index = 4 
        state_index = 1
        date_index = 0
        vac_number = 0 
        date = None

        #create a list of all states
        state_names = []
        for state in state_vaccinations:
            state_name1 = state[state_index]
            state_names.append(state_name1)

        # Loop through the list of states and vacs and retrieve the data about state of choice
        for i in state_vaccinations:
            if i[state_index] == state_name:
                if i[date_index] == "2021-12-10":    
                    vac_number = i[vac_index]
                    date = i[date_index]

        if state_name not in state_names:
            print(f"{state_name} not in list of vaccinated states")
        else:
            print(f"In {state_name} by {date} {vac_number[:-2]} people have been vaccinated.")
    
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)    

    except IndexError as index_err:
        print(index_err)

    except ValueError as val_err:
        print(val_err)
    

# Call main to start this program.
if __name__ == "__main__":
    main()