def feedback_percentage(ratings):
    if not ratings:  
        return None  
    positive_count = sum(1 for r in ratings if r >= 4)  
    percentage = (positive_count / len(ratings)) * 100 
    return round(percentage, 2)
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
result =feedback_percentage(ratings)
if result is None:  
    print("No ratings available.")
else:
    print(f"Percentage of positive feedback: {result}%")
