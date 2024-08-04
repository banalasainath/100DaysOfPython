# In python you can declare the type of a variable for further usage and modification
age: int
name: str
is_eligible: bool


def is_eligible_to_vote(age_value: int, person_name: str) -> bool:
    # global helps to refer to the global variable defined instead of creating a new local variable inside the fn.
    global is_eligible
    if age_value > 18:
        is_eligible = True
    else:
        is_eligible = False

    return is_eligible


age = 20
name = "Captain America"


if is_eligible_to_vote(age, name):
    print(f"{name} is eligible to vote")
else:
    print(f"{name} is not eligible to vote")
