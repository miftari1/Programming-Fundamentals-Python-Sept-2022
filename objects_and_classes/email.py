class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails = []


while True:
    line = input()
    if line == "Stop":
        break
    elements = line.split(" ")
    sender = elements[0]
    receiver = elements[1]
    content = elements[2]
    email = Email(sender, receiver, content)
    emails.append(email)

send_emails = list(map(int, input().split(", ")))
for index in send_emails:
    emails[index].send()

for email in emails:
    print(email.get_info())
