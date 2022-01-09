from django.contrib import admin
from .models import  Profile,NeighborHood,Location,Business,Authorities,Post,Category,Health

# Register your models here.
admin.site.register(Profile)
admin.site.register(NeighborHood)
admin.site.register(Location)
admin.site.register(Business)
admin.site.register(Authorities)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Health)