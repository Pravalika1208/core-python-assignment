def calculate_averages(students):
    averages = {}
    for name, marks in students.items():
        average = sum(marks) / len(marks)
        averages[name] = round(average, 2)
    return averages
def find_top_performer(averages):
    return max(averages, key=averages.get)
students = {"John": [85, 78, 92],"Alice": [88, 79, 95],"Bob": [70, 75, 80]}
average_marks = calculate_averages(students)
top_performer = find_top_performer(average_marks)
print("Average Marks:", average_marks)
print("Top Performer:", top_performer)
