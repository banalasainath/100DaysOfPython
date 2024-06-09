# Learning list and dictionary comprehension
# new_list = [ n+1 for n in range(1,8) if n%2 == 0 ]
# new_dict =  { new_key: new_value for (key, value) in existing_dict.items() if condition }

# comprehension using pandas dataframes
import pandas

players_list = {
    "player": ["Virat Kohli", "Hardik Pandya", "M S Dhoni"],
    "Jersey_No": [18, 33, 7]
}

df = pandas.DataFrame(players_list)
# we can work with dataframes similar to dictionary comprehensions, but we will get unnecessary while accessing the
# value
# for (key, value) in df.items():
#     # print(key)
#     print(value)

# to work with comprehensions for pandas we are having a separate function to loop
# This allows us to iterate over rows of the data frame instead of columns
for (index, row) in df.iterrows():
    print(index)  # Prints all indexes of the data frame
    print(row)   # prints each row
    print(row.player)  # prints player of that specific row
    print(row.Jersey_No)  # prints Jersey_No of that specific row
