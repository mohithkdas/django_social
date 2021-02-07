from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

post =[{
    'author':'Mohith',
    'title':'Blog Post 1',
    'content':'First Post Content',
    'date_posted': 'August 27, 2018'
},
{
    'author':'Mindas',
    'title':'Blog Post 2',
    'content':'Second Post Content',
    'date_posted': 'August 28, 2018'
}
]

def home(request):
    context = {
        'posts':post,
    }
    return render(request,'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html')


# def about(request):
#     return HttpResponse('<h1>About Us</h1>')
