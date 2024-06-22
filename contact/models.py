from django.db import models


select_mode_of_contact=(
    ("email","E-mail"),
    ("phone", "Phone"),
)

select_question_categories = (
    ("general_inquiry","General Inquiry"),
    ("order","Order"),
    ("delivery_and_availability","Delivery and Availability"),
    ("feedback_and_suggestions","Feedback and Suggesstions"),
    ("other","Other"),
)

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    mode_of_contact = models.CharField('Conatct by', 
    max_length=50,choices=select_mode_of_contact,default='email')
    question_categories = models.CharField('How can we help you?', 
    max_length=50,choices=select_question_categories,default='certification')
    message = models.TextField(max_length=3000)

    def __str__(self):
        return self.email