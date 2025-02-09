from django.contrib import admin
from django.conf import settings
from django.contrib.auth import get_user_model
# Register your models here.


User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('id','password')
    list_display = ('username','email','first_name','last_name')
    list_editable = ('email','first_name','last_name')

    class Meta:
        model = User
        fields = "__all__"
