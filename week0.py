# week 0 problem 1
# create a function that returns a list of (vitamins,injections) tuples for each attribute that they need.
# Complete problem statement in README.mds


# your input type should be a list,
# output should also be a list containing tuples
# Example:
# input: [250, 0, 250, 0, 0, 0]
# expected output: [(25,0),(0,0),(25,0),(0,0),(0,0),(0,0)]
# input: [500, 1, 2, 3, 4, 5]
#expected output: "No medicine given"
# HINT: using % operator to find remainder may be helpful
def dose(needs):
    #YOUR SOLUTION STARTS HERE
    if sum(needs)>=500:
        return "No medicine given"
    medicine_list = []
    for attribute in needs:
        if attribute>=250:
            return "No medicine given"
    for attribute in needs:
        if attribute%10==0:
            medicine_list.append((attribute//10,0))
        else:
            medicine_list.append((attribute//10+1,10-attribute%10))
    return medicine_list    
    #YOUR SOLUTION ENDS HERE

