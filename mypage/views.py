from django.shortcuts import render
#from django.shortcuts import render_to_response
#from django.http import HttpResponse


from .forms import PostForm


# Create your views here.
def page1(request):   
    if request.method == "POST" :
        form = PostForm(request.POST)
        
        if form.is_valid():
             obj = form.save()
             obj.blogpost=request.POST.get('blogpost')
             obj.save()
                  
             return render(request,'page2.html')
    else:
        form = PostForm()
        return render(request,'page1.html')
   # return render_to_response(request, 'page2.html', {})
    #return render( request,'page1.html')

