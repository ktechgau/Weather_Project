import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
         and celcius symbols.

     Args:
         temp: A string representing a temperature.
     Returns:
         A string contain the temperature and "degrees celcius."
     """
    return f"{temp}{DEGREE_SYBMOL}"


from datetime import datetime



def convert_date(iso_string):
    datetime_object = datetime.fromisoformat(iso_string)
    formatted_date = datetime_object.strftime("%A %d %B %Y")
    return formatted_date
 
"""Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
pass


def convert_f_to_c(temp_in_farenheit):
    to_cel = (float(temp_in_farenheit) - 32)* 5/9
    return round(to_cel,1) #rounds the float to 1dp
    
"""Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
        
     
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
pass


def calculate_mean(weather_data):

    weather_list = []   #for-loop to convert items in a list to float
    for items in weather_data:
        weather_list.append(float(items))

    mean = (sum(weather_list)/(len(weather_list)))
    return mean #calculating mean

"""Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
pass

 
def load_data_from_csv(csv_file):

    new_list=[]

    with open(csv_file) as csvopen:

        reader = csv.reader(csvopen)
        next(reader)

        for item in reader:
            if item: #check for empty rows and skips 
                date = item[0]
                min = int(item[1])  #converting index items 1 and 2 to integers, leaving index 0 as string as per example
                max = int(item[2])
                new_list.append([date,min,max])
   
    return (new_list)
        
"""Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
pass


def find_min(weather_data):

    if not weather_data:    #returning empty if no data in temperatures
            return()

    temp_data = []  #placing data in list as float
    
    for items in weather_data:
        temp_data.append(float(items))
    
    min_val = min(temp_data)    #finding max

    last_index = None   #initialise last index

    for index, item in enumerate(temp_data):    #iterating through list for multiple same values
        if item == min_val:
            last_index = index
    
    return (min_val, last_index)

"""Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
pass


def find_max(weather_data):

    if not weather_data:    #returning empty if no data in temperatures
            return()

    temp_data = []  #placing data in list as float
    
    for items in weather_data:
        temp_data.append(float(items))
    
    max_val = max(temp_data)    #finding min

    last_index = None   #initialise last index

    for index, item in enumerate(temp_data):    #iterating through list for multiple same values
        if item == max_val:
            last_index = index
    
    return (max_val, last_index)


"""Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
pass


def generate_summary(weather_data):

    dates_list = []
    min_list = []
    max_list = []
    day = len(weather_data)

    for row in weather_data:    #data to list
        dates = row[0]
        min = row[1]
        max = row[2]

        dates_list.append(dates)
        min_list.append(min)
        max_list.append(max)

# #setting variables and calling functions for min, max, date conversions
   
    low_temp = (find_min(min_list) ) #note: find_min has data eg 47, 0
    high_temp = (find_max(max_list))
    convert_low_temp = format_temperature(convert_f_to_c(low_temp[0]))
    convert_high_temp = format_temperature(convert_f_to_c(high_temp[0]))
    low_date = convert_date(dates_list[low_temp[1]])
    high_date = convert_date(dates_list[high_temp[1]])
    average_low = format_temperature(convert_f_to_c(calculate_mean(min_list)))
    average_high = format_temperature(convert_f_to_c(calculate_mean(max_list)))

    return f"{day} Day Overview\n  The lowest temperature will be {convert_low_temp}, and will occur on {low_date}.\n  The highest temperature will be {convert_high_temp}, and will occur on {high_date}.\n  The average low this week is {average_low}.\n  The average high this week is {average_high}.\n"



"""Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
pass


def generate_daily_summary(weather_data):
    
    daily_summary = ""
    
    for row in weather_data:  #by using for loop, all these instrucitons will iterate over each row 
        date = convert_date(row[0]) #converting date format using function
        min_temp = format_temperature(convert_f_to_c(row[1])) #finding min
        max_temp = format_temperature(convert_f_to_c(row[2])) #finding max

        #So far, the loop only returns a summary only after the loop is complete which in turn
        #only generates the last daily summary. Do a += like counting and storing the counts. 
        #Thank goodness for ChatGPT
        
        daily_summary +=f"---- {date} ----\n  Minimum Temperature: {min_temp}\n  Maximum Temperature: {max_temp}\n\n"

    return daily_summary
# FINAL NOTES: I propose that the very underwhelming "OK" when we pass the tests be changed to 
#   something bigger, we deserve fireworks for the brain power required here 😆🎉


"""Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """    
pass
