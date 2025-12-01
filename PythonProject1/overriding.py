from ftplib import parse150


class Notification:
    def send(self,message):
        print("Sending notification : ",message)
class EmailNotification(Notification):
    def send(self,message):
        print("Sending email : ",message)
class SMSNotification(Notification):
    def send(self,message):
        print("Sending SMS : ",message)
class PushNotification(Notification):
    def send(self,message):
        print("Sending push : ",message)
n1=EmailNotification()
n1.send("Your order is confirmed")
n2=SMSNotification()
n2.send("Your otp is 677")
n3=PushNotification()
n3.send("You have a new message")

class Payment:
    def pay(self,message):
        print("Mode of payment",message)
class GooglePay(Payment):
    def pay(self,message):
        print("Amount paid using google pay: ",message)
class Phonepay(Payment):
    def pay(self,message):
        print("Amount paid using phone pay: ",message)
class Paytm(Payment):
    def pay(self,message):
        print("Amount paid using paytm pay: ",message)
class Order(Payment):
    def pay(self,message):
        print("Status: ",message)
class OrderNumber(Payment):
    def pay(self,message):
        print("Order number: ",message)

p1=GooglePay()
#p1.pay("500")
p2=Phonepay()
#p2.pay("400")
p3=Paytm()
p3.pay("200")
p4=Order()
p4.pay("Order Confirmed")
p5=OrderNumber()
p5.pay("123")



