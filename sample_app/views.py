from django.http import HttpResponse
from django.views import generic
from .models import Location, WeatherData
from django.contrib.auth.mixins import LoginRequiredMixin
import io
import matplotlib.pyplot as pp



# def index(request):
#     context = {
#         'name' : 'iima',
#     }
#     return render(request, 'sample_app/index.html', context)

# def about(request):
#     """/about アバウトページ"""
#     return render(request, 'sample_app/about.html')

# def info(request):
#     """/info インフォページ"""
#     return render(request, 'sample_app/info.html')

class IndexView(LoginRequiredMixin, generic.ListView):
    model = Location
    paginate_by = 5
    ordering = ['-updated_at']
    template_name = 'sample_app/index.html'

class DetailView(generic.DetailView):
    model = Location
    template_name = 'sample_app/question.html'


def setPlt(pk):
    weather_data = WeatherData.objects.select_related('location').filter(location_id=pk)
    x = [data.data_datetime for data in weather_data]
    y1 = [data.temperature for data in weather_data] # 気温
    y2 = [data.humidity for data in weather_data]  # 湿度
    pp.plot(x, y1, x, y2)

def pltToSvg():
    buf = io.BytesIO()
    pp.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s

def get_svg(request, pk):
    setPlt(pk)
    svg = pltToSvg()  # convert plot to SVG
    pp.cla()  # clean up plt so it can be re-used
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response