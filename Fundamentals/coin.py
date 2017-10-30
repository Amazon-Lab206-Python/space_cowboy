import random

def toss(reps):
    # print new_toss
    attempts = 1
    heads = 0
    tails = 0
    result = ""
    result_string_complete = ""

    for x in range(1, reps):
        new_toss = random.randint(0,1)
        if new_toss == 1:
            heads += 1
            result = "head"
            print "Attempt #", attempts, ": Throwing a coin... It's a ", result, "! Got ", heads, "head(s) so far and", tails, "tail(s) so far"
        else:
            tails += 1
            result = "tail"
            print "Attempt #", attempts, ": Throwing a coin... It's a ", result, "! Got ", heads, "head(s) so far and", tails, "tail(s) so far"
        attempts += 1

toss(5001)