from utils import have_bathroom, make_coffee, drink_coffee, leave_your_house

morning_routine = (have_bathroom(), make_coffee(), drink_coffee(), leave_your_house())

for task in morning_routine:
    print(task)