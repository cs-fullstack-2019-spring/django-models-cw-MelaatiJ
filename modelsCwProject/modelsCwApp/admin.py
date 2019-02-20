from django.contrib import admin

# Register your models here.

#call it ino order for it to show up in the admin page


#for the dog model , so that way it comes on admin page
from . models import Dog
admin.site.register(Dog)


#for the account model so it comes on the admin page
from . models import Account
admin.site.register(Account)