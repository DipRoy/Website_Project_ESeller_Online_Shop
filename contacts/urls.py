from django.urls import path
from contacts import views

app_name = 'contacts'

urlpatterns = [

    path("contact", views.contact, name='contact'),
    path("contact_admin_view", views.contact_admin_view, name='contact_admin_view'),
    path("send_reply_admin/<int:message_id>", views.send_reply_admin, name='send_reply_admin'),
    path("ignore_contact_admin/<int:message_id>", views.ignore_contact_admin, name='ignore_contact_admin'),
    path("sent_replies_admin",views.sent_replies_admin, name='sent_replies_admin')
]