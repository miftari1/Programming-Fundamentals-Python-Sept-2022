number_inputs = int(input())
for _ in range(number_inputs):
    text = input()
    if "," in text or "." in text or "_" in text:
        print(f"{text} is not pure!")
    else:
        print(f"{text} is pure.")