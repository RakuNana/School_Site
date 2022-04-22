from django.urls import path, reverse_lazy
from . import views

app_name="My_ads_app"

urlpatterns = [
    path('', views.AdsListView.as_view(), name='all'),
    path('ads/<int:pk>', views.AdsDetailView.as_view(), name='ad_detail'),
    path('ads/create',
        views.AdsCreateView.as_view(success_url=reverse_lazy('My_ads_app:all')), name='ad_create'),
    path('ads/<int:pk>/update',
        views.AdsUpdateView.as_view(success_url=reverse_lazy('My_ads_app:all')), name='ad_update'),
    path('ads/<int:pk>/delete',
        views.AdsDeleteView.as_view(success_url=reverse_lazy('My_ads_app:all')), name='ad_delete'),
    path('ads/<int:pk>/ads_pic',views.AdsPic, name='ads_pic'),
    path('ads/<int:pk>/comments/',views.CommentCreateView.as_view(), name='add_comment'),
    path('comment/<int:pk>/delete',
        views.CommentDeleteView.as_view(success_url=reverse_lazy('My_ads_app:all')), name='delete_comment'),
]