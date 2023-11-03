from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
import threading 

# Send Email 
def send_email(subject, message, recipient_list, html_template=None, context=None, send_as_html=False):
    from_email = settings.DEFAULT_FROM_EMAIL
    if send_as_html:
        html_template = get_template(html_template)
        html_content = html_template.render(context)
        msg = EmailMultiAlternatives(subject, message, from_email, recipient_list)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    else:
        msg = send_mail(subject, message, from_email, recipient_list)


