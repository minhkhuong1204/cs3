import json
phones = [
    {"price": 3000, "name": "iphone 12"},
    {"price": 1000, "name": "iphone 10"},
    {"price": 5000, "name": "iphone 14"},
    {"price": 2000, "name": "iphone 11"},
    {"price": 4000, "name": "iphone 13"}
]


class Phone:
    def __init__(self, price, name):
        self.price = price
        self.name = name


class Node:
    def __init__(self, val) -> None:
        self.key = val
        self.left = None
        self.right = None


def insert(root, val):
    if root == None:
        return Node(val)
    elif root.key.price < val.price:
        root.right = insert(root.right, val)
    elif root.key.price > val.price:
        root.left = insert(root.left, val)
    return root


root = None
for p in phones:
    phone = Phone(p["price"], p["name"])
    root = insert(root, phone)


def tree_to_json(root):
    if root is None:
        return None
    return {
        'key': {
            "price": root.key.price,
            "name": root.key.name
        },
        'left': tree_to_json(root.left),
        'right': tree_to_json(root.right)
    }


tree_json = tree_to_json(root)
print(json.dumps(tree_json, indent=4))
