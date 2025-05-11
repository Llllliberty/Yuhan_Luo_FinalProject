import os  # Import os module for file and directory operations

# File paths to store recommendations and outfit history
RECOMMENDATION_FILE = 'outfit_recommendations.txt'  # File to store outfit recommendations
HISTORY_FILE = 'user_outfit_history.txt'  # File to store user's outfit history

# Function to save outfit recommendations
def save_outfit_recommendation(weather, occasion, recommendation):
    with open(RECOMMENDATION_FILE, 'a') as file:  # Open file in append mode
        file.write(f"Weather: {weather}, Occasion: {occasion}, Recommendation: {recommendation}\n")  # Write the recommendation

# Function to save user outfit history
def save_outfit_history(worn_clothes, weather):
    with open(HISTORY_FILE, 'a') as file:  # Open file in append mode
        file.write(f"Worn Clothes: {worn_clothes}, Weather: {weather}\n")  # Write the outfit history

# Function to read and display outfit recommendations
def read_outfit_recommendations():
    if os.path.exists(RECOMMENDATION_FILE):  # Check if the file exists
        with open(RECOMMENDATION_FILE, 'r') as file:  # Open file in read mode
            print("\nOutfit Recommendations History:")  # Print history title
            print(file.read())  # Display the file content
    else:
        print("No recommendations found.")  # If the file doesn't exist, print a message

# Function to read and display user outfit history
def read_outfit_history():
    if os.path.exists(HISTORY_FILE):  # Check if the file exists
        with open(HISTORY_FILE, 'r') as file:  # Open file in read mode
            print("\nUser Outfit History:")  # Print history title
            print(file.read())  # Display the file content
    else:
        print("No outfit history found.")  # If the file doesn't exist, print a message
