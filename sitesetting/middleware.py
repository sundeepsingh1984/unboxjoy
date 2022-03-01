from .shortcuts import get_blogs_category,get_site_info,get_games_menu,get_social,get_giveaway_type,get_kids_content_category
class InformationMiddleware:
    
    def __init__(self,get_response) :
        self.get_response=get_response


    def __call__(self,request):
        request.site_info=get_site_info(request)
        request.games_menu=get_games_menu(request)
        request.blog_menu=get_blogs_category(request)
        request.giveaway_menu=get_giveaway_type(request)
        request.social_links=get_social(request)
        request.kids_corner=get_kids_content_category(request)
        response = self.get_response(request)

        return response
       




    
        





