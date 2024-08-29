class student():
    def __init__(self,name,age,school,roll_num):
        self.name=name
        self.age=age
        self.school=school
        self.roll_num=roll_num

    def details(self):
        print(f"name of student : {self.name}\nage : {self.age} \nschool name : {self.school}\nroll number : {self.roll_num}")

    def mark(self,che,phy,maths,bio):
        self.che=che
        self.phy=phy
        self.maths=maths
        self.bio=bio

    def add_mark(self):
        return (self.che+self.phy+self.maths+self.bio)/4
    

user=input('enter name :')
user1=int(input('age '))
user2=input('school ')
user4=int(input('enter roll num'))
obj=student(user,user1,user2,user4)
obj.details()
obj.mark(80,70,90,95)
print(f"averange mark {obj.add_mark()}")