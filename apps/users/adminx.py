import xadmin
from .models import BannerInfo, EmailVerifyCode


class BannerInfoXadmin(object):
    list_display = ['image', 'url', 'add_time']
    search_fields = ['image', 'url']
    list_filter = ['image', 'url']



class EmailVerifyCodeXadmin(object):
    list_display = ['code', 'email', 'send_type', 'add_time']
    # search_fields = ['code', 'email']
    # list_filter = ['email']


xadmin.site.register(BannerInfo, BannerInfoXadmin)
xadmin.site.register(EmailVerifyCode, EmailVerifyCodeXadmin)