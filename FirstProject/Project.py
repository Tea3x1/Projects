import numpy as np
import pandas as pd
import time
import re
from datetime import timedelta, date , datetime
from collections import Counter

# ---------------------------------- Input interactions -----------------------------------#
def input_data():
    print("*----------------------------Welcome!! To Bike share data from Motivate ----------------------------*")
    day_name = ""
    month_name = ""
    filtering_list = ["day","days","months","month","none","both"]
    city_list = ["chicago","new york city","washington"]
    months_list = ["january", "february", "march", "april", "may","june","jan", "feb", "mar", "jun", "apr"]
    another_months_list = ['august', 'september', 'october', 'november', 'december',"july","aug","sep","Oct","Dec","Nov"]
    days_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday","sunday","sun","mon", "tue", "wed", "thu", "fri", "sat",]
    #Asking the User to input which City they would like to search infromation about?
    city_name = input("\nPLease enter the city u would like to know information about  # Chicago, New york city, Washington \n-> ").lower()
    while True:
                if city_name not in city_list:
                    print("This is not a city name , Please enter a city name....\n")
                    city_name = input("Please type a correct city name! -> [Chicago, New york city, Washington] # if you want New york pls enter New york city\n-> ").lower()

                else:
                    break
    filtering = input("\nWould u like to filter it by Days or Months or both?  #If u dont want to filter it please type : None\n-> ")
    while True:
                if filtering.lower() not in filtering_list:
                    filtering = input("\nPlease type a correct filter! -> [ Days, Months, both or None]\n-> ")
                else: 
                    break

    if filtering.lower() == "none":
        return city_name, month_name, day_name, filtering
    
    elif filtering.lower() == "days" or filtering.lower() == "day":
        day_name = input("\nPlease type which day u would like to filter with?  #Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday\n-> ").lower()
        while True:
                    if day_name in days_list:
                        break
                    
                    else:
                        print("This is not a day name , Please enter a day name....\n")
                        day_name = input("Please type a correct day name! -> [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday]\n-> ").lower()


    elif filtering.lower() == "months" or filtering.lower() == "month":
        month_name = input("\nPlease type which month u would like to filter with? January, February, March, April, May, or June\n-> ").lower()
        while True:

                    if month_name in another_months_list:
                        print("\nSorry we dont have these months in this data , Please enter another month name....\n")
                        month_name = input("Please choose a month name from these! -> [January, February, March, April, May, or June]\n-> ").lower()
                        break
                    elif month_name not in months_list:
                        print("This is not a month name , Please enter a month name....\n")
                        month_name = input("Please type a correct month name! -> [January, February, March, April, May, or June]\n-> ").lower()
                        continue
                    
                    else:
                        break

    elif filtering.lower() == "both":
        month_name = input("\nPlease type which month u would like to filter with? January, February, March, April, May, or June\n-> ").lower()
        while True:
                    if month_name not in months_list:
                        print("This is not a month name , Please enter a month name....\n")
                        month_name = input("Please type a correct month name! -> [January, February, March, April, May, or June]\n-> ").lower()

                    else:
                        break                               
        day_name = input("\nPlease type which day u would like to filter with?  #Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday\n-> ").lower()
        while True:
                    if day_name not in days_list:
                        print("This is not a day name , Please enter a day name....\n")
                        day_name = input("Please type a correct day name! -> [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday]\n-> ").lower()

                    else:
                        break
   

    
    return city_name, month_name.title(), day_name.title(), filtering                 

# ---------------------------------- Filtering our data -----------------------------------#
def filtering_data(city_name, month_name, day_name,filtering):
    df = pd.read_csv(f"{city_name}.csv")
    date_in_numbers = df["Start Time"]
    list_of_dates = []
    matched_day = []
    matched_month = []
    integer_list_of_dates = []

    if bool(month_name) == True and bool(day_name) == False:
        for index in date_in_numbers:
            list_of_dates.append(re.split("-0|-|:0|:|\s0|\s",index))

        month_object = datetime.strptime(month_name[0:3].title(), "%b")
        month_number = month_object.month
        
        for index in range(0,len(list_of_dates)):
            integer_list_of_dates.append([int(numbers) for numbers in list_of_dates[index]])

        for index in range(0,len(integer_list_of_dates)):
            
            if month_number == integer_list_of_dates[index][1]:
                
                    matched_month.append(datetime(*integer_list_of_dates[index]))

        df = df.loc[df['Start Time'].isin([str(date) for date in matched_month])]
        df[f"Filtering By Month "] = f"{month_name}"
    
    elif bool(day_name) == True and bool(month_name) == False:
        for index in date_in_numbers:
           list_of_dates.append(re.split("-0|-|:0|:|\s0|\s",index))

        for index in range(0,len(list_of_dates)):
                    integer_list_of_dates.append([int(numbers) for numbers in list_of_dates[index]])

        for index in range(0,len(integer_list_of_dates)):
            
            if day_name == datetime(*integer_list_of_dates[index]).strftime("%A") and day_name[0:3] == datetime(*integer_list_of_dates[index]).strftime("%a"):
                    matched_day.append(datetime(*integer_list_of_dates[index]))

        df = df.loc[df['Start Time'].isin([str(date) for date in matched_day])]
        df["Filtering By Day"] = f"{day_name}"
    
    elif bool(month_name) == False & bool(day_name) == False:
        df = df

    elif bool(month_name) == True & bool(day_name) == True:

        for index in date_in_numbers:
           list_of_dates.append(re.split("-0|-|:0|:|\s0|\s",index))

        for index in range(0,len(list_of_dates)):
                    integer_list_of_dates.append([int(numbers) for numbers in list_of_dates[index]])

        for index in range(0,len(integer_list_of_dates)):
            
            if day_name == datetime(*integer_list_of_dates[index]).strftime("%A") and day_name[0:3] == datetime(*integer_list_of_dates[index]).strftime("%a"):
                    matched_day.append(datetime(*integer_list_of_dates[index]))

        for index in date_in_numbers:
            list_of_dates.append(re.split("-0|-|:0|:|\s0|\s",index))

        month_object = datetime.strptime(month_name[0:3].title(), "%b")
        month_number = month_object.month
        
        for index in range(0,len(list_of_dates)):
            integer_list_of_dates.append([int(numbers) for numbers in list_of_dates[index]])

        for index in range(0,len(integer_list_of_dates)):
            
            if month_number == integer_list_of_dates[index][1]:
                
                    matched_month.append(datetime(*integer_list_of_dates[index]))

        df = df.loc[(df['Start Time'].isin([str(date) for date in matched_month])) & (df['Start Time'].isin([str(date) for date in matched_day]))]
        df["Filtering By Both"] = "".join([f"{month_name} , {day_name}"])
        

    return df

# ------------------------------------------------- Outputing informations ------------------------------------------------#
            

#------------------------------------ Start Stations ------------------------------------------#

def start_stations(dataframe):
    start_time = time.time()
    print('\nCollecting data....!!\n')

    stations_names = dataframe["Start Station"].value_counts()
    most_common_station = stations_names.loc[stations_names.values == max(stations_names)].to_frame(name="")
    least_common_station = stations_names.loc[stations_names.values == min(stations_names)].to_frame(name="")

    if len(most_common_station) > 1 :
        print("*------------------ The most common Start Stations ---------------*")
        for stations in most_common_station.index: 
            print(stations, end = " , ")
        
    else:    
        print(f"*------------------ The most common Start Station --------------- {most_common_station}")

    if len(least_common_station) > 1:
        print("\n*------------------ The least common Start Stations ---------------* \n")
        for stations in least_common_station.index:
            print(stations, end = " , ")
    else:
        print(f"*------------------ The least common Start Station ---------------*   -> {least_common_station} \n ")

    print("\nThis took %s seconds." % (time.time() - start_time))

#------------------------------------------ End Stations ------------------------------------------------#

def end_stations(dataframe):
    print('\nCollecting data....!!\n')
    start_time = time.time()
    stations_names = dataframe["End Station"].value_counts()
    most_common_station = stations_names.loc[stations_names.values == max(stations_names)].to_frame(name="")
    least_common_station = stations_names.loc[stations_names.values == min(stations_names)].to_frame(name="")

    if len(most_common_station) > 1 :
        print("\n *------------------ The most common End Stations ---------------*")
        for stations in most_common_station.index: 
            print(stations, end = " , ")

    else:    
        print(f"\n\n*------------------ The most common End Station ---------------*   \n{most_common_station} \n ")

    if len(least_common_station) > 1:
        print("*------------------ The least common End Stations ---------------* \n")
        for stations in least_common_station.index:
            print(stations, end = " , ")
    else:
        print(f"*------------------ The least common End Station ---------------*   ->{least_common_station} \n ")
                
    print("\nThis took %s seconds." % (time.time() - start_time))

#------------------------------------------ Trips ---------------- -----------------------------------#

def trips(dataframe):
    print('\nCollecting data....!!\n')
    start_time = time.time()
    distance =[]

    stations_names = dataframe[["Start Station","End Station"]].value_counts()
    longest_trip_duration = int(dataframe["Trip Duration"].max())
    filtering_using_trip_duration = dataframe.loc[dataframe["Trip Duration"] == dataframe["Trip Duration"].max()]
    td = str(timedelta(seconds=longest_trip_duration))
    time_data = re.split(":0|:",td)
    most_common_trip = stations_names.loc[stations_names.values == max(stations_names)].to_frame(name="")

    print("\n\n*----------------------- The most common Trip is ---------------------* \n")
    for a_point in most_common_trip.index[0]:
        distance.append(a_point)

    print(f"From {distance[0]} to {distance[1]} ,the amount of users who took it are {most_common_trip.values[0][0]} user...\n")
    
    print("*----------------------- The longest trip duration ---------------------* \n")
    print("->Is from *{}* to *{}* and It took about {} hours ,{} minutes and {} seconds...\n".format("".join(filtering_using_trip_duration["Start Station"].values),"".join(filtering_using_trip_duration["End Station"].values),time_data[0],time_data[1],time_data[2]))

    print("\nThis took %s seconds." % (time.time() - start_time))

#-------------------------------------------------- Travel Time--------------------------------------------------#

def travel_time(dataframe):
    print('\nCollecting data....!!\n')
    start_time = time.time()
    total_travel_time = int(dataframe["Trip Duration"].sum())
    average_travel_time = int(dataframe["Trip Duration"].mean())
    td = str(timedelta(seconds=total_travel_time))
    td_average = str(timedelta(seconds=average_travel_time))
    time_data = re.split(":0|:",td)
    time_average = re.split(":0|:",td_average)
    
    print("*----------------------- The total traveled time  ---------------------*\n")

    print(f"->Is about {time_data[0]} hours,{time_data[1]} minutes and {time_data[2]} seconds...\n")

    print("*----------------------- The average traveled time  ---------------------*\n")

    print(f"->Is about {time_average[0]} hours,{time_average[1]} minutes and {time_average[2]} seconds...\n")


    print("\nThis took %s seconds." % (time.time() - start_time))

#-------------------------------------------------------- Users Infromation ----------------------------------------------#

def users(dataframe):
           #----------------------- Checking if Gender in the DataFrame --------------------------#
    print('\nCollecting data....!!\n')
    start_time = time.time()
    searching_for_male = dataframe.isin(["Male"])
    word = ["Gender"]
    list_of_columns = []
    total_gender = []
    for columns in searching_for_male:
        list_of_columns.append([columns])

    if word in list_of_columns:
        genders = dataframe.groupby(["Gender"]).size()

        for gender_count in genders.values:
            total_gender.append(gender_count)

        print("*----------------------- Gender ---------------------*\n")
        print(f"->There is about {total_gender[1]} Males and about {total_gender[0]} Females....\n")
    
    else:
        print("Sorry, there is no Gender data in this dataframe!!...\n")    


        #--------------------------- Counting users type --------------------------#

    getting_data = dataframe.groupby(["User Type"]).size()
    type_of_user = []
    count_of_user = []

    [type_of_user.append(i) for i in getting_data.index]
    [count_of_user.append(i) for i in getting_data.values]

    if "Dependent" not in type_of_user:
        count_of_user.insert(1,0)

    print("#------------------------ Users Type ----------------------------#\n")

    print(f"->There is about {count_of_user[0]} Customer , {count_of_user[1]} Dependent ,and {count_of_user[2]} Subscriber , In Total there is about {sum(count_of_user)} users....\n")

        #------------------------------- Birth Year -----------------------------------#

    if "Birth Year" in dataframe.columns:
        youngest_user = dataframe["Birth Year"].max()
        oldest_user = dataframe["Birth Year"].min()
        birth_data = dataframe.groupby(["Birth Year"]).size()
        most_common_year = birth_data.loc[birth_data.values == max(birth_data)].to_frame(name="")
        today = date.today()
        year = [int(year) for year in most_common_year.index]
        age = lambda x : today.year - x

        print("*------------------------------ Users Birth ------------------------------*\n")
        print("->The youngest user was born in {} ,which is {} years old....\n".format(int(youngest_user),age(int(youngest_user))))
        print("->The oldest user was born in {} ,which is {} years old....\n".format(int(oldest_user), age(int(oldest_user))))
        print("->The most common user's birth year is {} ,which is {} years old....\n".format(year[0],age(year[0])))

# ---------------------------------------------- Individual information ---------------------------------------------------#
    while True:
        print("*-------------------------- Individual users information -------------------------------*\n")
        start_time = time.time()
        individual_user_info = input("Would you like to see some indvidual infromation? Please enter yes or no..\n-> ")

        users_individual_gender_list = ["male","female","all"]

        if individual_user_info == "yes":
            users_individual_type = input("\nOh!! Great, would u like to enter users type? [ Customer,Dependent,Subscriber ] if you want all users please type #- All -#..\n-> ")

            if users_individual_type.lower() == "customer":
                
                if "Customer" in dataframe["User Type"].values:

                    if bool(total_gender) == True:
                        users_individual_gender = input("\nWould u like to users gender? [ Male,Female ] if u dont want to filter please type #- All -#..\n-> ")
                        
                        while True:
                            if users_individual_gender in users_individual_gender_list:
                                if users_individual_gender.lower() == "male":
                                    df = dataframe.loc[(dataframe["Gender"] == "Male") & (dataframe["User Type"] == "Customer")].reset_index()
                                    print(df)

                                    asking_user = input("\nWould u like to see more infromation about these users ? Please type yes or no...\n-> ")
                                    while True:
                                        if asking_user.lower() == "yes":
                                            raw_numbers = 0
                                            while True:
                                                print(df.iloc[raw_numbers: raw_numbers+9])
                                                raw_numbers += 9

                                                more_rows = input("\nMore infromation? Please type yes or no... \n-> ")

                                                if more_rows.lower() != "yes":
                                                    break
                                            break
                                    
                                        elif asking_user.lower() == "no":
                                            break

                                        else:
                                            asking_user = input("\nSorry Wrong value , Please enter yes or no...\n-> ")
                                            

                                elif users_individual_gender.lower() == "female":
                                    df = dataframe.loc[(dataframe["Gender"] == "Female") & (dataframe["User Type"] == "Customer")].reset_index()

                                    print(df)
                                    asking_user = input("\nWould u like to see more infromation about these users ? Please type yes or no\n-> ")
                                    if asking_user.lower() == "yes":
                                        raw_numbers = 0
                                        while True:
                                            print(df.iloc[raw_numbers: raw_numbers+9])
                                            raw_numbers += 9

                                            more_rows = input("\nMore infromation? Please type yes or no... \n-> ")

                                            if more_rows.lower() != "yes":
                                                break
                                    
                                    elif asking_user.lower() == "no":
                                        break

                                    else:
                                        print("Sorry wrong value !!!!")
                                        break

                                elif users_individual_gender.lower() == "all":
                                     df = dataframe.loc[dataframe["User Type"] == "Customer"].reset_index()
                                     print(df)
                                     
                                     asking_user = input("\nWould u like to see more infromation about these users ? Please type yes or no\n-> ")
                                     if asking_user.lower() == "yes":
                                        raw_numbers = 0
                                        while True:
                                            print(df.iloc[raw_numbers: raw_numbers+9])

                                            more_rows = input("More informaton? Please type yes or no... \n-> ")

                                            raw_numbers += 9
                                            if more_rows.lower() != "yes":
                                                break
                                     
                                     elif asking_user.lower() == "no":
                                        break

                                     else:
                                        print("Sorry wrong value !!!!")
                                        break
                                break               
                            elif users_individual_gender.lower() == "no":
                                break


                            else:
                                users_individual_gender = input("\nSorry you entered a wrong gender!! ,Please enter [ Male,Female ] if u dont want to filter please type #- All -#.. or no if u dont want to continue...\n-> ").lower()

                    else:
                        df = dataframe.loc[dataframe["User Type"] == "Customer"].reset_index()
                        print(df)

                        asking_user = input("\nWould u like to see more infromation about these users ? Please type yes or no\n-> ")
                        
                        if asking_user.lower() == "yes":
                            raw_numbers = 0
                            while True:
                                print(df.iloc[raw_numbers: raw_numbers+9])
                                raw_numbers += 9

                                more_rows = input("\nMore infromation? Please type yes or no... \n-> ")

                                if more_rows.lower() != "yes":
                                    break
                        elif asking_user.lower() == "no":
                            break

                        else:
                            print("Sorry wrong value !!!!")
                            break            
                else:
                    print("\nOh!! sorry there is no customer in this dataframe , Please try another users type? [ Dependent,Subscriber ]..\n")
                    
            
            
            elif users_individual_type.lower() == "dependent":
                
                if "Dependent" in dataframe["User Type"].values:

                    if bool(total_gender) == True:
                        users_individual_gender = input("\nWould u like to enter users gender? [ Male,Female ] if u dont want to filter please type #- All -#..\n-> ")
                        while True:
                            if users_individual_gender in users_individual_gender_list:
                                if users_individual_gender.lower() == "male":
                                    df = dataframe.loc[(dataframe["Gender"] == "Male") & (dataframe["User Type"] == "Dependent")].reset_index()
                                    print(df)

                                    asking_user = input("\nWould u like to see more infromation about these users ? Please type yes or no...\n-> ")
                                    while True:
                                        if asking_user.lower() == "yes":
                                            raw_numbers = 0
                                            while True:
                                                print(df.iloc[raw_numbers: raw_numbers+9])
                                                raw_numbers += 9

                                                more_rows = input("\nMore infromation? Please type yes or no... \n-> ")

                                                if more_rows.lower() != "yes":
                                                    break
                                            break
                                    
                                        elif asking_user.lower() == "no":
                                            break

                                        else:
                                            asking_user = input("\nSorry Wrong value , Please enter yes or no...\n-> ")
                                            

                                elif users_individual_gender.lower() == "female":
                                    df = dataframe.loc[(dataframe["Gender"] == "Female") & (dataframe["User Type"] == "Dependent")].reset_index()

                                    print(df)
                                    asking_user = input("\nWould u like to see more infromation about these users ? Please type yes or no\n-> ")
                                    if asking_user.lower() == "yes":
                                        raw_numbers = 0
                                        while True:
                                            print(df.iloc[raw_numbers: raw_numbers+9])
                                            raw_numbers += 9

                                            more_rows = input("\nMore infromation? Please type yes or no... \n-> ")

                                            if more_rows.lower() != "yes":
                                                break
                                    
                                    elif asking_user.lower() == "no":
                                        break

                                    else:
                                        print("Sorry wrong value !!!!")
                                        break

                                elif users_individual_gender.lower() == "all":
                                     df = dataframe.loc[dataframe["User Type"] == "Dependent"].reset_index()
                                     print(df)
                                     
                                     asking_user = input("\nWould u like to see more infromation about these users ? Please type yes or no\n-> ")
                                     if asking_user.lower() == "yes":
                                        raw_numbers = 0
                                        while True:
                                            print(df.iloc[raw_numbers: raw_numbers+9])

                                            more_rows = input("More informaton? Please type yes or no... \n-> ")

                                            raw_numbers += 9
                                            if more_rows.lower() != "yes":
                                                break
                                     
                                     elif asking_user.lower() == "no":
                                        break

                                     else:
                                        print("Sorry wrong value !!!!")
                                        break
                                break               
                            elif users_individual_gender.lower() == "no":
                                break


                            else:
                                users_individual_gender = input("\nSorry you entered a wrong gender!! ,Please enter [ Male,Female ] if u dont want to filter please type #- All -#.. or no if u dont want to continue...\n-> ").lower()

                    else:
                        df = dataframe.loc[dataframe["User Type"] == "Dependent"].reset_index()
                        print(df)

                        asking_user = input("\nWould u like to see more infromation about these users ? Please type yes or no\n-> ")
                        if asking_user.lower() == "yes":
                            raw_numbers = 0
                            while True:
                                print(df.iloc[raw_numbers: raw_numbers+9])
                                raw_numbers += 9

                                more_rows = input("\nMore infromation? Please type yes or no... \n-> ")

                                if more_rows.lower() != "yes":
                                    break
                
                        elif asking_user.lower() == "no":
                            break

                        else:
                            print("Sorry wrong value !!!!")
                            break
                else:
                    print("\nOh!! sorry there is no dependent in this dataframe , Please try another users type? [ Customer,Subscriber ]..\n")

                        

            elif users_individual_type.lower() == "subscriber":
                
                if "Subscriber" in dataframe["User Type"].values:

                    if bool(total_gender) == True:
                        users_individual_gender = input("\nWould u like to enter users gender? [ Male,Female ] if u dont want to filter please type #- All -#..\n-> ")
                        while True:
                            if users_individual_gender in users_individual_gender_list:
                                if users_individual_gender.lower() == "male":
                                    df = dataframe.loc[(dataframe["Gender"] == "Male") & (dataframe["User Type"] == "Subscriber")].reset_index()
                                    print(df)

                                    asking_user = input("\nWould u like to see more infromation about these users ? Please type yes or no...\n-> ")
                                    while True:
                                        if asking_user.lower() == "yes":
                                            raw_numbers = 0
                                            while True:
                                                print(df.iloc[raw_numbers: raw_numbers+9])
                                                raw_numbers += 9

                                                more_rows = input("\nMore infromation? Please type yes or no... \n-> ")

                                                if more_rows.lower() != "yes":
                                                    break
                                            break
                                    
                                        elif asking_user.lower() == "no":
                                            break

                                        else:
                                            asking_user = input("\nSorry Wrong value , Please enter yes or no...\n-> ")
                                            

                                elif users_individual_gender.lower() == "female":
                                    df = dataframe.loc[(dataframe["Gender"] == "Female") & (dataframe["User Type"] == "Subscriber")].reset_index()

                                    print(df)
                                    asking_user = input("\nWould u like to see more infromation about these users ? Please type yes or no\n-> ")
                                    if asking_user.lower() == "yes":
                                        raw_numbers = 0
                                        while True:
                                            print(df.iloc[raw_numbers: raw_numbers+9])
                                            raw_numbers += 9

                                            more_rows = input("\nMore infromation? Please type yes or no... \n-> ")

                                            if more_rows.lower() != "yes":
                                                break
                                    
                                    elif asking_user.lower() == "no":
                                        break

                                    else:
                                        print("Sorry wrong value !!!!")
                                        break

                                elif users_individual_gender.lower() == "all":
                                     df = dataframe.loc[dataframe["User Type"] == "Subscriber"].reset_index()
                                     print(df)
                                     
                                     asking_user = input("\nWould u like to see more infromation about these users ? Please type yes or no\n-> ")
                                     if asking_user.lower() == "yes":
                                        raw_numbers = 0
                                        while True:
                                            print(df.iloc[raw_numbers: raw_numbers+9])

                                            more_rows = input("More informaton? Please type yes or no... \n-> ")

                                            raw_numbers += 9
                                            if more_rows.lower() != "yes":
                                                break
                                     
                                     elif asking_user.lower() == "no":
                                        break

                                     else:
                                        print("Sorry wrong value !!!!")
                                        break
                                break               
                            elif users_individual_gender.lower() == "no":
                                break


                            else:
                                users_individual_gender = input("\nSorry you entered a wrong gender!! ,Please enter [ Male,Female ] if u dont want to filter please type #- All -#.. or no if u dont want to continue...\n-> ").lower()
        

                    else:
                        df = dataframe.loc[dataframe["User Type"] == "Subscriber"].reset_index()
                        print(df)

                        asking_user = input("\nWould u like to see more infromation about these users ? Please type yes or no\n-> ")
                        if asking_user.lower() == "yes":
                            raw_numbers = 0
                            while True:
                                print(df.iloc[raw_numbers: raw_numbers+9])
                                raw_numbers += 9

                                more_rows = input("\nMore infromation? Please type yes or no... \n-> ")

                                if more_rows.lower() != "yes":
                                    break
                        elif asking_user.lower() == "no":
                            break

                        else:
                            print("Sorry wrong value !!!!")
                            break
                    
            elif users_individual_type.lower() == "all":
                if bool(total_gender) == True:
                    
                    users_individual_gender = input("\nWould u like to enter users gender? [ Male,Female ] if u dont want to filter please type #- All -#..\n-> ")

                    while True:
                        if users_individual_gender in users_individual_gender_list:
                            if users_individual_gender.lower() == "male":
                                df = dataframe.loc[dataframe["Gender"] == "Male"].reset_index()
                                print(df)

                                asking_user = input("\nWould u like to see more infromation about these users ? Please type yes or no...\n-> ")
                                while True:
                                    if asking_user.lower() == "yes":
                                        raw_numbers = 0
                                        while True:
                                            print(df.iloc[raw_numbers: raw_numbers+9])
                                            raw_numbers += 9

                                            more_rows = input("\nMore infromation? Please type yes or no... \n-> ")

                                            if more_rows.lower() != "yes":
                                                break
                                        break
                                
                                    elif asking_user.lower() == "no":
                                        break

                                    else:
                                        asking_user = input("\nSorry Wrong value , Please enter yes or no...\n-> ")
                                        

                            elif users_individual_gender.lower() == "female":
                                df = dataframe.loc[dataframe["Gender"] == "Female"].reset_index()

                                print(df)
                                asking_user = input("\nWould u like to see more infromation about these users ? Please type yes or no\n-> ")
                                if asking_user.lower() == "yes":
                                    raw_numbers = 0
                                    while True:
                                        print(df.iloc[raw_numbers: raw_numbers+9])
                                        raw_numbers += 9

                                        more_rows = input("\nMore infromation? Please type yes or no... \n-> ")

                                        if more_rows.lower() != "yes":
                                            break
                                
                                elif asking_user.lower() == "no":
                                    break

                                else:
                                    print("Sorry wrong value !!!!")
                                    break

                            elif users_individual_gender.lower() == "all":
                                 df = dataframe.reset_index()
                                 print(df)
                                 
                                 asking_user = input("\nWould u like to see more infromation about these users ? Please type yes or no\n-> ")
                                 if asking_user.lower() == "yes":
                                    raw_numbers = 0
                                    while True:
                                        print(df.iloc[raw_numbers: raw_numbers+9])

                                        more_rows = input("More informaton? Please type yes or no... \n-> ")

                                        raw_numbers += 9
                                        if more_rows.lower() != "yes":
                                            break
                                 
                                 elif asking_user.lower() == "no":
                                    break

                                 else:
                                    print("Sorry wrong value !!!!")
                                    break
                            break               
                        elif users_individual_gender.lower() == "no":
                            break


                        else:
                            users_individual_gender = input("\nSorry you entered a wrong gender!! ,Please enter [ Male,Female ] if u dont want to filter please type #- All -#.. or no if u dont want to continue...\n-> ").lower()


                else:
                    
                    df = dataframe.reset_index()
                    print(df)

                    asking_user = input("\nWould u like to see more infromation about these users ? Please type yes or no\n-> ")
                    if asking_user.lower() == "yes":
                        raw_numbers = 0
                        while True:
                            print(df.iloc[raw_numbers: raw_numbers+9])
                            raw_numbers += 9

                            more_rows = input("\nMore infromation? Please type yes or no... \n-> ")
                            print(more_rows)

                            if more_rows.lower() != "yes":
                                print(more_rows)
                                break
                    
                    elif asking_user.lower() == "no":
                        break

                    else:
                        print("Sorry wrong value !!!!")
                        break
            
            elif users_individual_type.lower() == "no":
                break
            
            else:
                print("\nSorry you entered a wrong value!!! , Please choose between [ Customer,Dependent,Subscriber ]....\n")




        elif individual_user_info == "no":
            break

        else:
            print("\nSorry u entered a wrong value, Please choose between [ Yes or No ]..\n")

    print("\nThis took %s seconds." % (time.time() - start_time))

# ---------------------------------------------- Date from numbers to Letters ---------------------------------------------------#

def getting_time(dataframe):
    print('\nCollecting data....!!\n')
    start_time = time.time()
    date_in_numbers = dataframe["Start Time"]
    zeros = [0,0,0]

    list_of_dates = []
    dict_of_dates = {}
    date_in_letters = []
    months = []
    days = []
    hours = []
    integer_list_of_dates = []

    for x in date_in_numbers:
        list_of_dates.append(re.split("-0|-|:0|:|\s0|\s",x))

    for index in range(0,len(list_of_dates)):
        integer_list_of_dates.append([int(numbers) for numbers in list_of_dates[index]])
        
        for zero in zeros:
            integer_list_of_dates[index].append(zero)
        
    for index in range(0, len(integer_list_of_dates)):
        date_in_letters.append(str(time.asctime(tuple(integer_list_of_dates[index]))))
        dict_of_dates[date_in_numbers.iloc[index]] = date_in_letters[index]

    [months.append(list_of_dates[index][1]) for index in range(0,len(list_of_dates))]
    [days.append(list_of_dates[index][2]) for index in range(0,len(list_of_dates))]
    [hours.append(list_of_dates[index][3]) for index in range(0,len(list_of_dates))]

    months_count = Counter(months)
    days_count = Counter(days)
    hours_count = Counter(hours)

    most_common_month = [int(key) for key , value in months_count.items() if value == max(months_count.values())]
    most_common_days = [int(key) for key , value in days_count.items() if value == max(days_count.values())]
    most_common_hours = [int(key) for key , value in hours_count.items() if value == max(hours_count.values())]

    months_object = datetime.strptime(str(most_common_month[0]), "%m")
    days_object = datetime.strptime(str(most_common_days[0]), "%d")
    hours_object = datetime.strptime(str(most_common_hours[0]), "%H")

    month_name = months_object.strftime("%b")
    days_name = days_object.strftime("%a")
    hours_name = hours_object.strftime("%#I %p")

    print("*-------------------------- Times to travel -------------------------------*\n")

    print(f"->The most common month to travel is {most_common_month[0]} in months -> {month_name} ....\n")
    print(f"->The most common day to travel is {most_common_days[0]} -> of each month ....\n")
    print(f"->The most common hour to travel is {most_common_hours[0]} O'clock in time -> {hours_name} ....\n")

    print("\nThis took %s seconds." % (time.time() - start_time))

    
#-------------------------------------------- Main() --------------------------------------------------#
def main():
    while True:
        # ---------------------------------- Reading Csv files and Filling Nan values with forward filling columns ---------------#
        city_name, month_name, day_name,filtering = input_data()
        print(f"*-------------------------- Filtering by {filtering} --------------------------*")
        print('\nCollecting data....!!\n')
        
        df = filtering_data(city_name,month_name,day_name,filtering)
        df = df.fillna(method="ffill", axis = 0)
        print(df)
         # ---------------------------------- Calling functions ---------------#
        getting_time(df)        
        start_stations(df)
        end_stations(df)
        trips(df)
        travel_time(df)
        users(df)
        print("-"*80)
        restart = input('\nWould you like to restart the program? Plz type [yes or no].\n-> ')
        if restart.lower() == 'yes':
            print("\n*------------------------------------- Restaring the program ------------------------------------*\n")

        else:
            break
if __name__ == "__main__":
    main()

