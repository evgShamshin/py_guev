def get_shipping_cost(count):
        return 1000 + 120 * (count - 1)

print(get_shipping_cost(int(input())))