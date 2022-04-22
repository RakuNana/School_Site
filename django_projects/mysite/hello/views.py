from django.shortcuts import HttpResponse

# Create your views here.


def hello_view(request):

    print(request.COOKIES)
    oldvalue = request.COOKIES.get("count_cookie", 1)
    resp = HttpResponse("view count="+str(oldvalue))

    if oldvalue:
        resp.set_cookie("count_cookie", int(oldvalue) + 1)
    else:
        resp.set_cookie("count_cookie", 1)

    resp.set_cookie("cookie", 0 , max_age=1000)

    resp.set_cookie("dj4e_cookie", "79aadfd3")

    return resp



'''def cookie(request):

    print(request.COOKIES)

    oldval = request.COOKIES.get('zap', None)

    resp = HttpResponse('In a view - the zap cookie value is '+str(oldval))

    if oldval :

        resp.set_cookie('zap', int(oldval)+1) # No expired date = until browser close

    else :

        resp.set_cookie('zap', 42) # No expired date = until browser close

    resp.set_cookie('sakaicar', 42, max_age=1000) # seconds until expire

    return resp

'''