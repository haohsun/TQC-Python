student1,student2,student3 = list(),[],list()

for j,n in zip((student1,student2,student3),("1st","2nd","3rd")):
    print("The "+n+" student:")
    for i in range(5):
        j.append(eval(input()))

for i,j in zip((student1,student2,student3),range(1,4)):
    print("Student",j)
    print("#Sum",sum(i))
    print("#Average {:.2f}".format(sum(i)/len(i)))