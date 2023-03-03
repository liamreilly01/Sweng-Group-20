from django.contrib import admin
from .models import Legislation, Questionanswer
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.

class DataResource(resources.ModelResource):
    class Meta:
        model = Legislation


class DataAdmin(ImportExportModelAdmin):
    resource_class = DataResource


class QuestionsResource(resources.ModelResource):
    class Meta:
        model = Questionanswer


class QuestionAdmin(ImportExportModelAdmin):
    resource_class = QuestionsResource


admin.site.register(Questionanswer, QuestionAdmin)
admin.site.register(Legislation, DataAdmin)
