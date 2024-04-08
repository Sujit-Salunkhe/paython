import time 

# sujit = 'sujit'
# sujit2 = 'salunkhe'
def lcs_recursive(list1,list2,idx1 = 0,idx2 =0):
    # print('list1c:',list1[idx1],'idx1c:',idx1 ,'list2c:' ,list2[idx2],'idx2c:',idx2)
    if idx1 == len(list1) or idx2 == len(list2): 
        return 0
    elif list1[idx1] == list2[idx2]:
        return 1 + lcs_recursive(list1,list2,idx1+1,idx2+1)
    else:
        return max(lcs_recursive(list1,list2,idx1+1,idx2),lcs_recursive(list1,list2,idx1,idx2+1))


# print(lcs_recursive('FKJFIKFK','IEOWLEDS'))


def lcs_memo(seq1,seq2):
    memo = {}
    def recurse (idx1,idx2):
        # print(memo)
        key = (idx1,idx2)
        if key in memo:
            return memo[key]
        elif idx1 == len(seq1) or idx2 == len(seq2):
             memo[key] = 0
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recurse(idx1+1,idx2+1)
        else:
            memo[key] = max(recurse(idx1+1,idx2),recurse(idx1,idx2+1))
        return memo[key]
    return recurse(0,0)

print(lcs_memo('sujit','salunkhe'))

def get_value(matrix,idx1,idx2):
    if idx1 < 0 or idx2 < 0:
        return 0
    return matrix[idx1][idx2]

def lcs_dp(seq1,seq2):
    m,n = len(seq1),len(seq2)
    results = [[0 for _ in range(n)] for _ in range(m)]
    for idx1 in range(m):
        for idx2 in range(n):
            if seq1[idx1] == seq2[idx2]:
                results[idx1][idx2] = 1 + get_value(results,idx1-1,idx2-1)
            else:
                results[idx1][idx2] = max(results[idx1 -1][idx2],results[idx1][idx2-1])
            
    return results[-1][-1] if m > 0 and n > 0 else 0

def napsack(capacity,weights,profits,idx=0):
    
    if idx == len(capacity):
        return 0
    elif weights[idx] <= capacity:
        option1 = profits[idx] + napsack(capacity -weights[idx],weights,profits,idx +1)
        option2 =  napsack(capacity,weights,profits,idx +1)
        return max(option1,option2)
    else:
        napsack(capacity,weights,profits,idx +1)

def knapSack(capacity,weights,profits):
    results =[[0 for _ in range(capacity + 1)] for _ in range(len(weights))]