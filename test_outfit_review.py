# Testing review_outfit function from outfit_review.py
from outfit_review import review_outfit  # Ensure correct import

def test_review_outfit():
    
    # Test different weather and outfit combinations
    print(review_outfit("T-shirt and shorts", "sunny"))  # Expected: 😊 Your outfit was perfect for the sunny weather!
    print(review_outfit("Raincoat and boots", "rainy"))  # Expected: 😢 The outfit might not have been suitable for the weather. 
    # Next time, make sure to wear a raincoat and waterproof shoes.
    print(review_outfit("Sweater and jeans", "cloudy"))  # Expected: 😢 The outfit might not have been suitable for the weather. 
    # Next time, a sweater or light jacket would be perfect for cloudy weather.
    print(review_outfit("T-shirt and jeans", "cloudy"))  # Expected: 😢 The outfit might not have been suitable for the weather. 
    # Next time, a sweater or light jacket would be perfect for cloudy weather.
    print(review_outfit("T-shirt and shorts", "snowy"))  # Expected: 😢 The outfit might not have been suitable for the weather. 
    # Next time, make sure to wear warm clothes, like a sweater and boots.
    print(review_outfit("Elegant sweater and warm pants", "snowy"))  # Expected: 😊 Your outfit was perfect for the snowy weather!

test_review_outfit()