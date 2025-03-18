from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter
from .views import (
    CountryViewSet, StateViewSet, DistrictViewSet, CityViewSet,
    FacilityViewSet, QuickServiceViewSet, PackageViewSet, ArticleViewSet,BannerViewSet,EnquiryFormContentViewSet,ProtectedDataView
    
)


 



router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'states', StateViewSet)
router.register(r'districts', DistrictViewSet)
router.register(r'cities', CityViewSet)
router.register(r'facilities', FacilityViewSet)
router.register(r'quickservices', QuickServiceViewSet)
router.register(r'packages', PackageViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'banners', BannerViewSet, basename='banner')
router.register(r'enquiryformcontent', EnquiryFormContentViewSet)






 
urlpatterns=[
    
    path('adminpannel/',views.adminpannel,name='adminpannel'),
    path('list_country/', views.list_country, name='list_country'),
    path('add-country/', views.add_country, name='add_country'),
    path('edit-country/<int:country_id>/', views.edit_country, name='edit_country'),  
    path('delete-country/<int:country_id>/', views.delete_country, name='delete_country'),
    path('add-state/', views.add_state, name='add_state'),
    path('list-state/', views.list_state, name='list_state'),
    path('edit-state/<int:state_id>/', views.edit_state, name='edit_state'),
    path('delete-state/<int:state_id>/', views.delete_state, name='delete_state'),path('add-district/', views.add_district, name='add_district'),
    path('list-district/', views.list_district, name='list_district'),
    path('edit-district/<int:district_id>/', views.edit_district, name='edit_district'),
    path('delete-district/<int:district_id>/', views.delete_district, name='delete_district'),
    path('list-city/', views.list_city, name='list_city'),  
    path('add-city/', views.add_city, name='add_city'),
    path('edit-city/<int:city_id>/', views.edit_city, name='edit_city'),
    path('delete-city/<int:city_id>/', views.delete_city, name='delete_city'),

    
    path('create-facility/',views.create_facility, name='create_facility'),
    path('facilities/',views.list_facilities, name='list_facilities'),
    
    

    path('quickservice/',views.list_quick_services, name='list_quick_services'),
    path('quickservice/add/',views.add_quick_service, name='add_quick_service'),
    path('quickservice/edit/<int:service_id>/',views. edit_quick_service, name='edit_quick_service'),
    path('quickservice/delete/<int:service_id>/',views. delete_quick_service, name='delete_quick_service'),




    path('packages/',views.package_list, name='package_list'),
    path('packages/add/',views.add_package, name='add_package'),
    path('packages/edit/<int:package_id>/',views.edit_package, name='edit_package'),
    path('packages/delete/<int:package_id>/',views.delete_package, name='delete_package'),


    path('articles/', views.list_articles, name='list_articles'),
    path('articles/add/', views.add_article, name='add_article'),
    path('articles/edit/<int:article_id>/', views.edit_article, name='edit_article'),
    path('articles/delete/<int:article_id>/', views.delete_article, name='delete_article'),



    path('banners/',views.banner_list, name='banner_list'),
    path('banners/add/',views.add_banner, name='add_banner'),
    path('banners/edit/<int:banner_id>/',views.edit_banner, name='edit_banner'),
    path('banners/delete/<int:banner_id>/',views.delete_banner, name='delete_banner'),


    path('enquiry/',views.enquiry_form, name='enquiry_form'),
    path('submit_enquiry/',views.submit_enquiry, name='submit_enquiry'),
    path('facility_enquiries_report/',views.facility_enquiries_report, name='facility_enquiries_report'),
    path('quick_service_enquiries_report/',views.quick_service_enquiries_report, name='quick_service_enquiries_report'),
    path('package_enquiries_report/',views.package_enquiries_report, name='package_enquiries_report'),
    path("protected/",views.ProtectedDataView.as_view(), name="protected-data"),
    

    path('api/', include(router.urls)),


    





    
    
   
]


  













   





    




    





    






  





  




