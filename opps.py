
print("Name: Anushka Porwal ")
print("Roll No: 0863CS241039")


class Bank:
    def __init__(self,name,acc_no,bal=1000): #dandar method '__'  is used    self likhna h function m 
        self.name = name
        self.acc_no = acc_no
        self.__bal = bal
        self.trans=[]

    def display(self):
        print('-'*50)
        print('BBank')
        print('-'*50)
        print(f'Holder Name: {self.name}')
        print(f'Account Number: {self.acc_no}')
        print(f'Balance: Rs. {self.__bal}')
        print('-'*50)

    def credit(self,cr_amt):
        self.__bal=self.__bal+cr_amt
        print(f'Hey {self.name}, amount credited successfully Rs. {cr_amt}')
        print(f'Your current balance is Rs. {self.__bal}')
        self.trans.append(('cr', cr_amt))   #Transaction add

    def debit(self,dr_amt):
        if dr_amt>self.__bal:
            print(f'Hey {self.name}, insufficient balance Rs. {self.__bal}')
        else:
            self.__bal=self.__bal-dr_amt
            print(f'Hey {self.name}, amount debited successfully Rs. {dr_amt}')
            print(f'Your current balance is Rs. {self.__bal}')
            self.trans.append(('dr', dr_amt))   #Transaction add

    def passbook(self):
        print('-'*50)
        print('Passbook')
        print('-'*50)
        print('S.No:         Credit/Debit:           Amount:')
        print('-'*50)
        i = 1
        for a, b in self.trans:
            print(f'{i}                {a}                     Rs. {b}')
            i += 1
        print('-'*50)
        print(f'Your Total balance is Rs. {self.__bal}')
        print('-'*50)

        
b1=Bank("Anushka", "12345", 5000)
b1.display()
b1.credit(2500)
b1.debit(1000)
b1.debit(7000)
b1.credit(1500)
b1.passbook()
