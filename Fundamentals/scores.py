import random

def grade(reps):
    print "Scores and Grades:"
    for x in range(0, reps):
        score = random.randint(60, 101)
        if score >= 60 and score < 70:
             print "Score:", score, "; Your grade is D"
        if score >= 70 and score < 80:
             print "Score:", score, "; Your grade is C"
        if score >= 80 and score < 90:
             print "Score:", score, "; Your grade is B"
        if score >= 90 and score <= 100:
             print "Score:", score, "; Your grade is A"
        else:
            print "Well you failed. Way to go LOSER."
    print "End of the program. Byeeeeeeee!"

grade(10)