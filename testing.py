import os

import requests
from dotenv import load_dotenv

load_dotenv()

token1 = os.getenv("token1")
token2 = os.getenv("token2")
token3 = os.getenv("token3")
token4 = os.getenv("token4")

portAccount = os.getenv("portAccount")
portTransaction = os.getenv("portTransaction")
baseUrl = os.getenv("baseUrl")

urlAccount = f"http://{baseUrl}:{portAccount}/api/v1"
urlTransaction = f"http://{baseUrl}:{portTransaction}/api/v1"


def first():
    r = requests.post(f"{urlAccount}/account", headers={"Authorization": f"Bearer {token1}"}, json={"type": "checking"})
    if r.status_code != 201:
        print(f"Status code: {r.status_code}")
        print(f"Error: {r.json()}")
        return
    acc = r.json()
    print(f"Account: {acc}")

    r = requests.patch(f"{urlAccount}/account/{acc['accountID']}/deposit",
                       headers={"Authorization": f"Bearer {token1}"},
                       json={"amount": 50.20})
    if r.status_code != 204:
        print(f"Status code: {r.status_code}")
        return
    print(f"Amount {50.20} was deposited")

    r = requests.get(f"{urlAccount}/account/{acc['accountID']}", headers={"Authorization": f"Bearer {token1}"})
    if r.status_code != 200:
        print(f"Status code: {r.status_code}")
        print(f"Error: {r.json()}")
        return
    acc = r.json()
    print(f"Account: {acc}")

    r = requests.patch(f"{urlAccount}/account/{acc['accountID']}/close", headers={"Authorization": f"Bearer {token1}"})
    if r.status_code != 204:
        print(f"Status code: {r.status_code}")
        print(f"Error: {r.json()}")
        return
    print("Account was closed")


def second():
    r = requests.post(f"{urlAccount}/account", headers={"Authorization": f"Bearer {token2}"}, json={"type": "checking"})
    if r.status_code != 201:
        print(f"Status code: {r.status_code}")
        print(f"Error: {r.json()}")
        return
    acc1 = r.json()
    print(f"Account 1: {acc1}")

    r = requests.post(f"{urlAccount}/account", headers={"Authorization": f"Bearer {token2}"}, json={"type": "saving"})
    if r.status_code != 201:
        print(f"Status code: {r.status_code}")
        return
    acc2 = r.json()
    print(f"Account 2: {acc2}")

    r = requests.patch(f"{urlAccount}/account/{acc1['accountID']}/deposit",
                       headers={"Authorization": f"Bearer {token2}"},
                       json={"amount": 50})
    if r.status_code != 204:
        print(f"Status code: {r.status_code}")
        print(f"Error: {r.json()}")
        return
    print(f"Amount {50} was deposited")

    req = {
        "amount": 50,
        "recipientAccountID": acc1["accountID"],
        "recipientID": acc1["userID"],
        "senderAccountID": acc1["accountID"],
        "type": 1,
    }

    r = requests.post(f"{urlTransaction}/transaction", headers={"Authorization": f"Bearer {token2}"}, json=req)
    if r.status_code != 201:
        print(f"Status code: {r.status_code}")
        print(f"Error: {r.json()}")
        return
    print(f"Transaction: {r.json()}")

    r = requests.patch(f"{urlAccount}/account/{acc1['accountID']}/withdraw",
                       headers={"Authorization": f"Bearer {token2}"},
                       json={"amount": 20})
    if r.status_code != 204:
        print(f"Status code: {r.status_code}")
        print(f"Error: {r.json()}")
        return
    print(f"Amount {20} was withdrawn")

    req = {
        "amount": 20,
        "recipientAccountID": acc2["accountID"],
        "recipientID": acc2["userID"],
        "senderAccountID": acc1["accountID"],
        "type": 1,
    }

    r = requests.post(f"{urlTransaction}/transaction", headers={"Authorization": f"Bearer {token2}"}, json=req)
    if r.status_code != 201:
        print(f"Status code: {r.status_code}")
        print(f"Error: {r.json()}")
        return
    print(f"Transaction: {r.json()}")

    r = requests.get(f"{urlAccount}/accounts/all/transactions", headers={"Authorization": f"Bearer {token2}"})
    if r.status_code != 200:
        print(f"Status code: {r.status_code}")
        print(f"Error: {r.json()}")
        return
    print(r.json())


def three():
    r = requests.post(f"{urlAccount}/account", headers={"Authorization": f"Bearer {token3}"},
                      json={"type": "checking"})
    if r.status_code != 201:
        print(f"Status code: {r.status_code}")
        print(f"Error: {r.json()['error']}")
        return
    acc1 = r.json()
    print(f"Account: {acc1}")

    r = requests.post(f"{urlAccount}/account", headers={"Authorization": f"Bearer {token3}"},
                      json={"type": "saving"})
    if r.status_code != 201:
        print(f"Status code: {r.status_code}")
        print(f"Error: {r.json()['error']}")
        return
    acc2 = r.json()
    print(f"Account: {acc2}")

    r = requests.patch(f"{urlAccount}/account/{acc1['accountID']}/close",
                       headers={"Authorization": f"Bearer {token3}"})
    if r.status_code != 204:
        print(f"Status code: {r.status_code}")
        print(f"Error: {r.json()['error']}")
        return
    print("Account was closed")

    r = requests.get(f"{urlAccount}/accounts/all", headers={"Authorization": f"Bearer {token3}"})
    if r.status_code != 200:
        print(f"Status code: {r.status_code}")
        print(f"Error: {r.json()['error']}")
        return
    print(r.json())


def four():
    r = requests.post(f"{urlAccount}/account", headers={"Authorization": f"Bearer {token4}"}, json={"type": "checking"})
    if r.status_code != 201:
        print(f"Status code: {r.status_code}")
        print(f"Error: {r.json()}")
        return
    acc = r.json()
    print(f"Account: {acc}")

    req = {
        "amount": 30,
        "recipientAccountID": acc["accountID"],
        "recipientID": acc["userID"],
        "senderAccountID": acc["accountID"],
        "type": 1,
    }

    r = requests.post(f"{urlTransaction}/transaction", headers={"Authorization": f"Bearer {token4}"}, json=req)
    if r.status_code != 201:
        print(f"Status code: {r.status_code}")
        print(f"Error: {r.json()}")
        return
    print(f"Transaction: {r.json()}")

    r = requests.get(f"{urlTransaction}/transaction/{acc['accountID']}/all",
                     headers={"Authorization": f"Bearer {token4}"}, json=req)
    if r.status_code != 200:
        print(f"Status code: {r.status_code}")
        print(f"Error: {r.json()}")
        return
    transaction = r.json()[0]
    print(f"Transaction: {transaction}")

    r = requests.delete(f"{urlTransaction}/transaction/{transaction['id']}",
                        headers={"Authorization": f"Bearer {token4}"}, json=req)
    if r.status_code != 204:
        print(f"Status code: {r.status_code}")
        print(f"Error: {r.json()}")
        return
    print("Transaction was deleted")


if __name__ == "__main__":
    first()
    print("=====\n")
    second()
    print("=====\n")
    three()
    print("=====\n")
    four()
