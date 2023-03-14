# Code Signal isCryptSolution

def solution(crypt, solution):
    key = {pair[0]:int(pair[1]) for pair in solution}
    nums = [] 
    for word in crypt:
        num = word_to_num(word, key)
        if num == -1: 
            return False 
        else:
            nums.append(num)
    return nums[0] + nums[1] == nums[2]
    
    
def word_to_num(word, key):
    # Handle the sole 0 edge case
    if key[word[0]] == 0:
        return -1 if len(word) > 1 else 0   
    # Accumulate solution 
    res = 0 
    for i in range(len(word)):
        res += key[word[i]] * (10 ** (len(word) - 1 - i))    
    return res 
