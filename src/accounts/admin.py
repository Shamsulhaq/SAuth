from .models import User
from .email_activation import EmailActivation
from .forms import UserAdminChangeForm, UserAdminCreationForm
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'date_joined', 'last_login', 'is_active', 'is_staff', 'is_admin',)
    search_fields = ('email',)
    readonly_fields = ('date_joined', 'last_login',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active')}),
        ('Position', {'fields': ('role',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'email', 'password1', 'password2')}
         ),
    )
    list_filter = ()
    ordering = ('email',)
    filter_horizontal = ()


@admin.register(EmailActivation)
class EmailActivationAdmin(admin.ModelAdmin):
    search_fields = ['email']

    class Meta:
        model: EmailActivation


admin.site.unregister(Group)
