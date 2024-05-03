import time

def display_menu():
    print("Health Calculator")
    print("-------------------")
    print("1. Calculate Water Intake")
    print("2. Calculate BMI")
    print("3. Calculate Target Heart Rate")
    print("4. Calculate Resting Heart Rate")
    print("5. Exit")

def calculate_water_intake():
    """
    Calculate the water intake from weight and activity level.
    """
    weight = float(input("Enter your weight (in pounds): "))
    activity_level = int(input("Enter your activity level (1 for sedentary, 2 for light activity, 3 for moderate activity, 4 for high activity): "))
    water_intake = 35 * weight + 0.5 * activity_level
    print("Your recommended daily water intake is: " + str(water_intake) + " ounces")
    # Health advice based on water intake
    if water_intake < 64:
        print("Remember to drink more water to stay hydrated!")
    elif water_intake > 100:
        print("Ensure you're not overhydrating. Moderation is key.")

def calculate_bmi(): 
    """
    Calculate the Body Mass Index (BMI) from weight and height.
    """
    weight = float(input("Enter your weight (in pounds): "))
    height = float(input("Enter your height (in inches): "))
    bmi = weight / (height ** 2)
    print("Your BMI is: " + str(bmi))
    # Health advice based on BMI
    if bmi < 18.5:
        print("Consider consulting a nutritionist for advice on healthy weight gain.")
    elif bmi > 25:
        print("Regular exercise and a balanced diet can help you maintain a healthy weight.")

def calculate_target_heart_rate():
    """
    Calculate the Target Heart rate.
    """
    age = int(input("Enter your age: "))
    max_heart_rate = 220 - age
    intensity = int(input("Enter your exercise intensity (1 for light, 2 for moderate, 3 for high): "))
    target_heart_rate = max_heart_rate * (intensity / 10.0)
    
    print("Your target heart rate is: " + str(target_heart_rate) + " beats per minute")
    # Health advice based on target heart rate
    if target_heart_rate < 100:
        print("To improve cardiovascular fitness, aim to increase your exercise intensity.")
    elif target_heart_rate > 160:
        print("Ensure you're not overexerting yourself during exercise. Listen to your body.")

def calculate_resting_heart_rate():
    """
    Calculate the Resting Heart rate.
    """
    resting_heart_rate = int(input("Enter your resting heart rate (beats per minute): "))
    print("Your resting heart rate is: " + str(resting_heart_rate) + " beats per minute")
    # Health advice based on resting heart rate
    if resting_heart_rate < 60:
        print("A lower resting heart rate is often a sign of good cardiovascular health.")
    elif resting_heart_rate > 100:
        print("Consult a healthcare provider if your resting heart rate is consistently high.")

def main():
    display_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        calculate_water_intake()
    elif choice == 2:
        calculate_bmi()
    elif choice == 3:
        calculate_target_heart_rate()
    elif choice == 4:
        calculate_resting_heart_rate()
    elif choice == 5:
        print("Thank you for using the Health Calculator!")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()