from django.contrib import admin
import hungry.models as hm

admin.site.register(hm.Business)
admin.site.register(hm.User)
admin.site.register(hm.Friend)
admin.site.register(hm.Event)
admin.site.register(hm.Event_Attendee)

