from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import Facility, FacilityImage, FacilityVideo,Country,State,District,City,QuickService,Package,Article,Banner,EnquiryFormContent
from django.core.files.storage import FileSystemStorage
from rest_framework import viewsets
from .serializers import FacilitySerializer,EnquiryFormContentSerializer
import os








 

 
 # Create your views here.
def adminpannel(request):
    return render(request,'adminpannel.html')




from django.shortcuts import render, redirect, get_object_or_404
from .models import Country

def add_country(request):
    if request.method == 'POST':
        country_name = request.POST.get('name')
        if country_name:
            Country.objects.create(name=country_name)
            return redirect('list_country')

    return render(request, 'add_country.html')

def list_country(request):
    countries = Country.objects.all()
    return render(request, 'list_country.html', {'countries': countries})

def edit_country(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        if new_name:
            country.name = new_name
            country.save()
            return redirect('list_country')

    return render(request, 'edit_country.html', {'country': country})

def delete_country(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    country.delete()
    return redirect('list_country')






# ✅ Add State
def add_state(request):
    if request.method == 'POST':
        state_name = request.POST.get('name')
        if state_name:
            State.objects.create(name=state_name)
            return redirect('list_state')  # Redirect to State list
    return render(request, 'add_state.html')

# ✅ List States
def list_state(request):
    states = State.objects.all()
    return render(request, 'list_state.html', {'states': states})

# ✅ Edit State
def edit_state(request, state_id):
    state = get_object_or_404(State, id=state_id)
    if request.method == 'POST':
        state.name = request.POST.get('name')
        state.save()
        return redirect('list_state')  # Redirect after update
    return render(request, 'edit_state.html', {'state': state})

# ✅ Delete State
def delete_state(request, state_id):
    state = get_object_or_404(State, id=state_id)
    state.delete()
    return redirect('list_state')  # Redirect after delete






def list_district(request):
    districts = District.objects.all()  # Fetch all districts
    return render(request, 'list_district.html', {'districts': districts})

def add_district(request):
    if request.method == 'POST':
        name = request.POST['name']
        District.objects.create(name=name)
        return redirect('list_district')
    return render(request, 'add_district.html')

def edit_district(request, district_id):
    district = get_object_or_404(District, id=district_id)
    if request.method == 'POST':
        district.name = request.POST['name']
        district.save()
        return redirect('list_district')
    return render(request, 'edit_district.html', {'district': district})

def delete_district(request, district_id):
    district = get_object_or_404(District, id=district_id)
    district.delete()
    return redirect('list_district')






def add_city(request):
    if request.method == 'POST':
        city_name = request.POST.get('name')
        if city_name:
            City.objects.create(name=city_name)
            return redirect('list_city')  # Redirect after adding a city

    return render(request, 'add_city.html')

def list_city(request):
    cities = City.objects.all()
    return render(request, 'list_city.html', {'cities': cities})





def list_city(request):
    cities = City.objects.all()
    return render(request, 'list_city.html', {'cities': cities})


def add_city(request):
    if request.method == 'POST':
        city_name = request.POST.get('name')
        if city_name:
            City.objects.create(name=city_name)
            return redirect('list_city')

    return render(request, 'add_city.html')


def edit_city(request, city_id):
    city = get_object_or_404(City, id=city_id)

    if request.method == 'POST':
        city.name = request.POST.get('name')
        city.save()
        return redirect('list_city')

    return render(request, 'edit_city.html', {'city': city})


def delete_city(request, city_id):
    city = get_object_or_404(City, id=city_id)
    city.delete()
    return redirect('list_city')











def create_facility(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        country_id = request.POST.get('country')
        state_id = request.POST.get('state')
        district_id = request.POST.get('district')
        city_id = request.POST.get('city')
        description = request.POST.get('description')
        
        # Handle multiple images
        images = request.FILES.getlist('images[]')  # Note the [] in the name
        
        # Handle multiple video links
        videos = request.POST.getlist('videos')  # This will get all values with name 'videos'

        facility = Facility.objects.create(
            name=name,
            country_id=country_id,
            state_id=state_id,
            district_id=district_id,
            city_id=city_id,
            description=description
        )

        # Process images (max 10)
        for image in images[:10]:
            FacilityImage.objects.create(facility=facility, image=image)

        # Process videos (max 10)
        for video in videos[:10]:
            if video.strip():  # Only add non-empty video URLs
                FacilityVideo.objects.create(facility=facility, video_link=video)

        return JsonResponse({'status': 'success', 'message': 'Facility created successfully'})

    countries = Country.objects.all()
    states = State.objects.all()
    districts = District.objects.all()
    cities = City.objects.all()

    return render(request, 'create_facility.html', {
        'countries': countries,
        'states': states,
        'districts': districts,
        'cities': cities
    })


def list_facilities(request):
    facilities = Facility.objects.all().prefetch_related('images', 'videos')
    return render(request, 'list_facilities.html', {'facilities': facilities})






def edit_facility(request, facility_id):
    facility = get_object_or_404(Facility, id=facility_id)

    if request.method == 'POST':
        facility.name = request.POST.get('name')
        facility.country_id = request.POST.get('country')
        facility.state_id = request.POST.get('state')
        facility.district_id = request.POST.get('district')
        facility.city_id = request.POST.get('city')
        facility.description = request.POST.get('description')
        facility.save()

        # Handle image updates (delete old and add new ones if provided)
        new_images = request.FILES.getlist('images[]')
        if new_images:
            FacilityImage.objects.filter(facility=facility).delete()
            for image in new_images[:10]:  # Max 10 images
                FacilityImage.objects.create(facility=facility, image=image)

        # Handle video updates (delete old and add new ones if provided)
        new_videos = request.POST.getlist('videos')
        if new_videos:
            FacilityVideo.objects.filter(facility=facility).delete()
            for video in new_videos[:10]:  # Max 10 videos
                if video.strip():
                    FacilityVideo.objects.create(facility=facility, video_link=video)

        return JsonResponse({'status': 'success', 'message': 'Facility updated successfully'})

    countries = Country.objects.all()
    states = State.objects.all()
    districts = District.objects.all()
    cities = City.objects.all()
    images = FacilityImage.objects.filter(facility=facility)
    videos = FacilityVideo.objects.filter(facility=facility)

    return render(request, 'edit_facility.html', {
        'facility': facility,
        'countries': countries,
        'states': states,
        'districts': districts,
        'cities': cities,
        'images': images,
        'videos': videos
    })



def delete_facility(request, facility_id):
    facility = get_object_or_404(Facility, id=facility_id)

    if request.method == "POST":
        facility.delete()
        return JsonResponse({'status': 'success', 'message': 'Facility deleted successfully'})

    return render(request, 'delete_facility.html', {'facility': facility})







def list_quick_services(request):
    """List all Quick Services"""
    services = QuickService.objects.all()
    return render(request, 'quickservicelist.html', {'services': services})

def add_quick_service(request):
    """Add a new Quick Service with Image"""
    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')

        if name:
            QuickService.objects.create(name=name, image=image)
            return redirect('list_quick_services')

    return render(request, 'quickserviceadd.html')


def edit_quick_service(request, service_id):
    """Edit an existing Quick Service"""
    service = get_object_or_404(QuickService, id=service_id)

    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')

        if name:
            service.name = name
            if image:  # Update image only if a new one is uploaded
                service.image = image
            service.save()
            return redirect('list_quick_services')

    return render(request, 'quickserviceedit.html', {'service': service})


def delete_quick_service(request, service_id):
    """Delete an existing Quick Service"""
    service = get_object_or_404(QuickService, id=service_id)

    if service.image:
        service.image.delete()  # Delete the image file when deleting the service

    service.delete()
    return redirect('list_quick_services')






# List Packages
def package_list(request):
    packages = Package.objects.all()
    return render(request, 'package_list.html', {'packages': packages})

# Add Package
def add_package(request):
    if request.method == 'POST':
        name = request.POST['name']
        details = request.POST['details']
        price = request.POST['price']
        Package.objects.create(name=name, details=details, price=price)
        return redirect('package_list')
    return render(request, 'add_package.html')

# Edit Package
def edit_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    if request.method == 'POST':
        package.name = request.POST['name']
        package.details = request.POST['details']
        package.price = request.POST['price']
        package.save()
        return redirect('package_list')
    return render(request, 'edit_package.html', {'package': package})

# Delete Package
def delete_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    package.delete()
    return redirect('package_list')





   

# List Articles
def list_articles(request):
    articles = Article.objects.all()
    return render(request, 'list_articles.html', {'articles': articles})

# Add Article
def add_article(request):
    if request.method == "POST":
        article_name = request.POST.get('article_name')
        article_description = request.POST.get('article_description')
        article_image = request.FILES.get('article_image')

        if article_name and article_image and article_description:
            Article.objects.create(
                article_name=article_name,
                article_image=article_image,
                article_description=article_description
            )
            return redirect('list_articles')

    return render(request, 'add_article.html')

# Edit Article
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    if request.method == "POST":
        article.article_name = request.POST.get('article_name')
        article.article_description = request.POST.get('article_description')
        if 'article_image' in request.FILES:
            article.article_image = request.FILES['article_image']
        article.save()
        return redirect('list_articles')

    return render(request, 'edit_article.html', {'article': article})

# Delete Article
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('list_articles')



# List all banners
def banner_list(request):
    banners = Banner.objects.all()
    return render(request, 'banner_list.html', {'banners': banners})

# Add a new banner
def add_banner(request):
    if request.method == "POST" and request.FILES.get('image'):
        image = request.FILES['image']
        Banner.objects.create(image=image)
        return redirect('banner_list')
    return render(request, 'add_banner.html')

# Edit a banner
def edit_banner(request, banner_id):
    banner = get_object_or_404(Banner, id=banner_id)
    
    if request.method == "POST" and request.FILES.get('image'):
        # Delete old image
        if banner.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, str(banner.image)))

        banner.image = request.FILES['image']
        banner.save()
        return redirect('banner_list')

    return render(request, 'edit_banner.html', {'banner': banner})

# Delete a banner
def delete_banner(request, banner_id):
    banner = get_object_or_404(Banner, id=banner_id)
    if banner.image:
        os.remove(os.path.join(settings.MEDIA_ROOT, str(banner.image)))
    banner.delete()
    return redirect('banner_list')




def facility_enquiries_report(request):
    facility_enquiries = EnquiryFormContent.objects.filter(facility__isnull=False)
    return render(request, 'facility_enquiries_report.html', {'facility_enquiries': facility_enquiries})

def quick_service_enquiries_report(request):
    quick_service_enquiries = EnquiryFormContent.objects.filter(quick_service__isnull=False)
    return render(request, 'quick_service_enquiries_report.html', {'quick_service_enquiries': quick_service_enquiries})

def package_enquiries_report(request):
    package_enquiries = EnquiryFormContent.objects.filter(package__isnull=False)
    return render(request, 'package_enquiries_report.html', {'package_enquiries': package_enquiries})



def enquiry_form(request):
    countries = Country.objects.all()
    states = State.objects.all()
    districts = District.objects.all()
    cities = City.objects.all()
    quick_services = QuickService.objects.all()
    facilities = Facility.objects.all()
    packages = Package.objects.all()
    
    context = {
        'countries': countries,
        'states': states,
        'districts': districts,
        'cities': cities,
        'quick_services': quick_services,
        'facilities': facilities,
        'packages': packages,
    }
    return render(request, 'enquiry_form.html', context)

def submit_enquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        country_id = request.POST.get('country')
        state_id = request.POST.get('state')
        district_id = request.POST.get('district')
        city_id = request.POST.get('city')
        quick_service_id = request.POST.get('quick_service')
        facility_id = request.POST.get('facility')
        package_id = request.POST.get('package')
        
        enquiry = EnquiryFormContent(
            name=name,
            email=email,
            mobile_number=mobile_number,
            country_id=country_id,
            state_id=state_id,
            district_id=district_id,
            city_id=city_id,
            quick_service_id=quick_service_id,
            facility_id=facility_id,
            package_id=package_id,
        )
        enquiry.save()
        
        return HttpResponse("Enquiry submitted successfully!")
    else:
        return HttpResponse("Invalid request", status=400)



















from rest_framework import viewsets
from .models import Country, State, District, City, Facility, QuickService, Package, Article,Banner
from .serializers import (
    CountrySerializer, StateSerializer, DistrictSerializer, CitySerializer,
    FacilitySerializer, QuickServiceSerializer, PackageSerializer, ArticleSerializer,BannerSerializer
)




class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

class QuickServiceViewSet(viewsets.ModelViewSet):
    queryset = QuickService.objects.all()
    serializer_class = QuickServiceSerializer

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer




class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer




class EnquiryFormContentViewSet(viewsets.ModelViewSet):
    queryset = EnquiryFormContent.objects.all()
    serializer_class = EnquiryFormContentSerializer



# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView

# class ProtectedDataView(APIView):
#     permission_classes = [IsAuthenticated]  # Require authentication

#     def get(self, request):
#         return Response({"message": "This is protected data"})




from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ProtectedDataView(APIView):
    permission_classes = [IsAuthenticated]  # This enforces authentication

    def get(self, request):
        return Response({"message": "This is protected data"})



