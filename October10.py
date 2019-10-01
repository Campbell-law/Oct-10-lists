# This is the grading program we looked at earlier


# 4) Grading program - if score is > 90 you get an A,
##  > 80 < 90 you get a B
##  > 70 < 80 a C
##  > 60 < 70 a D
## anything else you flunk

grade = 55

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("You Flunked!")


# We changed it to a Function:

def grader(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "You Flunked!"

g = grader(60)
print(g)

grades = [75,80,90,60,65,85]

def term_grader(grade):
    term = sum(grade) / len(grade)
    return grader(term)

print(term_grader(grades))