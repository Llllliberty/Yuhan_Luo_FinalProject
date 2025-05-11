def review_outfit(worn_clothes, weather):
    if weather == 'sunny' and 'T-shirt' in worn_clothes:
        return "😊 Your outfit was perfect for the sunny weather!"
    elif weather == 'rainy' and 'raincoat' in worn_clothes:
        return "😊 Your outfit was perfect for the rainy weather!"
    elif weather == 'cloudy' and 'sweater' in worn_clothes:
        return "😊 Your outfit was suitable for the cloudy weather!"
    else:
        return "😢 The outfit might not have been suitable for the weather."
