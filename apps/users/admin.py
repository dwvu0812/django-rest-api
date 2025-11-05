from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = [
        'email', 'username', 'user_type', 
        'is_verified', 'is_active', 'date_joined'
    ]
    
    list_filter = [
        'user_type', 'is_verified', 'is_active', 
        'is_staff', 'date_joined'
    ]
    
    search_fields = ['email', 'username', 'first_name', 'last_name']
    ordering = ['-date_joined']
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': (
                'user_type', 'phone', 'avatar', 'bio', 
                'is_verified', 'date_of_birth'
            )
        }),
    )
    
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('email', 'user_type')
        }),
    )
