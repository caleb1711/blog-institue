from django.urls import path
from .views import *

# Blog app Urls 
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("myblogs/", MyBlogsView.as_view(), name="myblogs"),
    path("blog_details/<int:id>/", BlogDetail.as_view(), name="blog_detail"),
    path("blog/<int:id>/", delete_blog, name="deleteblog"),
    path("addblog/", AddBlog.as_view(), name="addblog"),
    path("editblog/<int:id>/", EditBlog.as_view(), name="editblog"),
    path("privacy/", PrivacyView.as_view(), name="privacy"),
    path("about/", AboutUsView.as_view(), name="about"),

]