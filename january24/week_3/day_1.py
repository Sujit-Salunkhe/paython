# # if s == t perfect and number operations gt len(t) so return Yes.
# # loop through the s and t common elements and minuse k if k reaches to zero return no and do the operations till s becames t


# def append_and_delete(s,t,k):
#     common =0
#     non_common = 0
#     if s == t and len(s)*2 <= k:
#             return 'Yes'
#     if s == t and k % 2 == 0:
#         return 'yes'
#     n = min(len(s),len(t))
#     for i in range(n+1):
#         # print('i',i,'s',s[i],'t',t[i])
#         # if i == len(s) or i == len(t):
#         #      finish = i
#         #      break
#         if s[i] != t[i]:
#             #   common +=1
#               finish = i
#               break
#     first = s[finish:]
#     second= t[finish:]
#     print(finish,first,second)
#     answer = ((len(first) + len(second)) - k)
#     print(answer)
#     if answer == 0:
#          return 'Yes'
#     else:
#          return 'No'

def append_and_delete(s,t,k):
    
    if s == t and len(s)*2 <= k:
            return 'Yes'
    if s == t and k % 2 == 0:
        return 'yes'
    n = min(len(s),len(t))
    for i in range(n+1):
        if i == n:
             finish = i
             break
        if s[i] != t[i]:
              finish = i
              break
    first = s[finish:]
    second= t[finish:]
    print(finish,'first',first,'second',second)
    answer = (abs(len(first) + len(second)) - k)
    if len(first) == 0 or len(second) == 0:
         if len(first) % k == 0 and len(second) % k == 0:
              return 'Yes'
         else:
              return 'No'

    if answer <= 0:
             return 'Yes'
    else:
         return 'No'

     
    
        

                

# case='zzzzz'
# case2='zzzzzzz'
# op=4
case3='y'
case4 ='yu'
op=2
s='ashley'
t='ash'
k=2
print(append_and_delete(case3,case4,op))
