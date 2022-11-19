number = int(input())


def loading_bar(num):
    if num == 100:
        print(f"100% Complete!")
        print(f"[%%%%%%%%%%]")
    else:
        print(f"{num}%", end=" ")
        print("[", end="")
        n = num * 10 // 100
        for percent in range(n):
            print("%", end="")
        for fullstop in range(10 - n):
            print(".", end="")
        print("]")
        print("Still loading...")


loading_bar(number)