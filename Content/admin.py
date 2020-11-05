from django.contrib import admin
from .models import AllCourse, Contact, Blog, Motivational_Quote, Blogcomment
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'countrycode', 'phone', 'email')
    search_fields = ['name','phone', 'email']

class AllCourseAdmin(admin.ModelAdmin):
    search_fields = ['Name', 'Category']

class BlogAdmin(admin.ModelAdmin):
    search_fields = ['title']
    
admin.site.register(AllCourse, AllCourseAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Motivational_Quote)