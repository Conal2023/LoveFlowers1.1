from django.db import models


select_mode_of_contact = (
    ("email", "E-mail"),
    ("phone", "Phone"),
)

select_question_categories = (
    ("general_inquiry", "General Inquiry"),
    ("order", "Order"),
    ("delivery_and_availability", "Delivery and Availability"),
    ("feedback_and_suggestions", "Feedback and Suggesstions"),
    ("other", "Other"),
)


class Contact(models.Model):
    name = models.CharField(max_length=25, verbose_name="")
    email = models.EmailField(verbose_name="")
    phone = models.CharField(max_length=10, verbose_name="")
    mode_of_contact = models.CharField(
        max_length=50,
        choices=select_mode_of_contact,
        default='email',
        verbose_name="Contact by"
    )
    question_categories = models.CharField(
        max_length=50,
        choices=select_question_categories,
        default='certification',
        verbose_name="How can we help you?"
    )
    message = models.TextField(max_length=3000, verbose_name="Message")

    def __str__(self):
        return self.email
