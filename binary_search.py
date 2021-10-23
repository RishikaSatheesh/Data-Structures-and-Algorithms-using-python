def find(cards,query,low,high):
    while low<high:
        mid=(low+high)//2
        if(query>cards[mid]):
            high=mid
            find(cards,query,low,high)
        elif(query<cards[mid]):
            low=low+1
            find(cards,query,low,high)
        else:
            return mid

    return -1

def main():
    tests = [{'input': {'cards': [9, 7, 5, 4, 2, 1], 'query': 2}, 'output': 4},
                {'input': {'cards': [99, 83, 76, 64, 61, 52, 50, 48, 42, 39, 31, 29, 23, 16, 11, 8, 3], 'query': 42},
                 'output': 8},
                {'input': {'cards': [19, 17, 12, 9, 4, 2], 'query': 1}, 'output': -1},
                {'input': {'cards': [73, 61, 56, 51, 47, 43, 37, 28, 19, 13, 9, 8, 3, 1], 'query': 19}, 'output': 8}]

    total=0
    len_tests=len(tests)
    for test in tests:
        a=find(test['input']['cards'],test['input']['query'],0,len(test['input']['cards']))
        if(a==test['output']):
            total=total+1
    accuracy=(total/len_tests)*100
    print("Accuracy=%.2f "%accuracy,"%")
main()