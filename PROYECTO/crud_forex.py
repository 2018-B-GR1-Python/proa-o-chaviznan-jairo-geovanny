import pandas as pd
import properties
from models import Transaction
from managers import TransactionManager


def load_transactions(file):
    return pd.read_csv(file)


def parse_options(options_in_string):
    return options_in_string.split(',')


def build_transaction(local_time, ask, bid, ask_volume, bid_volume):
    transaction = Transaction()
    transaction.local_time = local_time
    transaction.ask = ask
    transaction.bid = bid
    transaction.ask_volume = ask_volume
    transaction.bid_volume = bid_volume
    return transaction


def main():
    quit = False
    transactions = load_transactions("EURUSD_Ticks_26.11.2018-26.11.2018.csv")
    manager = TransactionManager(transactions)
    while not quit:
        try:
            value = int(input(properties.OPTIONS_INIT))
        except:
            print("Valor no permitido\n")
        if value == 6:
            quit = True
        else:
            if value == 1:
                manager.list()

            elif value == 2:
                values = input(properties.OPTIONS_SEARCH)
                key, value = parse_options(values)
                print("Resultado:\n{}".format(manager.search(key, value)))

            elif value == 3:
                values = input(properties.OPTIONS_INSERT)
                options = parse_options(values)
                transaction = build_transaction(*options)
                manager.insert(transaction)

            elif value == 4:
                values = input(properties.OPTIONS_UPDATE)
                index, key, new_value = parse_options(values)
                manager.update(index, key, new_value)
            elif value == 5:
                values = input(properties.OPTIONS_DELETE)
                index = parse_options(values)
                manager.delete(index)


if __name__ == "__main__":
    main()
