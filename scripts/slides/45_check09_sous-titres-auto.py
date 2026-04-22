"""Slide 20 : Easy Check 9 - Piège des sous-titres automatiques.

Règles neuropédagogie appliquées :
- R18 : sécurité psychologique - l'auto est un point de départ, pas une arrivée
- R19 : feedback par exemple OK/KO
- R11 : faire deviner le taux d'erreur
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
        titre="Sous-titres auto : brouillon utile, livrable jamais",
        fil_ariane="3. Easy Checks | 9. Sous-titres",
        footer_text=f"{ctx.footer_base} / Easy Checks - Sous-titres",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.35)

    add_callout(
        slide,
        "Pourquoi l’auto ne suffit pas :",
        [
            "YouTube auto : 10 à 30 % d’erreurs sur un français soigné, pire avec un accent",
            "Noms propres, acronymes, chiffres : souvent massacrés",
            "Ponctuation absente : « on mange les enfants » vs « on mange, les enfants »",
            "Pas d’indication sonore non verbale (musique, applaudissements)",
        ],
        top=stack.push(estimate_callout_height('Pourquoi l’auto ne suffit pas :', ['YouTube auto : 10 à 30 % d’erreurs sur un français soigné, pire avec un accent', 'Noms propres, acronymes, chiffres : souvent massacrés', 'Ponctuation absente : « on mange les enfants » vs « on mange, les enfants »', 'Pas d’indication sonore non verbale (musique, applaudissements)'])),
    )

    add_alert(
        slide,
        titre="Méthode recommandée",
        bullets=[
            "Étape 1 : générer l’auto (YouTube, Whisper, outil interne) pour gagner 80 % du temps",
            "Étape 2 : relire, corriger, ajouter ponctuation et [indications sonores]",
            "Étape 3 : caler le timing sur les pauses naturelles (2 lignes max à l’écran)",
        ],
        top=stack.push(estimate_alert_height('Méthode recommandée', ['Étape 1 : générer l’auto (YouTube, Whisper, outil interne) pour gagner 80 % du temps', 'Étape 2 : relire, corriger, ajouter ponctuation et [indications sonores]', 'Étape 3 : caler le timing sur les pauses naturelles (2 lignes max à l’écran)'])),
        alert_type="success",
    )

    add_notes(
        slide,
        "Faire deviner : « Quel est le taux d’erreur moyen d’un sous-titrage auto en français ? » "
        "(20 %, soit 1 mot sur 5). "
        "Exemple concret à projeter : une vidéo ministérielle avec sous-titres auto - pointer 3 erreurs. "
        "Règle d’or (R18) : l’automatique est un allié pour brouillonner, une faute s’il est publié tel quel.",
    )
    return slide
