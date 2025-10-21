from django.contrib import admin
from .models import Conference,Submission

# Register your models here.
admin.site.site_title="Gestion Conférence 25/26"
admin.site.site_header="Gestoin Conférence"
admin.site.index_title="Django App Conférence"
#admin.site.register(Conference)
#admin.site.register(Submission)

class SubmissionInline(admin.StackedInline):
    model=Submission
    extra=1 #nb formulaires
    readonly_fields=("submission_date",)

@admin.register(Conference)
class AdminConferenceModel(admin.ModelAdmin):
    list_display=("name","theme","start_date","end_date","a")
    ordering=("start_date",)
    list_filter=("theme",)
    search_fields=("description","name") #barre de recherche
    date_hierarchy="start_date"
    fieldsets=(
        ("Information Gnénérale",{"fields":("conference_id","name","theme","description")}),
        ("Logistics Info",{"fields":("location","start_date","end_date")})
    )
    readonly_fields=("conference_id",)
    def a(self,objet):
        if objet.start_date and objet.end_date:
            return (objet.end_date-objet.start_date).days
        return "RAS"
    a.short_description="Duration (days)"
    inlines=[SubmissionInline]

@admin.action(description="marquer les soumissions comme payés")
def mark_as_payed(modeladmin,req,queryset):
    queryset.update(payed=True)
def mark_as_accepted(m,rq,q):
    q.update(status="accepted")


@admin.register(Submission)
class AdminSubmissionModel(admin.ModelAdmin):
    list_display=("title" , "status" , "payed" , "submission_date")
    fieldsets=(
        ("Information general", {
            "fields":("title","abstract","keywords")
        }),
        ("document", {
            "fields":("paper","user","conference")
        }),
        ("Status", {
            "fields":("status","payed")
        })
    )
    actions =[mark_as_payed,mark_as_accepted]

