#wap to take 5 mark of student display all mark,total mark and avrage mark
math=int(input("enter math mark="))
physics=int(input("enter physics mark="))
eng=int(input("enter eng mark="))
chem=int(input("enter chem mark="))
bio=int(input("enter bio mark="))
total_mark=math+physics+eng+chem+bio
print(math,physics,eng,chem,bio)
print(total_mark)
print("average mark=",total_mark/5)
