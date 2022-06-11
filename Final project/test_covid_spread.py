from covid_spread import read_dict, get_data_country, get_data_vac, correct_vac, get_data_state, get_data_vac_state
from os import path
import pytest


def test_read_dict():
    """Verify that the read_dict function works correctly.
    Parameters: none
    Return: nothing
    """

    # Call the read_dict function which will read the global_data.csv
    # file and create and return a list.
    filename = path.join(path.dirname(__file__), "global_data.csv")
    countries = read_dict(filename)

    # Verify the correctness of the five items in the dictionary.
    assert countries[0] == ["2020-01-03", "AF", "Afghanistan", "EMRO", "0", "0", "0", "0"]
    assert countries[695] == ["2021-11-28" , "AF", "Afghanistan", "EMRO", "19", "157190", "1", "7308"]
    assert countries[-1] == ["2021-12-06", "ZW", "Zimbabwe", "AFRO", "523", "139046", "1", "4710"] 
    assert countries[148793] == ["2020-09-08" ,"GB", "The United Kingdom","EURO","2447","355504","3","41554"]  
    assert countries[135075] == ["2021-09-05","SC","Seychelles","AFRO","59","20340","0","103"]


def test_get_data_country():
    """Verify that the get_data_country function works correctly.
    Parameters: none
    Return: nothing
    """
    filename = path.join(path.dirname(__file__), "global_data.csv")
    countries = read_dict(filename)
    assert get_data_country("United States of America", countries) == "For United States of America by 2021-12-06: \n\
48702375 cumulative cases of Covid-19. \n\
781265 cumulative deaths caused by Covid-19."

    assert get_data_country("Chile", countries) == "For Chile by 2021-12-06: \n\
1772547 cumulative cases of Covid-19. \n\
38501 cumulative deaths caused by Covid-19."
    assert get_data_country("Chil", countries) == "Chil does not exist or has no data. Please check your spelling."
    assert get_data_country("Argentina", countries) == "For Argentina by 2021-12-06: \n\
5339382 cumulative cases of Covid-19. \n\
116643 cumulative deaths caused by Covid-19."


def test_get_data_vac():
    """Verify that the get_data_vac function works correctly.
    Parameters: none
    Return: nothing
    """
    filename = path.join(path.dirname(__file__), "data.csv")
    vacs = read_dict(filename)
    vaccinations = correct_vac(vacs)
    assert get_data_vac("Chile", vaccinations) == print("In Chile by 2021-12-05 16903669 people have been vaccinated.")
    assert get_data_vac("Peru", vaccinations) == print("In Peru by 2021-12-04 22749614 people have been vaccinated.")
    assert get_data_vac("Somalia", vaccinations) == print("In Somalia by 2021-11-13 589128 people have been vaccinated.")
    assert get_data_vac(" ", vaccinations) == print("  not in list of vaccinated countries")


def test_get_data_state():
    """Verify that the get_data_state function works correctly.
    Parameters: none
    Return: nothing
    """
    filename = path.join(path.dirname(__file__), "us-states.csv")
    states = read_dict(filename)
    assert get_data_state("Florida", states) == "For the state of Florida by 2021-12-06: \n\
3702338 cumulative cases of Covid-19. \n\
61789 cumulative deaths caused by Covid-19."
    assert get_data_state("North Carolina", states) == "For the state of North Carolina by 2021-12-06: \n\
1553349 cumulative cases of Covid-19. \n\
18870 cumulative deaths caused by Covid-19."
    assert get_data_state("Abc", states) == "Abc does not exist or has no data. Please check your spelling."
    assert get_data_state("Kentucky", states) == "For the state of Kentucky by 2021-12-06: \n\
804568 cumulative cases of Covid-19. \n\
11381 cumulative deaths caused by Covid-19."


def test_get_data_vac_state():
    """Verify that the read_dict function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the read_dict function which will read the us_vacs.csv
    # file and create and return a list.
    filename = path.join(path.dirname(__file__), "us_vacs.csv")
    vaccinations = read_dict(filename)
    assert get_data_vac_state("Wyoming", vaccinations) == print("In Wyoming by 2021-12-10 316040 people have been vaccinated.")
    assert get_data_vac_state("Utah", vaccinations) == print("In Utah by 2021-12-10 2103796 people have been vaccinated.")
    assert get_data_vac_state("Virgin Islands", vaccinations) == print("In Virgin Islands by 2021-12-10 61503 people have been vaccinated.")
    assert get_data_vac_state(" ", vaccinations) == print("  not in list of vaccinated states")


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])