import json
import requests

class RazorPayments():
    def __init__(self):       
        # self.username = 'rzp_live_tQ4fsF41dDjqXE'
        # self.password = 'N7sPn4YKSvPxGEzcsXoRqFRo'

        self.username = 'rzp_test_umDK9i0XaxUVDx'
        self.password = 'k471cppXmoz4vzRkYlD7hSIR'

    def check_payment(self,payment_id,details=False):
        r = requests.get(url=f'https://api.razorpay.com/v1/payments/{payment_id}',auth=(self.username,self.password))
        code = r.status_code

        if details:
            return r.json()
        else:
            if code == 400:
                return False
            if code == 200:
                return True

    def normal_refund(self,payment_id,amount):
        r = requests.post(url=f'https://api.razorpay.com/v1/payments/{payment_id}/refund',
         auth=(self.username,self.password), data={
                                    "amount": amount
                                    })

        return r.json()

    def capture(self,payment_id,amount):
        r = requests.post(url=f'https://api.razorpay.com/v1/payments/{payment_id}/capture',auth=(self.username,self.password),
        data={
            "amount":amount,
            "currency":"INR"
        })
        return r

    def razor_refund(payment_id,amount): 
        refund = RazorPayments()
        res = refund.normal_refund(payment_id=payment_id,amount=amount)
        return res