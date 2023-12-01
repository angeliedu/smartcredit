from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views

urlpatterns = [
		path('index/', views.index, name ='index'),
        path('', views.checkout_view, name='checkout'),
        path('creditForm/',views.creditForm_page,name='creditForm'),
        path('Dashboard/',views.Dashboard_page,name='Dashboard'),

        
        #Dashboard
        path('profile/',views.profile,name='profile'),
        path('helpCenter/',views.helpCenter,name='helpCenter'),
        path('Setting/',views.Setting,name='Setting'),
        path('Transation/',views.Transation,name='Transation'),
        path('wallet/',views.wallet,name='wallet'),
        # for going Back and forth on Dashboard page
        path('Dashboard/profile.html',views.profile,name='profile'),
        path('Dashboard/setting.html', views.Setting, name='Setting'),
        path('Dashboard/help-center.html', views.helpCenter, name='helpCenter'),
        path('Dashboard/dashboard.html',views.Dashboard_page,name='Dashboard'),
        path('Dashboard/Transation_detail.html', views.Transation, name='Transation'),
        path('Dashboard/wallet.html', views.wallet, name='wallet'),
        path('Dashboard/login.html',views.Login, name ='login'),
        # for going Back and forth on profile page
        path('profile/profile.html',views.profile,name='profile'),
        path('profile/setting.html', views.Setting, name='Setting'),
        path('profile/help-center.html', views.helpCenter, name='helpCenter'),
        path('profile/dashboard.html',views.Dashboard_page,name='Dashboard'),
        path('profile/Transation_detail.html', views.Transation, name='Transation'),
        path('profile/wallet.html', views.wallet, name='wallet'),
        path('profile/login.html',views.Login, name ='login'),
        # for going back and forth setting page
        path('Setting/profile.html',views.profile,name='profile'),
        path('Setting/setting.html', views.Setting, name='Setting'),
        path('Setting/help-center.html', views.helpCenter, name='helpCenter'),
        path('Setting/dashboard.html',views.Dashboard_page,name='Dashboard'),
        path('Setting/Transation_detail.html', views.Transation, name='Transation'),
        path('Setting/wallet.html', views.wallet, name='wallet'),
        path('Setting/login.html',views.Login, name ='login'),
        # for going back and forth Transation page
        path('Transation/profile.html',views.profile,name='profile'),
        path('Transation/setting.html', views.Setting, name='Setting'),
        path('Transation/help-center.html', views.helpCenter, name='helpCenter'),
        path('Transation/dashboard.html',views.Dashboard_page,name='Dashboard'),
        path('Transation/Transation_detail.html', views.Transation, name='Transation'),
        path('Transation/wallet.html', views.wallet, name='wallet'),
        path('Transation/login.html',views.Login, name ='login'),
        #for going back and forth wallet page
        path('wallet/profile.html',views.profile,name='profile'),
        path('wallet/setting.html', views.Setting, name='Setting'),
        path('wallet/help-center.html', views.helpCenter, name='helpCenter'),
        path('wallet/dashboard.html',views.Dashboard_page,name='Dashboard'),
        path('wallet/Transation_detail.html', views.Transation, name='Transation'),
        path('wallet/wallet.html', views.wallet, name='wallet'),
        path('wallet/login.html',views.Login, name ='login'),
        #for going back and forth Help Center page
        path('helpCenter/profile.html',views.profile,name='profile'),
        path('helpCenter/setting.html', views.Setting, name='Setting'),
        path('helpCenter/help-center.html', views.helpCenter, name='helpCenter'),
        path('helpCenter/dashboard.html',views.Dashboard_page,name='Dashboard'),
        path('helpCenter/Transation_detail.html', views.Transation, name='Transation'),
        path('helpCenter/wallet.html', views.wallet, name='wallet'),
        path('helpCenter/login.html',views.Login, name ='login'),
]
