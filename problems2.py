class Calculator():
    def __init__(self):
        self.ResultList = []
        self.repository = []
        with open("HouseData.txt","r",encoding="utf-8") as file:
            housepay = file.readlines()
        for i in housepay:
            a = i.strip("\n")
            data = a.split(" ")
            iniCos = data[0]
            annuFue = data[1]
            annuTax = data[2]
            datas = [iniCos,annuFue,annuTax]
            self.repository.append(datas)
        for n in self.repository:
            self.initial_cost = float(n[0])
            self.annu_fue_cos = float(n[1])
            self.annu_tax_rate = float(n[2])
            self.calculateTotalCost()

    def calculateTotalCost(self):
        totalCost = self.initial_cost + self.annu_fue_cos*10 + self.annu_tax_rate*10*self.initial_cost
        self.ResultList.append(totalCost)
    
    def disPlayCost(self):
        print("The total cost of each house :")
        num = 1
        for i in self.ResultList:
            print(f"{num} house's total cost is {i}")
            num += 1
    
    def selectBestBuy(self):
        BestBuy = min(self.ResultList)
        turn = self.ResultList.index(BestBuy)
        print(f"You should select {turn}. house whose total cost is {BestBuy}")

problem = Calculator()
problem.disPlayCost()
problem.selectBestBuy()