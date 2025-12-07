import argparse, csv

parser = argparse.ArgumentParser(description="Отслеживание расходов^^")

parser.add_argument("command", type=str, help="Команда, которую должна выполнить программа.")
parser.add_argument("--description", "-d", type=str, help="Описание расхода")
parser.add_argument("--amount", "-a", type=int, help="Сумма расхода")

args = parser.parse_args()

field = ['ID', 'Date', 'Description', 'amount']

def exp_add():
    description = args.description
    amount = args.amount
    id = get_id()
    date = get_date()
    with open('database.csv', 'a') as file:
        new_row = [[id, date, description, amount]]
        csv_writer = csv.writer(file)
        csv_writer.writerows(new_row)


# нужна оптимизация
def get_id() -> str:
    with open("database.csv", "r") as file:
        csv_dict_reader = csv.DictReader(file)
        temp = [0]
        for row in csv_dict_reader:
            temp.append(row["ID"])
            # if row["ID"]-1 != temp[-1]:
            #     break
        return str(temp[-1])


def get_date() -> str:
    return "2025"

if args.command == "add":
    exp_add()