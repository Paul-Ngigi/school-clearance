from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


EMAIL_HOST_USER = settings.EMAIL_HOST_USER

def send_mails(request, template_name, subject, recipient_list, context):
    # Render the HTML content using the template
    html_content = render_to_string(template_name, context)

    # Create an EmailMultiAlternatives object
    email = EmailMultiAlternatives(
        subject=subject,
        body=strip_tags(html_content),  # Plain text version for email clients that don't support HTML
        from_email=EMAIL_HOST_USER,
        to=recipient_list,
    )

    # Attach the HTML content
    email.attach_alternative(html_content, "text/html")

    # Send the email
    email.send()    
