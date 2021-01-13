from django.http import HttpResponse
class SimpleMiddleware:
      def __init__(self,get_response):
          self.get_response=get_response
      def __call__(self,request):
        print("Preprocessing the request")
        response=self.get_response(request)
        print(response)    
        print("Postprocessing the request")
        return response
      def process_exception(self,request,exception):
          return HttpResponse("Pls wait...Server is under maintainace ")
        
        
        