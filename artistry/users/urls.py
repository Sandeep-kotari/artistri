from django.contrib import admin
from django.urls import path
from users import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path("admin/", admin.site.urls),

    path("register/",views.register,name="register"),

    path("register/login/",views.user_login,name="register"),

    path("register/rig/",views.register,name="register"),

    path("login/rig/",views.register,name="register"),

    path("contact/",views.contact,name="contact"),

    path("login/",views.user_login,name="login/"),

    path("login/",views.user_login,name="login"),

    path("login/passwordreset/",views.passwordreset,name='resetp'),

    path("newpassword/<str:token>/",views.newpassword,name='reset'),

    path('create/', views.create_post, name='create_post'),

    path('view_post/',views.view_post,name='view_post'),

    path('signout/', views.signout, name='signout'),

    path('', views.index, name='homepage'),

    path('<int:pk>/', views.post_detail, name='post_detail'),

    path('user_home/', views.user_home, name='user_home'),

    path('user_home/toggle-like-post/<int:post_id>/', views.toggle_like_post, name='toggle_like_post'),

    path('view_post/toggle-like-post/<int:post_id>/', views.toggle_like_post, name='toggle_like_post'),

    path('view_post/contest', views.contest, name='contest'),

    path('user_home/view/<int:profile_id>/toggle-like-post/<int:post_id>/', views.pref_toggle_like_post, name='toggle_like_post'),

    path('user_home/view/<int:profile_id>/toggle-like-article/<int:article_id>/',views.ref_toggle_like_post,name='toggle_like_article'),

    path('user_home/srch/<str:srch_txt>/', views.searchfun, name='search'),

    path('help/', views.help1, name='help'),

    path('article',views.article1,name='article') ,

    path('view_article',views.view_article,name="view_arti"),

    path('view_article/toggle-like-article/<int:article_id>/',views.toggle_like_article,name='toggle_like_article'),

    path('view_post/toggle-like-article/<int:article_id>/',views.toggle_like_article,name='toggle_like_article'),

    path('user_home/search/', views.search, name='search'),

    path('user_home/view/<int:profile_id>/',views.searched_profile,name='viewprofile'),

    path('e_verify',views.e_verify,name='e_verify'),

    path('send_msg',views.send_msg,name="send_msg"),

    path('contest',views.contest,name="contest"),

    

   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
