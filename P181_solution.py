# Homework 3
# P181

test = list(map(int, input().split()))
name = list(map(str, input().split()))
grade = list(map(int, input().split()))

for i in range(test[1]):
    temp = list(map(int, input().split()))
    l = temp[0]
    r = temp[1]
    
    name_1 = name[l-1:r]
    grade_1 = grade[l-1:r]
    grade_dict = {}
    
    for i in range(len(name_1)):
        if name_1[i] not in grade_dict:
            grade_dict[name_1[i]] = [grade_1[i]]
        else:
            grade_dict[name_1[i]].append(grade_1[i])
    #print(grade_dict)
    res = []
    for key in grade_dict:
        res.append(sum(grade_dict[key])/len(grade_dict[key]))
    mean_grade = sum(res) / len(res)
    
    print('{:.7f}'.format(mean_grade))