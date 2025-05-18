def review_outfit(worn_clothes, weather):
    # Check if the outfit matches the weather
    if weather == 'sunny' and 'T-shirt' in worn_clothes:
        return "😊 Your outfit was perfect for the sunny weather!"
    elif weather == 'rainy' and 'raincoat' in worn_clothes:
        return "😊 Your outfit was perfect for the rainy weather!"
    elif weather == 'cloudy' and 'sweater' in worn_clothes:
        return "😊 Your outfit was suitable for the cloudy weather!"
    else:
        # If the outfit doesn't match the weather, add a suggestion
        suggestion = ""
        if weather == 'sunny':
            suggestion = "Next time, try wearing something light like a T-shirt and shorts."
        elif weather == 'rainy':
            suggestion = "Next time, make sure to wear a raincoat and waterproof shoes."
        elif weather == 'cloudy':
            suggestion = "Next time, a sweater or light jacket would be perfect for cloudy weather."
        
        # Include additional check for any other weather condition
        if weather == 'snowy':
            suggestion = "Next time, make sure to wear warm clothes, like a sweater and boots."

        return f"😢 The outfit might not have been suitable for the weather. \n{suggestion}"
