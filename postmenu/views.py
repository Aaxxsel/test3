from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        title = request.POST.get('title')
        text = request.POST.get('text')
        if form.is_valid():
            try:
                Post.objects.create(title=title, text=text)
                return redirect('list_post')

            except:
                form.add_error(None, "Ошибка")
    else:
        form = PostForm()
    return render(request, 'postmenu/mainpage.html', {'form': form})


def listpost(request):
    posts = Post.objects.all()
    return render(request, 'postmenu/listpost.html', {'posts': posts})

