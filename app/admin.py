from django.contrib import admin

# Register your models here.


from django.contrib.admin import AdminSite
from django.http import HttpResponseRedirect

from .models import MyModel3, Applicant  # Import both models

# MyModel3 Admin Configuration
class MyModel3Admin(admin.ModelAdmin):
    # Specify which fields to display in the admin list view
    list_display = ('name', 'email', 'phone', 'recentedu', 'relatedexp', 'companies', 
                    'licenseType', 'passdate', 'expdate', 'cpccard', 'totalcpc', 
                    'address', 'city', 'distance')
    
    # Add filters based on these fields
    list_filter = ('name', 'email', 'phone', 'licenseType', 'city', 'passdate', 'expdate')
    
    # Enable search functionality for these fields
    search_fields = ('name', 'email', 'phone', 'recentedu', 'relatedexp', 'companies', 'city')
    
    # Optional: You can group fields in sections using fieldsets
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Education and Experience', {
            'fields': ('recentedu', 'relatedexp', 'companies')
        }),
        ('License Information', {
            'fields': ('licenseType', 'passdate', 'expdate', 'cpccard', 'totalcpc')
        }),
        ('Address and Location', {
            'fields': ('address', 'city', 'distance')
        }),
    )
    
    # Optionally make some fields read-only
    readonly_fields = ('passdate', 'expdate')

# Applicant Admin Configuration
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone','qualifications')
    list_filter = ('name', 'email', 'phone','qualifications')
    search_fields = ('name', 'email', 'phone','qualifications')

# Register both models
admin.site.register(MyModel3, MyModel3Admin)
admin.site.register(Applicant, ApplicantAdmin)


class MyAdminSite(AdminSite):
    def login(self, request, extra_context=None):
        response = super(MyAdminSite, self).login(request, extra_context)
        # Check if the login was successful and the user has been authenticated
        if request.method == 'POST' and request.user.is_authenticated:
            return HttpResponseRedirect('/custom-page/')  # Redirect to a custom page
        else:
            return response

# Replace the default admin site with the custom one
admin_site = MyAdminSite(name='myadmin')
