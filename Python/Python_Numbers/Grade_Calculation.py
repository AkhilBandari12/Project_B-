"""
90%        --   A
80%-90%    --   B
70%-80%    --   C
60%-70%    --   D
50%-60%    --   E
<50%       --   F (Fail)
"""

sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5

if(avg>=90):
    print("Grade: A")
elif(avg>=80 and avg<90):
    print("Grade: B")
elif(avg>=70 and avg<80):
    print("Grade: C")
elif(avg>=60 and avg<70):
    print("Grade: D")
elif(avg>=50 and avg<60):
    print("Grade: E")
else:
    print("Grade: F")