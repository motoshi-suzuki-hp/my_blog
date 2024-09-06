from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm  # 後で作成

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('../../', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

def post_delete(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

