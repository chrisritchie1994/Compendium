from django.contrib import admin
from compendium_app.models import Journal, Idea, Decision, Principle, Aphorism

admin.site.register(Journal)
admin.site.register(Idea)
admin.site.register(Decision)
admin.site.register(Principle)
admin.site.register(Aphorism)

# Register your models here.
