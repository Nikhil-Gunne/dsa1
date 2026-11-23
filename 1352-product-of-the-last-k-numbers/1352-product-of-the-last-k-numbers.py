class ProductOfNumbers:

    def __init__(self):

        self.product = []
        self.zeroCnt = []
        

    def add(self, num: int) -> None:
        if self.product:
            self.product.append((self.product[-1]*num) if num else 1)
            self.zeroCnt.append((self.zeroCnt[-1] + 1) if num == 0 else self.zeroCnt[-1])
        else:
            self.product.append(num if num else 1)
            self.zeroCnt.append(1 if num == 0 else 0)
    

    def getProduct(self, k: int) -> int:
        if k < len(self.product):
            return self.product[-1]//self.product[len(self.product)-k-1] if self.zeroCnt[-1] - self.zeroCnt[len(self.zeroCnt)-k-1] < 1 else 0
        return self.product[-1] if self.zeroCnt[-1] < 1 else 0
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)