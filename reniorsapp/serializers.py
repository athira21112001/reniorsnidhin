from rest_framework import serializers
from .models import Country, State, District, City, Facility, FacilityImage, FacilityVideo, QuickService, Package, Article,Banner,EnquiryFormContent

 
 

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class FacilityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityImage
        fields = '__all__'

class FacilityVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityVideo
        fields = '__all__'

class FacilitySerializer(serializers.ModelSerializer):
    images = FacilityImageSerializer(many=True, read_only=True)
    videos = FacilityVideoSerializer(many=True, read_only=True)

    country = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()
    district = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()

    class Meta:
        model = Facility
        fields = '__all__'

    def get_country(self, obj):
        return obj.country.name if obj.country else None  # Fetch country name

    def get_state(self, obj):
        return obj.state.name if obj.state else None  # Fetch state name

    def get_district(self, obj):
        return obj.district.name if obj.district else None  # Fetch district name

    def get_city(self, obj):
        return obj.city.name if obj.city else None  # Fetch city name

class QuickServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuickService
        fields = '__all__'

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'




class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'  # Includes all fields in the model






class EnquiryFormContentSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source="country.name")
    state = serializers.CharField(source="state.name")
    district = serializers.CharField(source="district.name")
    city = serializers.CharField(source="city.name")
    quick_service = serializers.CharField(source="quick_service.name")
    facility = serializers.CharField(source="facility.name")
    package = serializers.CharField(source="package.name")

    class Meta:
        model = EnquiryFormContent
        fields = "__all__"

