import pandas as pd

my_data = 'forcebrute.csv'
wallet = 500
result = []
temp = []
temp2 = []
action = []
price = []
benefice = []
all_action = []
all_price = []
all_benefice = []


def read_data(my_data):
    df = pd.read_csv((my_data), sep=";")
    df["benefice"] = df["price"] * df["profit"] / 100
    return df


def combination(actions, prices, benefices, position_start=0, i=0):
    if position_start < len(actions):
        for position in range(position_start, len(actions)):

            del temp[i:]
            temp.append(position)

            temp2.clear()
            action.clear()
            price.clear()
            benefice.clear()
            for value in range(0, len(temp)):
                action.append(actions[temp[value]])
                price.append(prices[temp[value]])
                benefice.append(benefices[temp[value]])

            all_action.append((action.copy()))
            all_price.append((sum(price.copy())))
            all_benefice.append((sum(benefice.copy())))

            combination(
                actions,
                prices,
                benefices,
                position_start=position+1,
                i=i+1
            )


def analyse(all_action, all_price, all_benefice):
    final_df = pd.DataFrame({
        "name": all_action,
        "price": all_price,
        "benefice": all_benefice
    })

    inferior_to_500 = final_df.loc[
        (final_df["price"] <= wallet) &
        (final_df["benefice"])
    ].sort_values(by=['benefice'], ascending=False)

    print('=======================\n')
    print('Liste des actions à acheter :\n')
    print(inferior_to_500.iloc[0][0])
    print('=======================\n')
    print(
        "Montant total d'actions achetées : " +
        str(inferior_to_500.iloc[0][1])
    )
    print("Bénéfices : " + str(inferior_to_500.iloc[0][2]))
    print('=======================\n')


def main():
    df = read_data(my_data)

    actions = df["name"].to_list()
    prices = df["price"].to_list()
    benefices = df["benefice"].to_list()

    combination(actions, prices, benefices)
    analyse(all_action, all_price, all_benefice)


if __name__ == '__main__':
    main()
