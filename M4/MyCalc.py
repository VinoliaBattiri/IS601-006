class MyCalc:
    ans = 0

    @staticmethod
    def _is_float(val):
        try:
            val = float(val)
            return True
        except:
            return False

    @staticmethod
    def _is_int(val):
        try:
            val = int(val)
            return True
        except:
            return False
        
    @staticmethod
    def _as_number(val):
        if MyCalc._is_int(val):
            return int(val)
        elif MyCalc._is_float(val):
            return float(val)
        else:
            raise Exception("Not a number")

    def calc(self, num1, num2, operator):
        if num1 == "ans":
            return self.calc(self.ans, num2, operator)
        num1 = MyCalc._as_number(num1)
        num2 = MyCalc._as_number(num2)

        if operator == "+":
            self.ans = num1+num2
        elif operator == "-":
            self.ans = num1-num2
        elif operator == "*":
            self.ans = num1*num2
        elif operator == "/":
            self.ans = num1/num2
        return self.ans

if __name__ == '__main__':
    is_running = True
    iSTR = input("Are you ready?")
    calc = MyCalc()
    print(calc)
    if iSTR == "yes":
        while is_running:
            iSTR = input("What is your eq:")
            if iSTR == "quit" or iSTR == "q":
                is_running = False
            else:
                print("Your eq was " + str(iSTR))
                ops = ["+", "/", "*","-"]
                for op in ops:
                    if op in iSTR:
                        nums = iSTR.split(op)
                        r = calc.calc(nums[0].strip(), nums[1].strip(), op)
                        print("R is " + str(r))





    else:
        print("Good bye")
        is_running = False
        
        
        """

class MyCalc:
    def _init_(self):
        self.ans = 0
        
    def add(self, num):
        self.ans += num
        
    def subtract(self, num):
        self.ans -= num
        
    def multiply(self, num):
        self.ans *= num
        
    def divide(self, num):
        if num == 0:
            print("Error: cannot divide by zero")
        else:
            self.ans /= num
        
    def main(self):
        while True:
            user_input = input("Enter a math expression (or 'exit' to quit): ")
            if user_input.lower() == "exit":

if __name__ == "__main__":
    calc = MyCalc()
"""