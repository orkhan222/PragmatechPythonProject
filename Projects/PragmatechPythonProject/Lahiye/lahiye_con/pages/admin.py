from django.contrib import admin
from django.db.models.deletion import CASCADE
from . models import Slider,HomeBestSeller,MenViewProduct,Contact,About,Home,MenSlider,MenShopNow,WomenSlider,TrustedPartner,WomenShopNow,Cart,Related,Product,ShopMore

# Register your models here.

admin.site.register(Slider)
admin.site.register(HomeBestSeller)
admin.site.register(MenViewProduct)
admin.site.register(Contact)
admin.site.register(About)
admin.site.register(Home)
admin.site.register(MenSlider)
admin.site.register(MenShopNow)
admin.site.register(WomenSlider)
admin.site.register(WomenShopNow)
admin.site.register(TrustedPartner)
admin.site.register(Cart)
admin.site.register(Related)
admin.site.register(Product)
admin.site.register(ShopMore)



class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

admin.site.register(Contact,ContactAdmin)