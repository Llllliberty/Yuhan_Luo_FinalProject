def recommend_outfit(weather, occasion):
    recommendations = {
        'sunny': {
            'casual': 'T-shirt and shorts',
            'interview': 'Formal shirt and pants',
            'date': 'Nice shirt and jeans',
            'party': 'Stylish dress or shirt and jeans',
            'holiday': 'Comfortable dress or light shirt and shorts'  # Add sunny holiday combination here
        },
        'rainy': {
            'casual': 'Raincoat and boots',
            'interview': 'Formal shirt, pants, and umbrella',
            'date': 'Waterproof jacket and comfortable shoes',
            'party': 'Stylish jacket and boots',
            'holiday': 'Waterproof jacket and boots'  # Add rainy holiday combination here
        },
        'cloudy': {
            'casual': 'Light sweater and jeans',
            'interview': 'Smart blouse and skirt',
            'date': 'Smart-casual outfit',
            'party': 'Chic blouse and skirt',
            'holiday': 'Casual jacket and jeans'  # Add cloudy holiday combination here
        },
        'snowy': {
            'casual': 'Thick sweater, warm pants, and boots',
            'interview': 'Wool coat, dress pants, and scarf',
            'date': 'Warm coat and gloves',
            'party': 'Elegant sweater and warm pants',
            'holiday': 'Warm coat, gloves, and boots'  # Add snowy holiday combination here
        }
    }

    # If the weather and occasion are valid, return the recommended outfit
    try:
        outfit = recommendations[weather][occasion]
        return outfit
    except KeyError:
        return "Sorry, we don't have a recommendation for this combination."
