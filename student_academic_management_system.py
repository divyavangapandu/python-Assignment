class Student:
    def __init__(self,id,name,m1,m2,m3,byear,fee):
        self.id=id
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.byear=byear
        self.fee=fee

    def average(self):
        return (self.m1+self.m2+self.m3)/3

    def cgpa(self):
        return self.average()/10

    def age(self):
        return 2026-self.byear

    def balance(self):
        return 50000-self.fee


class College:
    def __init__(self,code,name,loc):
        self.code=code
        self.name=name
        self.loc=loc

    def display(self,s):
        print("\nStudent ID:",s.id)
        print("Name:",s.name)
        print("Marks:",s.m1,s.m2,s.m3)
        print("Average Marks:",s.average())
        print("CGPA:",s.cgpa())
        print("Age:",s.age())
        print("Fee Paid:",s.fee)
        print("Fee Balance:",s.balance())


c=College("ANIL","ANITS College","Visakhapatnam")
print("College Code:",c.code)
print("College Name:",c.name)
print("Location:",c.loc)

s1=Student(61,"Divya",90,92,95,2007,30000)
s2=Student(29,"keerthi",92,89,91,2006,25000)
s3=Student(52,"moni",93,91,92,2006,40000)

c.display(s1)
c.display(s2)
c.display(s3)
