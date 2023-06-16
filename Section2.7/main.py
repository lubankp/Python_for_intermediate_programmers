# days = ['mon','tue','wed','thu','fri','sat','sun']
# workdays = days.copy()
# print(days)
# print(workdays)
# workdays = workdays[:-2]
# print(days)
# print(workdays)

# list = ['load data', 'export data', 'analyze & predict']
# option = input("Choose: 'load data', 'export data', 'analyze & predict'")
# while option:
#     if option.isdigit():
#         try:
#             print(list[int(option)])
#         except:
#             print("There is no option")
#     else:
#         print("It is not number")
#     option = input("Choose: 'load data', 'export data', 'analyze & predict'")

def DisplayOptions(options):
    for i in range(len(options)):
        print("{} - {}".format(i + 1, options[i]))

    choice = input('Select option above or press enter to exit: ')
    return choice


choice = 'x'
options = ['load data', 'export data', 'analyze & predict']
print(range(len(options)))
while choice:

    choice = DisplayOptions(options)

    # executed only if something was entered
    if choice:
        try:
            choice_num = int(choice) - 1
            if choice_num >= 0 and choice_num < len(options):
                print("you have selected {} - {}".format(choice_num + 1, options[choice_num]))
            else:
                print("choose a value from a list or press enter")
        except:
            print("You need to enter a number")
    else:
        print('----- END -----')