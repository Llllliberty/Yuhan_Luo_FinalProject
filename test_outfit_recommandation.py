# Testing recommend_outfit function from outfit_recommendation.py
from outfit_recommendation import recommend_outfit  # Ensure correct import

def test_recommend_outfit():
    

    # Test different weather and occasion combinations
    print(recommend_outfit("sunny", "casual"))  # Expected: T-shirt and shorts
    print(recommend_outfit("rainy", "interview"))  # Expected: Formal shirt, pants, and umbrella
    print(recommend_outfit("cloudy", "date"))  # Expected: Smart-casual outfit
    print(recommend_outfit("sunny", "party"))  # Expected: Stylish dress or shirt and jeans

    # Test new weather and occasion combinations
    print(recommend_outfit("snowy", "casual"))  # Expected: Thick sweater, warm pants, and boots
    print(recommend_outfit("sunny", "holiday"))  # Expected: Comfortable dress or light shirt and shorts
    print(recommend_outfit("rainy", "holiday"))  # Expected: Waterproof jacket and boots
    print(recommend_outfit("snowy", "interview"))  # Expected: Wool coat, dress pants, and scarf
    print(recommend_outfit("cloudy", "holiday"))  # Expected: Casual jacket and jeans
    print(recommend_outfit("sunny", "party"))  # Expected: Stylish dress or shirt and jeans
    print(recommend_outfit("snowy", "party"))  # Expected: Elegant sweater and warm pants

    # Test invalid weather or occasion combinations
    print(recommend_outfit("snowy", "holiday"))  # Expected: Warm coat, gloves, and boots
    print(recommend_outfit("sunny", "vacation"))  # Expected: Sorry, we don't have a recommendation for this combination.

test_recommend_outfit()
