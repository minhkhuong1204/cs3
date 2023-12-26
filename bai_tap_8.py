products = ["cat", "banana", "obama", "car", "cow", "alibaba", "barack"]


nameProduct = input("Nhập tên sản phẩm: ")

for pro in products:
    if pro.startswith(nameProduct):
        print(pro, " ---- index is ", products.index(pro))
