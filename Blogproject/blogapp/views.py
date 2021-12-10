from django.shortcuts import render,get_object_or_404
from blogapp.models import Post,Comments
from blogapp.forms import CommentForm
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from taggit.models import Tag

# Create your views here.
def post_list_view(request,tag_slug=None):
   post_list=Post.objects.all()
   tag=None
   if tag_slug:
       tag=get_object_or_404(Tag,slug=tag_slug)
       post_list=post_list.filter(tags__in=[tag])

   paginator= Paginator(post_list,3)
   page_number=request.GET.get('page')
   try:
       post_list=paginator.page(page_number)
   except PageNotAnInteger:
       post_list=paginator.page(1)
   except EmptyPage:
       post_list=paginator.page(paginator.num_pages)


   return render(request,'blogapp/post_list.html',{'post_list':post_list,'tag':tag})

def post_detail_view(request,slug):
    post=get_object_or_404(Post,slug=slug)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True

    else:
        form=CommentForm()

    return render(request,'blogapp/post_detail.html',{'post':post,'form':form,'comments':comments,'csubmit':csubmit})

from django.core.mail import send_mail
from blogapp.forms import EmailSendForm

def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id)
    sent=False
    if request.method=='POST':
        form=EmailSendForm(request.POST)
        if form.isvalid():
            cd=form.cleaned_data
            send_mail('subject','message','sowju4h@gmail.com',[cd['to']])
            sent=True

    else:
        form=EmailSendForm()
    return render(request,'blogapp/share_email.html',{'form':form,'post':post})
