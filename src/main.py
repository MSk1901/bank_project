import os

from src.processing import sort_by_date, sort_by_state
from src.utils import get_data, transaction_amount
from src.widget import fix_date, make_numbers

PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")


def main() -> None:
    transactions = get_data(PATH_TO_FILE)
    tr_filtered = sort_by_state(transactions)
    tr_sorted = sort_by_date(tr_filtered)
    five_tr = tr_sorted[:5]
    for tr in five_tr:
        date = fix_date(tr["date"])
        desc = tr["description"]
        from_ = tr.get("from")
        if from_:
            from_new = f"{make_numbers(from_)} -> "
        else:
            from_new = ""
        to_ = make_numbers(tr["to"])
        amount = transaction_amount(tr)
        print(f"""{date} {desc}
{from_new}{to_}
{amount} руб.\n""")


if __name__ == '__main__':
    main()
