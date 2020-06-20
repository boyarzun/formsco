from django import forms
from forms.models import Form


class Form(forms.ModelForm):
    class Meta:
        model = Form
        fields = ["from_name", "subject", "to", "cc", "bcc", "reply_to", "re_captcha"]
        widgets = {
            "from_name": forms.TextInput(attrs={"placeholder": "FormsCo"}),
            "subject": forms.TextInput(
                attrs={"placeholder": "Sending with Django is fun"}
            ),
            "to": forms.TextInput(attrs={"placeholder": "to@example.com"}),
            "cc": forms.TextInput(
                attrs={"placeholder": "cc-one@example.com, cc-two@example.com"}
            ),
            "bcc": forms.TextInput(
                attrs={"placeholder": "bcc-one@example.com, bcc-two@example.com"}
            ),
            "reply_to": forms.TextInput(attrs={"placeholder": "reply-to@example.com"}),
            "re_captcha": forms.TextInput(
                attrs={"placeholder": "9Lcbn6YZAAAAALP3D5rxv95CNHQKk-wey5D_LUNz"}
            ),
        }
        labels = {
            "re_captcha": "reCAPTCHA",
        }
