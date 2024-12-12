

def  send_email(message,recipient,sender = "university.help@gmail.com"):
    valid_dom =( ".com",".ru",".net")
    if "@" not in recipient or not recipient.endswith(valid_dom):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if "@" not in sender or not sender.endswith(valid_dom):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if recipient==sender:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
        return





send_email("Hello!", "student@gmail.com")
send_email("Hello!", "university.help@gmail.com")
send_email("Hello!", "student@domain.org")  # Некорректный e-mail
send_email("Hello!", "student@gmail.com", sender="support@company.net")