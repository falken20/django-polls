from django.contrib import admin

from .models import Question, Choice

# With this registration Django is able to construct a defaut form
# representation for the model in admin

# admin.site.register(Question)
# admin.site.register(Choice)


# Choice objects are edited on the Question admin page. By default,
# provide enough fields for 3 choices
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# We can set up this representation in the admin for a particula model
class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    # Set up the way to list the questions
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # Set up fields for filters
    list_filter = ['pub_date']
    # Set up search fields
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

