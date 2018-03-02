from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import BlogPost, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import BlogPostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView, ListView,
                                CreateView, DetailView,
                                UpdateView, DeleteView)

# Create your views here.

# Blog Posts

class AboutView(TemplateView):
    template_name = 'about.html'

class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self):
        return BlogPost.objects.filter(creation_date__lte = timezone.now()).order_by('-creation_date')

class BlogPostDetailView(DetailView):
    model = BlogPost

class BlogPostCreateView(CreateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/blogpost_detail.html'
    form_class = BlogPostForm

    model = BlogPost

class BlogPostUpdateView(UpdateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/blogpost_detail.html'
    form_class = BlogPostForm

    model = BlogPost

class BlogPostDeleteView(DeleteView, LoginRequiredMixin):
    login_url ='/login/'
    #redirect_field_name = 'blog/blogpost_list.html'
    model = BlogPost
    success_url = reverse_lazy('blogpost_list')




# Comments



def add_comment_to_post(request,pk):
    blogpost = get_object_or_404(BlogPost,pk = pk)
    if (request.method == 'POST'):
        form = CommentForm(request.POST)
        if (form.is_valid):
            comment = form.save(commit = False)
            comment.blogpost = blogpost
            comment.save()
            return redirect('blogpost_detail', pk=blogpost.pk)
    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    blogpost_pk = comment.blogpost.pk
    comment.approval()
    return redirect('blogpost_detail', pk=comment.blogpost.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment,pk=pk)
    blogpost_pk = comment.blogpost.pk
    comment.delete()
    return redirect('blogpost_detail', pk=blogpost_pk)
