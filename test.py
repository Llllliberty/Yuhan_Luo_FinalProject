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
from file_operations import save_outfit_recommendation, save_outfit_history, read_outfit_recommendations, read_outfit_history  # Ensure correct import

def test_file_operations():
    print("\nTesting file operations:")

    # Test saving outfit recommendations to file
    save_outfit_recommendation("sunny", "casual", "T-shirt and shorts")
    save_outfit_recommendation("rainy", "interview", "Formal shirt, pants, and umbrella")

    # Test saving user outfit history to file
    save_outfit_history("T-shirt and shorts", "sunny")
    save_outfit_history("Raincoat and boots", "rainy")
    
    # Test reading outfit recommendations history
