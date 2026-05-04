"""Slide 20 : Point de contrôle rapide 9 - Piège des sous-titres automatiques.

Règles neuropédagogie appliquées :
- R18 : sécurité psychologique - l'auto est un point de départ, pas une arrivée
- R19 : feedback par exemple OK/KO
- R11 : faire deviner les erreurs typiques
"""

from igpde_dsfr_components import (
    Stack,
    add_alert,
    add_callout,
    add_notes,
    estimate_alert_height,
    estimate_callout_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Sous-titres auto : brouillon utile, livrable à relire",
        fil_ariane="3. points de contrôle rapides | 9. Sous-titres",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - Sous-titres",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.35)

    add_callout(
        slide,
        "Pourquoi l’auto ne suffit pas :",
        [
            "Les sous-titres automatiques peuvent déformer les mots, surtout les noms propres et acronymes",
            "Noms propres, acronymes, chiffres : souvent mal reconnus",
            "Ponctuation absente : « on mange les enfants » vs « on mange, les enfants »",
            "Pas d’indication sonore non verbale (musique, applaudissements)",
        ],
        top=stack.push(estimate_callout_height('Pourquoi l’auto ne suffit pas :', ['Les sous-titres automatiques peuvent déformer les mots, surtout les noms propres et acronymes', 'Noms propres, acronymes, chiffres : souvent mal reconnus', 'Ponctuation absente : « on mange les enfants » vs « on mange, les enfants »', 'Pas d’indication sonore non verbale (musique, applaudissements)'])),
    )

    add_alert(
        slide,
        titre="Méthode recommandée",
        bullets=[
            "Étape 1 : générer l’auto (YouTube, Whisper, outil interne) pour accélérer le brouillon",
            "Étape 2 : relire, corriger, ajouter ponctuation et [indications sonores]",
            "Étape 3 : caler le timing sur les pauses naturelles (2 lignes max à l’écran)",
        ],
        top=stack.push(estimate_alert_height('Méthode recommandée', ['Étape 1 : générer l’auto (YouTube, Whisper, outil interne) pour accélérer le brouillon', 'Étape 2 : relire, corriger, ajouter ponctuation et [indications sonores]', 'Étape 3 : caler le timing sur les pauses naturelles (2 lignes max à l’écran)'], line_spacing=1.0)),
        alert_type="success",
        line_spacing=1.0,
    )

    add_notes(
        slide,
        "Faire deviner : « Quels mots un sous-titrage auto rate le plus souvent ? » "
        "Exemple concret à projeter : une vidéo ministérielle avec sous-titres automatiques - pointer 3 erreurs. "
        "Règle d’or (R18) : l’automatique est un allié pour brouillonner, mais la publication demande une relecture humaine.",
    )
    return slide
