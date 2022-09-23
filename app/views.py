from django.shortcuts import render , HttpResponseRedirect , redirect
from app.models import post , likepost ,commnetpost
from django.views import View
from .forms import CustomerRegistrationForm
from django.core.paginator import Paginator
from django.contrib.auth import logout
from app.forms import CommnetForm
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        all_post = post.objects.all().order_by('id')
        all_likepost = likepost.objects.filter(user=request.user)
        paginator = Paginator(all_post,5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,'index.html',{'page_obj':page_obj ,'likepost':all_likepost})
    else:
        return HttpResponseRedirect('/login/')

def viewallpost(request,id):
    if request.user.is_authenticated:
        form = CommnetForm()
        getpost = post.objects.get(id=id)
        ispresent = likepost.objects.filter(user=request.user).filter(postname=getpost).exists() 
        allcommnet = None
        try:
            allcommnet = commnetpost.objects.filter(postname=getpost)
            print(allcommnet)
        except:
             pass
        return render(request,'post.html',{'onepost':getpost,'ispresent':ispresent,'fm':form ,'allcommnet':allcommnet})
    else:
        return HttpResponseRedirect('/login/')
def addlikepost(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            getpost = post.objects.get(id=id)
            f = likepost(user=request.user,postname=getpost)
            f.save()
            print("======================")
        return HttpResponseRedirect('/post/'+str(id))
    else:
        return HttpResponseRedirect('/login/')

class CustomerRegistrationView(View):
 def get(self, request):
  form = CustomerRegistrationForm()
  return render(request, 'customerregistration.html', {'form':form})
  
 def post(self, request):
    print("===============")
    form = CustomerRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/')


def logoutby(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def addcommnetinpost(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            print("*************************************")
            getonepost = post.objects.get(id=id)
            print(getonepost)
            print("===============")
            fm = CommnetForm(request.POST)
            print(fm)
            if fm.is_valid():
                comment = fm.cleaned_data['commnent']
                f = commnetpost(user=request.user,postname=getonepost,commnent=comment)
                f.save()
        return HttpResponseRedirect('/post/'+str(id))
    else:
        return HttpResponseRedirect('/login/')

def getlikepost(request,id):
    if request.user.is_authenticated:
        getlikepost = likepost.objects.get(id=id)
        getmainpost = post.objects.get(postname=getlikepost.postname.postname)
        print(getmainpost)
        return HttpResponseRedirect('/post/'+str(getmainpost.id))
    else:
        return HttpResponseRedirect('/login/')



     