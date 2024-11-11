grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = sorted({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
list_students = list(students)
Aaron =(sum(grades[0])/len(grades[0]))
Bilbo = (sum(grades[1])/len(grades[1]))
Johnny = (sum(grades[2])/len(grades[2]))
Khendrik = (sum(grades[3])/len(grades[3]))
Steve = (sum(grades[4])/len(grades[4]))
all_students = [
    [list_students [0], Aaron],
    [list_students [1], Bilbo],
    [list_students [2], Johnny],
    [list_students [3], Khendrik],
    [list_students [4], Steve]
]
students_dict = dict(all_students)
print(students_dict)