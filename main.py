from outfit_recommendation import recommend_outfit  # Import the function to recommend outfits
from outfit_review import review_outfit  # Import the function to review the outfit after the event
from file_operations import save_outfit_recommendation, save_outfit_history, save_user_choice, read_outfit_recommendations, read_outfit_history, read_user_choice_history  # Import file handling functions

def main():
    print("Welcome to the Weather & Occasion Outfit Assistant!")  # Print welcome message

    # Provide mode selection
    mode = input("Choose a mode (1: Pre-Departure Recommendation, 2: Post-Event Review): ")  # Ask user for mode selection

    if mode == '1':
        # Pre-departure recommendation mode
        weather = input("Enter the weather (sunny/rainy/cloudy): ").lower()  # Get weather input
        occasion = input("Enter the occasion (casual/interview/date/party): ").lower()  # Get occasion input
        recommendation = recommend_outfit(weather, occasion)  # Call the recommend function
        print(f"Recommended Outfit: {recommendation}")  # Display the recommended outfit
        
        # Save the recommendation to file
        save_outfit_recommendation(weather, occasion, recommendation)
        
        # NEW: Ask user what they actually chose to wear
        user_choice = input("What did you decide to wear? (Press Enter to skip): ")
        
        if user_choice:  # Only save if user provided a choice
            save_user_choice(weather, occasion, recommendation, user_choice)
            print("Your choice has been saved!")

    elif mode == '2':
        # Post-event review mode
        worn_clothes = input("Enter the clothes you wore today: ")  # Get the user's worn clothes input
        weather = input("Enter the weather today (sunny/rainy/cloudy): ").lower()  # Get the weather input
        feedback = review_outfit(worn_clothes, weather)  # Call the outfit review function
        print(feedback)  # Display the feedback
        
        # Save outfit history to file
        save_outfit_history(worn_clothes, weather)

    # Read historical recommendations and outfit history
    read_outfit_recommendations()  # Read and display outfit recommendations history
    read_user_choice_history()  # NEW: Read and display user choice history
    read_outfit_history()  # Read and display user outfit history

if __name__ == "__main__":
    main()  # Execute the main program
