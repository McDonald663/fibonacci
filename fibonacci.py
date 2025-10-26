def fibonacci(index):
    if index <0:
        return
    elif index<=1:
        return index
    else:
        return fibonacci(index-1)+fibonacci(index-2)
print(fibonacci(2))
