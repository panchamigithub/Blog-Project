from django.shortcuts import render
#from .forms import Reg
from .models import register,blog


# Create your views here.
'''

def registration(request):
    if request.method == "POST":
        form = Reg(request.POST)

        if form.is_valid():
             obj = form.save()
             obj.username=request.POST.get('usr')
             obj.name=request.POST.get('name')
             obj.email=request.POST.get('email')
             obj.mobile=request.POST.get('mob')
             obj.password=request.POST.get('pwd')
             obj.city=request.POST.get('city')
             obj.save()
             return render(request,'login.html')
        else:
             return render(request,'register.html')
    else:
        form = Reg()
        return render(request,'register.html')

'''
def registration(request):
    if request.method == "POST":
      if(request.POST.get('usr') and request.POST.get('name') and request.POST.get('email') and request.POST.get('mob') and request.POST.get('pwd') and request.POST.get('city')):
        obj = register()
        obj.username=request.POST.get('usr')
        obj.name=request.POST.get('name')
        obj.email=request.POST.get('email')
        obj.mobile=request.POST.get('mob')
        obj.password=request.POST.get('pwd')
        obj.city=request.POST.get('city')
        obj.ans=request.POST.get('color')
        obj.save()
        return render(request,'success.html')
      else:
        return render(request,'register.html')
    else:
        return render(request,'register.html')


def login(request):
    username = 'not logged in'
    if request.method == "POST":
        if (request.POST.get('usr') and request.POST.get('pwd')):
            u=request.POST.get('usr')
            p=request.POST.get('pwd')
            #print(u+p)
            try:
               obj=register.objects.get(username=u, password=p)
               if(obj):
                  request.session['username'] = u
                  request.session['name']=obj.name
                  return render(request,'home.html')

            except register.DoesNotExist:
                return render(request, 'login.html')

        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return render(request,"login.html")

def blogpost(request):
  if ('username' in request.session):
    if request.method=='POST':
       if(request.POST.get('blog')):
           obj2 = blog()
           obj2.blogp=request.POST.get('blog')
           name=request.session['name']
           usr=request.session['username']
           obj2.author=name
           obj2.username=usr
           obj2.save()
           return render(request,'home.html')
       else:
           return render(request,'errorr.html')
    else:
       return render(request,'blog.html')
  else:
      return render(request, 'login.html')

def index(request):
    return render(request,'index.html')

def viewblog(request):

    if('username' in request.session):
        uname = request.session['username']
        data=blog.objects.filter(username=uname)
        return render(request,'viewblog.html',{'data':data,})
    else:
        return render(request,'login.html')

def security_question(request):
     if request.method=='POST':
         uname = request.POST.get('usr')
         data = register.objects.get(username=uname)
         answer=request.POST.get('color')
         if(data.ans==answer):
             return render(request,'change_password.html',{'data':uname})
         else:
             return render(request,'login.html')
     else:
         return render(request, 'forgot.html')

def Password_change(request):
    if request.method=='POST':
        usr = request.POST.get('usr')
        new_pwd=request.POST.get('pwd')

        try:
            obj=register.objects.get(username=usr)
            obj.password=new_pwd
            obj.save()
            return render(register, 'login.html')

        except register.DoesNotExist:
            return render(request, 'change_password.html')

        ''' 
        usr = request.POST.get('usr')
        
     register.objects.filter(username='panchu123').update(password=new_pwd)

        return render(register,'login.html')
    else:
      return render(request, 'change_password.html')
        '''