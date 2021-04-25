#  View do projeto antigo, caso queira usar em comparação
#from django.views.generic.list import ListView
#from photos.models import Photo
#from feedback.forms import FeedbackForm

#class PhotoView(ListView):
#    model = Photo
#    template_name = 'photos/photo_list.html'
#    paginate_by = 24

#    def get_context_data(self, **kwargs):
#        context = super(PhotoView, self).get_context_data(**kwargs)
#        context['form'] = FeedbackForm()
#        return context

from rest_framework import viewsets
from photos.models import Photo
from picha.serializers import PhotoSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
