class RandomizedSet:

    def __init__(self):
        self.tickers = []
        self.ticker_to_index = {}
        

    def insert(self, val: int) -> bool:
        if val in self.ticker_to_index:
            return False
        self.ticker_to_index[val] = len(self.tickers)
        self.tickers.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.ticker_to_index:
            return False
        
        idx = self.ticker_to_index[val]
        last_val = self.tickers[-1]
        
        # Overwrite the target index with the last element
        self.tickers[idx] = last_val
        self.ticker_to_index[last_val] = idx
        
        # Remove the last element
        self.tickers.pop()
        del self.ticker_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.tickers)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()