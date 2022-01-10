from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import *

from hoodapp.forms import *

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    
    return render(request, 'index.html')

@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    neighborhood = NeighborHood.objects.all()
    businesses = Business.objects.filter(user_id=current_user.id)
    return render(request, "profile.html", {"profile": profile, ' neighborhood':  neighborhood, 'businesses':businesses })


@login_required(login_url='/accounts/login/')
def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile')
    return render(request, 'update_profile.html', {"form":form}) 


@login_required(login_url="/accounts/login/")
def create_hood(request):
    current_user = request.user
    if request.method == 'POST':
        hood_form = HoodForm(request.POST, request.FILES)
        if hood_form.is_valid():
            hood = hood_form.save(commit=False)
            hood.user = current_user
            hood.save()
        return HttpResponseRedirect('/hood')
    else:
        hood_form = HoodForm()
    context = {'hood_form':hood_form}
    return render(request, 'hood_form.html',context)

@login_required(login_url="/accounts/login/")
def hood(request):
    current_user = request.user
    hood = NeighborHood.objects.all().order_by('-id')
    return render(request, 'hoods.html', {'hood': hood})

@login_required(login_url='/accounts/login/')
def one_hood(request,name):
    hood = NeighborHood.objects.get(name=name)
    businesses = Business.objects.filter(neighborhood=hood)
    posts = Post.objects.filter(neighborhood=hood)

    return render(request,'one_hood.html',{'hood':hood, 'businesses':businesses, 'posts':posts}) 
    
def join_hood(request,id):
    neighborhood = get_object_or_404(NeighborHood, id=id)
    
    request.user.profile.neighborhood = neighborhood
    request.user.profile.save()
    return redirect('hood')

def leave_hood(request, id):
    hood = get_object_or_404(NeighborHood, id=id)
    request.user.profile.neighborhood = None
    request.user.profile.save()
    return redirect('hood')


@login_required(login_url="/accounts/login/")
def businesses(request):
    current_user = request.user
    businesses = Business.objects.all().order_by('-id')
    
    profile = Profile.objects.filter(user_id=current_user.id).first()

    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first()
        
        locations = Location.objects.all()
        neighborhood = NeighborHood.objects.all()
        
        businesses = Business.objects.all().order_by('-id')
        
        return render(request, "profile.html", {"danger": "Update Profile", "locations": locations, "neighborhood": neighborhood, "businesses": businesses})
    else:
        neighborhood = profile.neighborhood
        businesses = Business.objects.all().order_by('-id')
        return render(request, "businesses.html", {"businesses": businesses})

@login_required(login_url="/accounts/login/")
def new_business(request):
    current_user = request.user
    if request.method == "POST":
        
        form=BusinessForm(request.POST,request.FILES)

        if form.is_valid():
            business=form.save(commit=False)
            business.user=current_user
            business.hood= hood
            business.save()
        return HttpResponseRedirect('/businesses')
    else:
        form=BusinessForm()
    return render (request,'business_form.html', {'form': form, 'profile': profile})



# authorities
@login_required(login_url='/accounts/login/')
def authorities(request):
    current_user=request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
   
    authorities = Authorities.objects.all().order_by('-id')
    return render(request,'authorities.html',{"authorities":authorities, 'profile':profile})

# create_authorities
@login_required(login_url="/accounts/login/")
def create_authorities(request):
    current_user = request.user
    if request.method == "POST":
        
        form=AuthoritiesForm(request.POST,request.FILES)

        if form.is_valid():
            authority=form.save(commit=False)
            authority.user=current_user
            authority.hood= hood
            authority.save()
        return HttpResponseRedirect('/authorities')
    else:
        form=AuthoritiesForm()
    return render (request,'authorities_form.html', {'form': form, 'profile': profile})

# health
@login_required(login_url='/accounts/login/')
def health(request):
    current_user=request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
   
    health = Health.objects.all().order_by('-id')

    return render(request,'health.html',{"health":health,"profile":profile})




# blogpost
@login_required(login_url="/accounts/login/")
def create_post(request):
    current_user = request.user
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()

        return HttpResponseRedirect('/post')
    else:
        form = PostForm()
    return render(request, "create_post.html", {'form':form})

@login_required(login_url="/accounts/login/")
def post(request):
    current_user = request.user
    post = Post.objects.all().order_by('-id')
    return render(request, 'posts.html', {'posts': post})


# view_blog
@login_required(login_url='/accounts/login/')
def view_blog(request,id):
    current_user = request.user

    try:
        comments = Comment.objects.filter(post_id=id)
    except:
        comments =[]

    blog = Post.objects.get(id=id)
    if request.method =='POST':
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.username = current_user
            comment.post = blog
            comment.save()
    else:
        form = CommentForm()

    return render(request,'view_blog.html',{"blog":blog,"form":form,"comments":comments})

# new blogposts
@login_required(login_url='/accounts/login/')
def new_blogpost(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)

    if request.method=="POST":
        form =PostForm(request.POST,request.FILES)
        if form.is_valid():
            blogpost = form.save(commit = False)
            blogpost.username = current_user
            blogpost.neighborhood = profile.neighborhood
            blogpost.avatar = profile.avatar
            blogpost.save()

        return HttpResponseRedirect('/blog')

    else:
        form = PostForm()

    return render(request,'blogpost_form.html',{"form":form})


    # search
@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_post(search_term)
        message=f"{search_term}"

        print(searched_posts)

        return render(request,'search.html',{"message":message,"blogs":searched_posts})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})


# health
# @login_required(login_url='/accounts/login/')
# def health(request):
#     current_user=request.user
#     profile=Profile.objects.get(username=current_user)
#     healthservices = Health.objects.filter(neighborhood=profile.neighborhood)

#     return render(request,'health.html',{"healthservices":healthservices})


    

     