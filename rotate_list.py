# Given a sorted list that was rotated unknown number of times, find the number of times it was rotated,
# nums: a sorted rotated list
# count_rotations : returns the number of times the list is rotated.
def count_rotations(given_list):
    #creating position with value 1
    pos=1
    while(pos<(len(given_list))):
        #compare the number at current position to the number before it
        #if the number is lesser than its predecessor, return position.
        if(given_list[pos-1]<=given_list[pos]):
            pos=pos+1
        #Otherwise imcrement position by 1
        else:
            return pos
    return 0

def main():

    test1={'input':{'nums':[4,5,7,8,1,2,3]},'output':4}
    test2={'input':{'nums':[8,1,2,3,5,7]},'output':1}
    test3={'input':{'nums':[9,9,10,2,3,5,7,8]},'output':3}
    test4={'input':{'nums':[1,2,3,4,5,6]},'output':0}
    #In test case 4, the list,[1,2,3,4,5,6], would remain the same if it were rotated 6 times.
    #The possible values are 0,6 and multiples of 6.
    #So, the solution to this problem would be to choose the minimum number of times the list is rotated.
    #Hence, the answer=0
    test5={'input':{'nums':[4]},'output':0}
    tests = [test1, test2, test3, test4, test5]
    accuracy=evaluate_testcases(count_rotations, tests)
    if(accuracy==100):
        print("ALL TEST CASES PASSED!\n")
    print("Accuarcy=",accuracy,"%")



def evaluate_testcases(count_rotations,tests):
    total_cases_passed = 0
    for test in tests:
        output = count_rotations(test['input']['nums'])
        if output == test['output']:
            total_cases_passed = total_cases_passed + 1

    return(total_cases_passed/len(tests))*100
main()