# 10. Create a class BANK and with two function simple interest and compound interest. 
#  U need to create instance for pnb, icici and hdfc banks with corresponding input.

class Bank:

    def __init__(self,bank_name,P,R,T):
      self.bank_name= bank_name
      self.principle = P
      self.rate = R
      self.time = T


    def simple_interest(principal, rate, time):

        SI = (principal * rate * time)/100
        print("simple interest is", SI)

    simple_interest(3000, 7, 1)


    def compound_interest(principal, rate, time):

        Amount = principal * (pow((1 + rate / 100), time))
        CI = Amount - principal
        print("Compound interest is", CI)

    compound_interest(10000, 10.25, 5)

#instances of the class Bank
pnb = Bank("PNB",5000,7,1)
icici = Bank("ICICI",3000,10,4)
hdfc = Bank("HDFC",5000,9,6)
