from django.contrib import admin
from .models import Article, Commentaire

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_creation', 'date_mise_a_jour')
    list_filter = ('auteur', 'date_creation')
    search_fields = ('titre', 'contenu')

admin.site.register(Article, ArticleAdmin)


class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('auteur', 'contenu_court', 'article', 'date_creation')
    list_filter = ('date_creation', 'auteur')
    search_fields = ('contenu', 'auteur__username', 'article__titre')

    def contenu_court(self, obj):
        if len(obj.contenu) > 50:
            return obj.contenu[:50] + "..."
        return obj.contenu
    contenu_court.short_description = 'Aperçu du Contenu'

admin.site.register(Commentaire, CommentaireAdmin)    

# Register your models here.
