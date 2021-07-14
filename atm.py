class Atm:
    def __init__(self,cardnumber,pin):
        self.carnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("your balnce is 50000")

    def withdrawal(self,amount):
        new_amount = 50000 - amount
        print("your withdrawan amount is" + str(amount) + "tour current balance is" + str(new_amount))

def main():
    card_number = print("enter your card number")
    pin_number = print("enter your pin number")

    new_user = Atm(card_number,pin_number)

    print("choose your activity")
    print("1.Bank Balance 2.Withdrawal")

    activity = int(input("enter your activity number:-"))

    if(activity == 1):
        new_user.check_balance()
    elif(activity == 2):
        amount =  int(input("enter your amount number:-"))
        new_user.withdrawal(amount)
    else:
        print("print a valid number")

if __name__=="__main__":
    main()
