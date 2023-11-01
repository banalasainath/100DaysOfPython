# csv is comma seperated values
# with open('./weather_data.csv', mode='r') as weather_file:
#     weather_report = weather_file.readlines()
#     print(weather_report)

import csv

# with open('./weather_data.csv', mode='r') as weather_file:
#     weather_report = csv.reader(weather_file)
#     temperatures = []
#     for one_day_weather in weather_report:
#         if one_day_weather[1] != "temp":
#             temperatures.append(int(one_day_weather[1]))
#     print(temperatures)

import pandas

weather_report = pandas.read_csv('weather_data.csv')
# print(weather_report.get('temp'))
# or
# print(weather_report["temp"])
#
# # learn more about dataframes, series and their functions in the pandas docs
#
# # we can convert the dataframe to different types of python data structures
# report_dict = weather_report.to_dict()
# print(report_dict)
#
# # similarly we can convert the series of a dataframe to different types of python data structures
# temp_list = weather_report["temp"].to_list()
# # average
# # print(sum(temp_list)/len(temp_list))
# # we can calculate the average using the inbuilt mean() function for series
# print(weather_report["temp"].mean())
#
# # getting the max of a series
# print(weather_report["temp"].max())


# getting a row based on a condition
# print(weather_report[weather_report.day == 'Monday'])
#
# print(weather_report[weather_report.temp == weather_report["temp"].max()])


# accessing the elements of a row
sunday = weather_report[weather_report.day == 'Monday']
# converting the celsius to Fahrenheit
# print(f"{sunday.temp*(9/5)+32}F")


# creating a dataframe from a dictionary
players_list = {
    "player": ["Virat Kohli", "Hardik Pandya", "M S Dhoni"],
    "Jersey_No": [18, 33, 7]
}

players = pandas.DataFrame(players_list)
# print(players)
# Writing into a csv file
# players.to_csv('players_jersey_no.csv')


squirrel_file = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
cinnamon_squirrel_count = len(squirrel_file[squirrel_file["Primary Fur Color"] == "Cinnamon"])
gray_squirrel_count = len(squirrel_file[squirrel_file["Primary Fur Color"] == "Gray"])
black_squirrel_count = len(squirrel_file[squirrel_file["Primary Fur Color"] == "Black"])
# print(f"black= {black_squirrel_count}, cinnamon= {cinnamon_squirrel_count}, gray = {gray_squirrel_count}")

squirrels = pandas.DataFrame(
    {
        "Fur Color": ["Gray", "Cinnamon", "Black"],
        "Squirrel Count for Each Color": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
    }
)

squirrels.to_csv("squirrels_color_count.csv")


