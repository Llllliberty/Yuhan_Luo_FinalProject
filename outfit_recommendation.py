def recommend_outfit(weather, occasion):
    recommendations = {
        'sunny': {
            'casual': 'T-shirt and shorts',
            'interview': 'Formal shirt and pants',
            'date': 'Nice shirt and jeans',
            'party': 'Stylish dress or shirt and jeans'
        },
        'rainy': {
            'casual': 'Raincoat and boots',
            'interview': 'Formal shirt, pants, and umbrella',
            'date': 'Waterproof jacket and comfortable shoes',
            'party': 'Stylish jacket and boots'
        },
        'cloudy': {
            'casual': 'Light sweater and jeans',
            'interview': 'Smart blouse and skirt',
            'date': 'Smart-casual outfit',
            'party': 'Chic blouse and skirt'
        }
    }

    # If the weather and occasion are valid, return the recommended outfit
    try:
        outfit = recommendations[weather][occasion]
        return outfit
    except KeyError:
        return "Sorry, we don't have a recommendation for this combination."
