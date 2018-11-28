import pandas as pd


class TransactionManager:

    def __init__(self, transactions):
        self.transactions = transactions

    def list(self):
        print(self.transactions)

    def search(self, key, value):
        if key != 'Local time':
            value = float(value)
        return self.transactions[self.transactions[key] == value]

    def update(self, index, key, value):
        print('{}/{}:{}'.format(index, key, value))
        # self.transactions.loc[index, key] = 
        self.transactions.set_value(index, key, value)

    def delete(self, index):
        index = int(index[0])
        self.transactions = self.transactions[self.transactions.index != index]

    def insert(self, transaction):
        row = [
            transaction.local_time,
            transaction.ask,
            transaction.bid,
            transaction.ask_volume,
            transaction.bid_volume,
        ]
        new_df = pd.DataFrame([row], columns=[
                                "Local time",
                                "Ask",
                                "Bid",
                                "AskVolume",
                                "BidVolume"
                            ])
        self.transactions = self.transactions.append(new_df)
