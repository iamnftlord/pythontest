# Instructions
# Implement score_summary(name, a, b, c). Convert the three score values to numbers. If conversion fails, 
# return Invalid score. If any score is below 0 or above 100, return Invalid score. 
# Otherwise calculate the average, round it to 2 decimal places, choose a grade, and 
# return a three-line report with labels Student, Average, and Grade. Grade is A for 90 and above, 
# B for 80 and above, C for 70 and above, and F below 70.

def score_summary(name, a, b, c):
    try:
        a_num = float(a)
        b_num = float(b)
        c_num = float(c)
    except ValueError:
        return "Invalid score"

    if any(score < 0 or score > 100 for score in [a_num, b_num, c_num]):
        return "Invalid score"

    average = round((a_num + b_num + c_num) / 3, 2)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    else:
        grade = "F"

    report = f"Student: {name}\nAverage: {average}\nGrade: {grade}"
    return report

print(score_summary("John Doe", 85, 92, 78))
