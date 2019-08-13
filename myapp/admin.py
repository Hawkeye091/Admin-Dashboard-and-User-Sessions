from django.contrib import admin
from .models import MySimpleModel
from io import StringIO
# Register your models here.
class MyAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    list_display = ('emp_id', 'emp_name','emp_post','emp_salary')
    search_fields = ('emp_id','emp_name',)
    def download_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        from io import StringIO

        f = StringIO()
        writer = csv.writer(f)
        writer.writerow(["emp_id", "emp_name", "emp_post", "emp_salary"])

        for s in queryset:
            writer.writerow([s.emp_id, s.emp_name, s.emp_post, s.emp_salary])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=stat-info.csv'
        return response
    download_csv.short_description = "Download CSV file for selected stats."
admin.site.register(MySimpleModel,MyAdmin)