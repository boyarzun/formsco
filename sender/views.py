# Rest Framework
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

# Django
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.conf import settings

# SendGrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, From, To, Subject, Cc, Bcc, ReplyTo

# Models
from forms.models import Form

# Utils
from sender.utils import get_form_content, get_current_host, re_captcha, get_emails


@api_view(["POST"])
@csrf_exempt
def send_email(request, pk):

    form = get_object_or_404(Form, pk=pk)

    re_captcha_is_valid = re_captcha(request, form.re_captcha)

    if not re_captcha_is_valid:
        return Response(status=status.HTTP_403_FORBIDDEN)

    reply_to = request.POST.get("_replyTo") or form.reply_to
    content = get_form_content(request.POST)

    message = Mail(
        from_email=From(settings.FROM_EMAIL, form.from_name),
        to_emails=To(form.to),
        subject=Subject(form.subject),
        html_content=content,
    )

    message.reply_to = ReplyTo(reply_to)

    if form.cc:
        message.cc = get_emails(form.cc)

    if form.bcc:
        message.bcc = get_emails(form.bcc)

    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
