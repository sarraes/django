from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from django.utils.translation import gettext_lazy as _
from .models import User, Organizing_Commitee 

admin.site.site_title = "Gestion Conférence 25/26"
admin.site.site_header = "Gestion Conférences"
admin.site.index_title = "Django App Conférence"

class CustomUserAdmin(UserAdmin):
    list_display = ('user_id', 'username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    ordering = ('last_name', 'first_name')
    list_filter = ('role',)
    search_fields = ('first_name', 'last_name',)
    readonly_fields = ('user_id', 'created_at', 'update_at',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal Info'), {
            'fields': ('user_id', 'first_name', 'last_name', 'email', 'affiliation', 'nationality', 'role')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined', 'created_at', 'update_at')
        }),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password', 'password') 
        }),
        (_('Personal Info'), {
            'fields': ('first_name', 'last_name', 'affiliation', 'nationality', 'role')
        }),

    )

@admin.register(Organizing_Commitee)
class AdminOrganizingCommiteeModel(admin.ModelAdmin):
    list_display = ("user", "conference", "commitee_role", "date_joined") 
    ordering = ("conference", "commitee_role")
    list_filter = ("commitee_role",)
    search_fields = ("user__first_name", "user__last_name")
    date_hierarchy = "date_joined"

    fieldsets = (
        ("Committee Assignment", {
            "fields": ("user", "conference", "commitee_role")
        }),
        ("Dates", {
            "fields": ("date_joined",) 
        }),
    )
    readonly_fields = ('created_at', 'update_at')

if admin.site.is_registered(User):
    admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
