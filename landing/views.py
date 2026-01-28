from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def index(request):
    return render(request, 'landing/index.html')

def subscribe(request):
    if request.method == "POST":
        email = request.POST.get('email')
        
        try:
            subject = 'Welcome to FoodDistro!'
            html_content = render_to_string('landing/email_confirmation.html', {'email': email})
            text_content = strip_tags(html_content)
            
            msg = EmailMultiAlternatives(
                subject,
                text_content,
                settings.DEFAULT_FROM_EMAIL,
                [email]
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            
            message = f"Thank you! {email} has been subscribed."
        except Exception as e:
            print(f"Email sending failed: {e}")
            # Don't show the error to the user, just confirm subscription
            message = f"Thank you! {email} has been subscribed."

        return HttpResponse(f"""
            <div class="animate__animated animate__fadeIn">
                <p class="text-success"><i class="fas fa-check-circle"></i> {message}</p>
            </div>
        """)
    return HttpResponse("")

def delete_account(request):
    return render(request, 'landing/delete_account.html')
