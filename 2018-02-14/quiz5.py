MAX_STONES = 3

class Collector:
    def __init__(self):
        self.stones = []

    def collectStone(self, stone):
        self.stones.append(stone)
        if len(self.stones) > MAX_STONES:
            self.discardStone()

    def discardStone(self):
        stone = self.stones[0]
        self.stones = self.stones[1:]
        return stone

    def getAllStones(self):
        return self.stones

tivian = Collector()

tivian.collectStone('Mind Gem') # ['Mind Gem']
tivian.collectStone('Soul Gem')# ['Mind Gem', 'Soul Gem']
tivian.collectStone('Space Gem')# ['Mind Gem', 'Soul Gem', 'Space Gem']
tivian.collectStone('Power Gem') #['Soul Gem', 'Space Gem', 'Power Gem']

gem = tivian.discardStone()#['Space Gem', 'Power Gem']
print(gem, 'discarded.') # Soul Gem discarded.

tivian.collectStone('Time Gem')#['Space Gem', 'Power Gem', 'Time Gem']
tivian.collectStone('Reality Gem')#['Power Gem', 'Time Gem', 'Reality Gem']

for gem in tivian.getAllStones():
    print(gem)
    #Power Gem
    #Time Gem
    #Reality Gem






class TradingAccount:
    def __init__(self):
        self.bal = 0

    def getBalance(self):
        return self.bal

    def collectFromSale(self, profit):
        self.bal += profit

    def payForPurchase(self, expense):
        if self.getBalance() >= expense:
            self.bal -= expense
            return True

        return False


bitcoin = TradingAccount()
bitcoin.collectFromSale(1000)
bitcoin.collectFromSale(750)
print(bitcoin.getBalance()) #1750

result = bitcoin.payForPurchase(1500)
print(result) # True
print(bitcoin.getBalance()) #250

result = bitcoin.payForPurchase(500)
print(result) # False
print(bitcoin.getBalance()) #250