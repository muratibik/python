class customer:
    money = 100

    def draw(self):
        self.money -= 1

    def checkmoney(self):
        if self.money <= 0:
            print('you have not any money')
        else:
            print(str(self.money) + " money left")

customer1 = customer()
customer2 = customer()

customer1.draw()
customer1.draw()
customer2.draw()
customer1.checkmoney()
customer2.checkmoney()
