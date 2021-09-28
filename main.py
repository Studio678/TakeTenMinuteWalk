from walks import Walks

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    walk1 = Walks(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'])
    if walk1.is_valid_walk():
        print("Walk was perfect")
    else:
        print("Walk was not so perfect")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
