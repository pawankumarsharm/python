from django.contrib import admin
from jobcityapp.models import Hydjobs,Blrjobs,punejobs,Chennaijobs
class HydJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phoneno']
class BlrJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phoneno']
class PuneJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phoneno']
class ChennaiJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phoneno']
admin.site.register(Hydjobs,HydJobsAdmin)
admin.site.register(Blrjobs,BlrJobsAdmin)
admin.site.register(punejobs,PuneJobsAdmin)
admin.site.register(Chennaijobs,ChennaiJobsAdmin)
