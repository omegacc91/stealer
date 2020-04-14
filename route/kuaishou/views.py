# Create your views here.
from route import controller
from tools.type import Video


vtype = Video.KUAISHOU


def fetch(request):
    return controller.fetch(vtype, request)


def download(request):
    return controller.download(vtype, request)
