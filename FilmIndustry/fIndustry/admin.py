from django.contrib import admin
from .models import person
from .models import talent
from .models import bankDetails
from .models import job
from .models import jobTalent
from .models import Admin
# Register your models here.
admin.site.register(person)
admin.site.register(talent)
admin.site.register(bankDetails)
admin.site.register(jobTalent)
admin.site.register(job)
admin.site.register(Admin)