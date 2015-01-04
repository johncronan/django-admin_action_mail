from django.conf.urls import patterns, url, include

urlpatterns = patterns('admin_action_mail.views',
        url(r'^mail_form/$','mail_form',name='admin_action_mail-form'),
        )
