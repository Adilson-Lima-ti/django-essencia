from django.contrib import admin

from . models import Customer, Expense


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    List_dsplay = ('__srt__', 'email') #customização Admin
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    List_dsplay = ('__srt__', 'customer', 'value', 'payment_date', 'paid') #customização Admin
    search_fields = ('description', 'customer__firt_name', 'customer__last_name') # noqa E501
    list_filter = ('paid',)
    date_hierarchy ='payment_date'

