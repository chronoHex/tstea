from django.shortcuts import render
from .models import Post, Comment, Blogger
from .forms import NewPostForm, ProfileEditForm, EditProfileForm
from django.utils.timezone import now as curr_time
from django.views import generic
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    """View fxn for the home page of this site."""

    # Generate some counts for the main objects
    num_posts = Post.objects.all().count()

    context = {
        'num_posts': num_posts,
    }

    return render(request, 'index.html', context=context)


class PostListView(generic.ListView):
    model = Post


class PostDetailView(generic.DetailView):
    model = Post


class BloggerDetailView(generic.DetailView):
    model = Blogger

class CommentDetailView(generic.DetailView):
    model = Comment

if 1==0:
    pass

def new_post(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.blogger = request.user.blogger
            post.published_date = curr_time()
            post.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = NewPostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = NewPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.blogger = request.user
            post.published_date = curr_time()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = NewPostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

