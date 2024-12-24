import os
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from contacts.models import Contact, SentReplies


def contact(request):
    """
    This method will display the contact page and in contact page there
    will be a form to contact with the admin. It will take data from the
    customer and will store those data in the database

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns contact page

    """
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        comment = request.POST.get("comment")

        if name != "":
            contact = Contact(name = name, email = email, phone = phone, comment = comment, date = datetime.today())
            contact.save()
            messages.success(request, 'Your response has been submitted successfully!!!')

    return render(request, 'contact/contact.html')


@login_required(login_url='/login')
def contact_admin_view(request):
    """
    This method will display the list of messages that customers has sent to
    admins. To view this list a user must have to login with admin account.

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns contact admin view page

    """
    if request.user.is_superuser:
      contact = Contact.objects.all().filter(is_replied=False).order_by('-date')
      params = {'contact': contact}
      return render(request, 'contacts/contact_admin_view.html', params)

    else:
        return render(request, 'html_view_with_error', {"error" : "PERMISSION DENIED"})


@login_required(login_url='/login')
def send_reply_admin(request, message_id):
    """
    This method will send replies to those customers who have contacted with admins
    through contract page of the  shop.  The reply will go to the customer's email
    only  if the  email address that  customer has provided is valid. A user must
    have to login with admin account to send reply to those customers.

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :param name: message_id - used to find the specific message of the customer
    :param type: HttpResponse
    :return: returns contact admin view page

    """
    if request.user.is_superuser :

        if request.method == 'POST':
            recipient = request.POST.get('recipient_name')
            subject = request.POST.get('email_subject')
            message = request.POST.get('message_text')

            send_mail(
                subject,
                message,
                'eseller.sunjare@gmail.com',
                [recipient],
                fail_silently=False
            )

            contact = Contact.objects.get(pk=message_id)
            contact.is_replied = True
            contact.save()

            SentReplies.objects.create(message_sender=contact)
            sent_replies_message_id = SentReplies.objects.get(message_sender__message_id=message_id)
            sent_replies_message_id.reply = message
            sent_replies_message_id.subject = subject
            sent_replies_message_id.save()

            messages.success(request, 'Message has been sent successfully!!!')
            return redirect("contact/contact_admin_view")

    else:
        return render(request, 'html_view_with_error', {"error" : "PERMISSION DENIED"})


# Admin Delete Email Through Contact
def ignore_contact_admin(request, message_id):
    """
    This method will ignore or delete contacts. If the admin wants to ignore any
    messages that customers have sent, he has to click on the ignore button and
    the message that the customer has sent will be deleted from the database

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :param name: message_id - used to find the specific message of the customer
    :param type: HttpResponse
    :return: returns contact admin view page

    """
    message = Contact.objects.get(pk=message_id)
    message.delete()
    return redirect("contact_admin")


# View Sent Replies
@login_required(login_url='/login')
def sent_replies_admin(request):
    """
    This  method will show replies that  admins have sent to the customer.  So, admin
    can view the messages that customers have sent them also they can see their replies
    through that page

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns sent replies page

    """
    if request.user.is_superuser :
        sent_replies = SentReplies.objects.all()
        params = {'sent_replies': sent_replies}
        return render(request,'contact/sent_replies.html',params)
