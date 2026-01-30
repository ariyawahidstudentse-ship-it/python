class employee:

    def __init__ (self):
        print("Employee has been hired")


    def __del__ (self):
        print("Destructor called, Employee has been fired")


obj = employee()
del obj