def general_info():
    print("-----------------BMI Calculator-----------------")
    name_info = input("Please enter your name here: ")
    weight_info = float(input("{}, Enter your weight in kilograms (kg) :  ".format(name_info)))
    height_info = float(input("{}, Enter your height in meters (m):  ".format(name_info)))
    check_BMI(height_info, weight_info, name_info)

def check_BMI(height,weight,name):
    BMI = weight/(height*height)
    if BMI<18.5:
        print("\nYou are under weight")
        print("\n Measures to be taken.\n >> Eating more frequently. \n >> Choosing food with lots of nutrients. \n >> Exercise. \n >> Avoiding empty calories.")
    elif 18.5< BMI <=24.9:
        print("\nYou have normal weight")
    elif 25<=BMI<=29.9:
        print("\nYou are Overweight")
    else:
        print("\nYou are Obese")
        print("\n Measures to be taken. \n >> Have a reduced-calorie diet and exercise regularly. \n >> Choosing healthier foods. \n >> Limit processed foods. ")

    print("\n{}, your BMI is {}.".format(name, BMI))

general_info()
