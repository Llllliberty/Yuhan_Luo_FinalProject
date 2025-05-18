# Testing recommend_outfit function from outfit_recommendation.py
from outfit_recommendation import recommend_outfit  # Ensure correct import

def test_recommend_outfit():
    print("Testing recommend_outfit function:")
    
    # Test different weather and occasion combinations
    print(recommend_outfit("sunny", "casual"))  # Expected: T-shirt and shorts
    print(recommend_outfit("rainy", "interview"))  # Expected: Formal shirt, pants, and umbrella
    print(recommend_outfit("cloudy", "date"))  # Expected: Smart-casual outfit
    print(recommend_outfit("sunny", "party"))  # Expected: Stylish dress or shirt and jeans
    
    # Test invalid weather or occasion combinations
    print(recommend_outfit("snowy", "casual"))  # Expected: Sorry, we don't have a recommendation for this combination.
    print(recommend_outfit("sunny", "holiday"))  # Expected: Sorry, we don't have a recommendation for this combination.

test_recommend_outfit()

# Testing review_outfit function from outfit_review.py
from outfit_review import review_outfit  # Ensure correct import

def test_review_outfit():
    print("\nTesting review_outfit function:")
    
    # Test different weather and outfit combinations
    print(review_outfit("T-shirt and shorts", "sunny"))  # Expected: 😊 Your outfit was perfect for the sunny weather!
    print(review_outfit("Raincoat and boots", "rainy"))  # Expected: 😊 Your outfit was perfect for the rainy weather!
    print(review_outfit("Sweater and jeans", "cloudy"))  # Expected: 😊 Your outfit was suitable for the cloudy weather!
    print(review_outfit("T-shirt and jeans", "cloudy"))  # Expected: 😢 The outfit might not have been suitable for the weather.

test_review_outfit()

# Testing file operations from file_operations.py
from file_operations import (save_outfit_recommendation, save_outfit_history, 
                           save_user_choice, read_outfit_recommendations, 
                           read_outfit_history, read_user_choice_history)  # Import all necessary functions

def test_file_operations():
    print("\nTesting file operations:")

    # Test saving outfit recommendations to file
    save_outfit_recommendation("sunny", "casual", "T-shirt and shorts")
    save_outfit_recommendation("rainy", "interview", "Formal shirt, pants, and umbrella")
    print("Saved outfit recommendations.")

    # Test saving user outfit history to file
    save_outfit_history("T-shirt and shorts", "sunny")
    save_outfit_history("Raincoat and boots", "rainy")
    print("Saved user outfit history.")
    
    # Test saving user choice history to file (NEW)
    save_user_choice("sunny", "casual", "T-shirt and shorts", "Blue T-shirt and khaki shorts")
    save_user_choice("rainy", "interview", "Formal shirt, pants, and umbrella", "Navy suit with umbrella")
    print("Saved user choice history.")
    
    # Test reading all files
    print("\nReading saved records:")
    read_outfit_recommendations()
    read_user_choice_history()  # NEW
    read_outfit_history()

test_file_operations()

# Test the complete workflow
def test_complete_workflow():
    print("\nTesting complete workflow:")
    
    # Simulate pre-departure recommendation workflow
    weather = "cloudy"
    occasion = "date"
    print(f"Weather: {weather}, Occasion: {occasion}")
    
    # Get recommendation
    recommendation = recommend_outfit(weather, occasion)
    print(f"Recommended outfit: {recommendation}")
    
    # Save recommendation
    save_outfit_recommendation(weather, occasion, recommendation)
    
    # Simulate user choice
    user_choice = "Dark blue sweater with black jeans"
    print(f"User chose: {user_choice}")
    
    # Save user choice
    save_user_choice(weather, occasion, recommendation, user_choice)
    
    # Later, simulate post-event review
    worn_clothes = user_choice  # In real scenario, user might enter different clothes
    print(f"User wore: {worn_clothes}")
    
    # Get feedback
    feedback = review_outfit(worn_clothes, weather)
    print(f"Feedback: {feedback}")
    
    # Save outfit history
    save_outfit_history(worn_clothes, weather)
    
    # Read all histories
    print("\nFinal histories:")
    read_outfit_recommendations()
    read_user_choice_history()
    read_outfit_history()

test_complete_workflow()