#Задача "Рассылка писем"

def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if '@' not in recipient or '@' not in sender:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif not (recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net')):
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif not (sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net')):
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender,  'на адрес', recipient)




    else:
        print ('ok')


send_email('Это сообщение для проверки связи', 'qwert@gmail.com')