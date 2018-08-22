from django.shortcuts import render
from website.models import SiteForm,Site
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
import datetime
from django.utils import timezone
# Create your views here.
def index(request):
    pages=getNewestPages(request)
    if request.method=="POST":
        form=SiteForm(request.POST)
        if form.is_valid():
            try:
                ispriv=request.POST['isPrivate']
            except:
                ispriv=False
            try:
                usesBs=request.POST['usesBootstrap']
            except:
                usesBs=False
            try:
                usesJq=request.POST['usesJquery']
            except:
                usesJq=False
            if request.POST['endingDate']=='':
                endingDate=datetime.datetime.now()+datetime.timedelta(days=2)
            else:
                endingDate=datetime.datetime.now()+datetime.timedelta(days=int(request.POST['endingDate']))
            site=Site(js=request.POST['js'],css=request.POST['css'],html=request.POST['html'],name=request.POST['name'], usesBootstrap=usesBs ,usesJquery=usesJq,endingDate=endingDate,isPrivate=ispriv)
            site.makeHash()
            site.viewsCount=0
            site.save()
            return HttpResponseRedirect("/view/"+site.hash)
    else:
        form=SiteForm()
    return render(request,'website/index.html',{'form': form, 'pages': pages})
def getNewestPages(request,mini=0,maxi=10,ignorePrivate=False):
    if ignorePrivate:
        objs=Site.objects.all("pk")[mini:maxi]
    else:
        objs=Site.objects.filter(isPrivate=False).order_by("-pk")[mini:maxi]
    return objs
def viewSite(request, hash):
    def splitAndAdd(input,string,i=0):
        x=input.split(string)
        x[i] += string
        return x
    site = get_object_or_404(Site, hash=str(hash))
    print(site.endingDate)
    print(datetime.datetime.now())
    if site.endingDate < timezone.now():
        return HttpResponse('<meta http-equiv="refresh" content="2; url=../../" />The webpage has expired, redirect in 2s')
    if '<html>' not in site.html and '</html>' not in site.html:
        site.html = "<!DOCTYPE html>\n<html>"+site.html+"\n</html>"
    skeleton=splitAndAdd(site.html,"<html>")
    skeleton[0].replace('<head>','')
    skeleton[0]+='\n<head>'
    if site.usesJquery:
        skeleton[0]+='\n<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>\n'
    if site.usesBootstrap:
        skeleton[0]+='\n<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">\n<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>'
    skeleton[0]+="\n<style>\n{0}\n</style>\n".format(site.css)
    skeleton[0]+="\n<script>\n{0}\n</script>\n".format(site.js)
    output=''.join(skeleton)
    return HttpResponse(output)