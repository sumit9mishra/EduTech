from django.contrib import admin

from .models import (
    Course,
    Student,
    Cart,
    OrderPlaced
    

)


@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city', 'zipcode', 'state']


@admin.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price',
                    'description', 'category']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'Course', 'quantity']


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'Student',
                    'Course', 'ordered_date',]
