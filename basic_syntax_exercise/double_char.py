text = input()
while text != "End":
    if text == "SoftUni":
        text = input()
        continue
    else:
        double_charred_text = ""
        for letter in text:
            for i in range(2):
                double_charred_text += letter
        print(double_charred_text)
        text = input()