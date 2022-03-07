from sitesetting.shortcuts import get_banner_by_name
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import *
from django.core.paginator import Paginator
from.filters import ContentFilter

# Create your views here.


# view kids store page
def kids_store_view(request):

    #fetch categories
    
    try:
        category_query_set=StoreCatagory.objects.all()
    except Exception as e:
        raise Http404("Data error.please try again or contact to system admin")

    #fetch paginated affilated products

    try:
        product_query_set=AffilatedProducts.objects.order_by("-created_at").all()
        page_obj=Paginator(product_query_set,1)
        page_number=request.GET.get("page")


    except Exception as e:
        raise Http404("There is Some Error fetching products.Please Try again after a while")


    
    try:
        page_obj = page_obj.get_page(page_number)  # returns the desired page object
        
    except  PageNotAnInteger:
    # if page_number is not an integer then assign the first page
        page_obj = page_obj.page(1)
        
    except EmptyPage:
        # if page is empty then return last page
        page_obj = page_obj.page(page_obj.num_pages)
    
        
    # sending the page object to pages

    banner=get_banner_by_name("kidstore-banner")
    
    return render(request,"kids-store-view.html",{"products":page_obj,"categories":category_query_set,"page_count":page_obj.count ,"banner":banner})










# view kids store page(filtered)
def kids_store_refined_view(request):

    filter_value=request.POST.getlist('category')








        #fetch categories
    
    try:
        category_query_set=StoreCatagory.objects.all()
    except Exception as e:
        raise Http404("Data error.please try again or contact to system admin")

    #fetch paginated affilated products

    try:
        product_query_set=AffilatedProducts.objects.filter( product_cat__in =filter_value).order_by("-created_at").all()
        page_obj=Paginator(product_query_set,12)
        page_number=request.GET.get("page")


    except Exception as e:
        raise e
        raise Http404("There is Some Error fetching products.Please Try again after a while")


    
    try:
        page_obj = page_obj.get_page(page_number)  # returns the desired page object
        
    except  PageNotAnInteger:
    # if page_number is not an integer then assign the first page
        page_obj = page_obj.page(1)
        
    except EmptyPage:
        # if page is empty then return last page
        page_obj = page_obj.page(page_obj.num_pages)
    
        
    # sending the page object to pages
    
    return render(request,"kids-store-view.html",{"products":page_obj,"categories":category_query_set,"filter_by":list(map(int, filter_value)),"page_count":page_obj.count})




# kids content view
def kids_corner_content_view(request,category_id):

    try:
        #query set

        content_query_set=Content.objects.filter(content_type=category_id,published="True").all()
        latest_quote=Content.objects.filter(content_type__content_type_name="Quotes").order_by("-created_at").get()

        filtered_qs=ContentFilter(request.GET,content_query_set)
        page_obj=Paginator(filtered_qs.qs,1)
        page_number=request.GET.get("page")
    except Exception as e:
        raise e
        raise Http404("There is Some Error fetching products.Please Try again after a while")
    
    try:
        page_obj = page_obj.get_page(page_number)  # returns the desired page object
        
    except  PageNotAnInteger:
    # if page_number is not an integer then assign the first page
        page_obj = page_obj.page(1)
        
    except EmptyPage:
        # if page is empty then return last page
        page_obj = page_obj.page(page_obj.num_pages)

    banner=get_banner_by_name("kidcontent-banner")
    
        
    # sending the page object to pages
    return render(request,"content-view.html",{"content_list":page_obj,"filter_form":filtered_qs.form,"quote_of_day":latest_quote,"banner":banner})



#view to fetch the content details

def content_detail_view(request,content_id):
    # current content details
    content_obj=get_object_or_404(Content,content_id=content_id)

    #latest quote
    latest_quote=Content.objects.filter(content_type__content_type_name="Quotes").order_by("-created_at").get()




    
    #latest occasions articles
    
    latest_occasionals=Content.objects.filter(content_type__content_type_name="Occasions").order_by("-created_at").all()[:3]


    #catogories 
    categories=KidsContentType.objects.all()
    return render(request,"content-detail-view.html",{"categories":categories,"content":content_obj,"latest_occasionals":latest_occasionals,"quote_of_day":latest_quote})

