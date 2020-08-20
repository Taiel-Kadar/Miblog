from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
from django.core.mail import send_mail
from django.views.generic import ListView
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm, NewPostForm, EditPostForm, DeletePostForm
from taggit.models import Tag
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    context = {'page': page, 'posts': posts, 'tag': tag}
    return render(request, 'blog/post/list.html', context)


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug,
                             status='published',)

    # List of active comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                                  .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                .order_by('-same_tags','-publish')[:4]

    context = {'post': post, 'comments': comments,
               'new_comment': new_comment, 'comment_form': comment_form,
               'similar_posts': similar_posts}
    return render(request, 'blog/post/detail.html', context)


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


@login_required
def post_share(request, post_slug):
    # Retrieve post by slug
    post = get_object_or_404(Post, slug=post_slug, status='published')
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                      f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'admin@mysite.com', [cd['to']])
            sent = True
    
    else:
        form = EmailPostForm()

    context = {'post': post, 'form': form, 'sent': sent}
    return render(request, 'blog/post/share.html', context)


@login_required
def new_post(request):

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = NewPostForm()
    else:
        # POST data submitted; process data.
        form = NewPostForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.save()
            form.save_m2m()
            return redirect('blog:post_list')

    context = {'form': form}
    return render(request, 'blog/post/new_post.html', context)


@login_required
def edit_post(request, post_slug):
    """Edit an existing entry."""
    post = get_object_or_404(Post, slug=post_slug)

    form = EditPostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context = {'form': form}
    return render(request, 'blog/post/edit_post.html', context)


@login_required
def delete_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect("/")

    context = {'post': post}
    return render(request, 'blog/post/delete_post.html', context)
