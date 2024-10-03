from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count=0
        for form in self.forms:
            if form.cleaned_data['is_main'] and count==0:
                print(form.cleaned_data['is_main'])
                return super().clean()
            else:
                # вызовом исключения ValidationError можно указать админке о наличие ошибки
                # таким образом объект не будет сохранен,
                # а пользователю выведется соответствующее сообщение об ошибке
                raise ValidationError('Тут всегда ошибка')
        return super().clean()

class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset
    extra = 3

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    #pass
    inlines = [RelationshipInline,]
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass

