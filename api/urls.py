from django.urls import path


from api.views import ImageProcessingView


urlpatterns = [
    path('image/', ImageProcessingView.as_view(), name='image_process'),
]
