from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from django.db.models import Q
from django.http import HttpResponseRedirect

# Create your views here.
def age_conf(request):
    if request.method == 'POST':
        if 'yes' in request.POST:
            request.session['age_confirm'] = True
            return redirect('app:post_tab')
        elif 'no' in request.POST:
            previous_page = request.META.get('HTTP_REFERER', '/')
            return HttpResponseRedirect(previous_page)
    return render(request, 'app/age_conf.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app/post_list.html',{'posts':posts})

def post_tab(request):
    if not request.session.get('age_confirm'):
        return redirect('app:age_conf')
    else:
        tab = request.GET.get('tab', 'tab1')
        posts = Post.objects.all().order_by('published_date')
        working_images = Post.objects.filter(
            Q(image__isnull=False) & Q(status=Post.WORKING_ROOM)
            )
        sleeping_images = Post.objects.filter(
            Q(image__isnull=False) & Q(status=Post.SLEEPING_ROOM)
            )
        context = {
            'posts':posts,
            'working_images':working_images,
            'sleeping_images':sleeping_images
        }
    return render(request, 'app/post_tab.html', context)

def post_detail(request, blog_id):
    post_detail = get_object_or_404(Post, id = blog_id)
    return render(request, 'app/detail.html', {'post_detail':post_detail})
