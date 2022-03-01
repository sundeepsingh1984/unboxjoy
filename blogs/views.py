from sre_parse import CATEGORIES
from unicodedata import category
from webbrowser import get
from django.shortcuts import render,get_object_or_404

from.models import Blog,BlogCatagory,BlogSubCategory
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.


def blogs_home_view(request):
    try:
        blogs_query_set=Blog.objects.order_by("-created_at").all()[:10]
    except Exception as e:
        raise Http404("OOPS Seems Basket Is Empty")


def blogs_categorical_view(request,cat_id):
    try:
        blg_qry_set=Blog.objects.order_by("-created_at").filter(blog_category = cat_id, public="True").all()
        paginator_obj=Paginator(blg_qry_set,6)
        page_number = request.GET.get('page')
    except Exception as e:
        return Http404("There was some Issue Finding blogs")

    try:
        page_obj = paginator_obj.get_page(page_number)  # returns the desired page object
        
    except  PageNotAnInteger:
    # if page_number is not an integer then assign the first page
        page_obj = paginator_obj.page(1)
        
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator_obj.page(paginator_obj.num_pages)
    
        # sending the page object to index.html


    categories=BlogCatagory.objects.all()

    sub_categories=BlogSubCategory.objects.filter(cat_id=cat_id).all

    trending_blogs=Blog.objects.filter(trending="True",public="True").all()[:3]

    latest_blogs=Blog.objects.order_by("-created_at").filter(public="True").all()[:3]
        
    return render(request, 'blog-view.html', {'page_obj': page_obj,"latest_blogs":latest_blogs,"trending_blogs":trending_blogs,"categories":categories,"tags":sub_categories})
  


#view to fetch blod details
def blog_detail_view(request,id):
    blog=get_object_or_404(Blog,blog_id=id)
    categories=BlogCatagory.objects.all()
    sub_categories=BlogSubCategory.objects.filter(cat_id=blog.blog_category.category_id).all
    trending_blogs=Blog.objects.filter(trending="True",public="True").all()[:3]
    latest_blogs=Blog.objects.order_by("-created_at").filter(public="True").all()[:3]
    return render(request, 'blog-detail-view.html', {'blog_details': blog,"latest_blogs":latest_blogs,"trending_blogs":trending_blogs,"categories":categories,"tags":sub_categories})
  


#view to fetch blogs based on sun category

def blogs_subcategorical_view(request,cat_id,sub_cat_id):
    try:
        blg_qry_set=Blog.objects.order_by("-created_at").filter(blog_category = cat_id, blog_sub_cat=sub_cat_id, public="True").all()
        paginator_obj=Paginator(blg_qry_set,6)
        page_number = request.GET.get('page')
    except Exception as e:
        return Http404("There was some Issue Finding blogs")

    try:
        page_obj = paginator_obj.get_page(page_number)  # returns the desired page object
        
    except  PageNotAnInteger:
    # if page_number is not an integer then assign the first page
        page_obj = paginator_obj.page(1)
        
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator_obj.page(paginator_obj.num_pages)
    
        # sending the page object to index.html


    categories=BlogCatagory.objects.all()

    sub_categories=BlogSubCategory.objects.filter(cat_id=cat_id).all

    trending_blogs=Blog.objects.filter(trending="True",public="True").all()[:3]

    latest_blogs=Blog.objects.order_by("-created_at").filter(public="True").all()[:3]
        
    return render(request, 'blog-view.html', {'page_obj': page_obj,"latest_blogs":latest_blogs,"trending_blogs":trending_blogs,"categories":categories,"tags":sub_categories})
  



    

