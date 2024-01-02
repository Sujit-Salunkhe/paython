class Notebook:
    def __init__(self,title,username,likes):
        self.title,self.username,self.likes = title,username,likes

    def __repr__(self) -> str:
        return 'Notebook <"{}/{}",{} Likes>'.format(self.username,self.title,self.likes)


def compare_likes(nb1, nb2):
    if nb1.likes >nb2.likes:
        return 'lesser'
    elif nb1.likes == nb2.likes:
        return 'equal'
    elif nb1.likes < nb2.likes:
        return 'greater'

def default_likes(nb1, nb2):
    if nb1.likes >nb2.likes:
        return 'lesser'
    elif nb1.likes == nb2.likes:
        return 'equal'
    elif nb1.likes < nb2.likes:
        return 'greater'

def merge_sort(objs,compare=default_likes):
    if len(objs) < 2:
        return objs
    mid =len(objs) //2
    return (merge_sort(objs[:mid],compare),
            merge_sort(objs[mid:],compare),compare)

def merge(left,right,compare):
    i,j,merged = 0,0,[]
    while i < len(left) and j < len(right):
        result =compare(left[i],right[j])
        if result == 'lesser' or result =='equal':
            merged.append(left[i])
            i +=1
        else:
            merged.append(right[j])
            j +=1
    return merged + right[i:] + left [j:]

a = list(range(5))
print(a[5:])
            