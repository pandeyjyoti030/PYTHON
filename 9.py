#9. Create class OOPS and implement all oops concept in that.

class Gojo:
    def __init__(self,var1) :
        self.obj1= var1
        print("constructor of class Gojo :", self.obj1)

    def function(self) :
        print("function of class Gojo :", self.obj1)
    
    # #METHOD OVERLOADING
    # def function(self,val) :
    #     self.val = val
    #     print("another function of class Gojo :", self.obj1)
    #     print("demonstrating method overloading :", self.val)

# obj1= Gojo("mission completed")
# obj1.function("method overloading trial")

# b = Gojo(35)
# b.function()

# #INHERITANCE
class Light(Gojo):
    def __init__(self,var, x) :
        self.obj1= var
        print("constructor of class Light :", self.obj1)
        super().__init__(x)

    def function2(self) :
        print("function of class Light :", self.obj1)
        super().function()
    
#obj1 = Light(22,11)
#obj1.function2()
#obj1.function1()

#     #METHOD OVERRIDING
    def function(self) :
        print("demonstrating method overloading ")
        print("same function used in class Gojo :", self.obj1)


# # a= Gojo(5)
# # a.function()

obj1 = Light(22,11)
obj1.function2()
obj1.function1()


