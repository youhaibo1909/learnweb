
from django.http import HttpResponse

def index(request):
    print(request.POST)
    print(request.GET)
    print(request.FILES)
    for item in request.FILES:
        fileObj = request.FILES.get(item)
        f = open(fileObj.name, 'wb')
        iter_file = fileObj.chunks()
        for line in iter_file:
            f.write(line)
        f.close()
    return HttpResponse('ok')