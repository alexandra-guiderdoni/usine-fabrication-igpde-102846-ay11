"""Slide 42 : Pilier 4 - Espaces et objets clignotants.

Règles neuropédagogie appliquées :
- R21 : Révéler les caractères invisibles (symboles de paragraphe)
- R11 : Alerte zéro-tolérance sur l'épilepsie (sécurité avant pédagogie)
- R15 : Démonstration directe du mode Afficher tout
"""

from igpde_dsfr_components import (
    add_callout, add_alert, add_notes, new_slide,
    estimate_callout_height, estimate_alert_height
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Pilier 4 - Espaces et objets clignotants",
        fil_ariane="2. Documents accessibles | 4. Langue",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Langue",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    callout_bullets = [
        "Points = espaces successifs > supprimer et ne garder qu'un seul espace",
        "Flèches = tabulations utilisées pour simuler une mise en page",
        "Retours à la ligne manuels = utiliser les sauts de page propres à la place"
    ]
    add_callout(
        slide,
        "Activer les marques de formatage : Accueil > Paragraphe > Afficher tout (signe paragraphe)",
        callout_bullets,
        top=2.3
    )

    alert_bullets = [
        "Animations, GIF avec flashs, vidéos à plus de 3 Hz : interdits sans exception",
        "Risque de crise d'épilepsie photosensible",
        "En cas de doute sur un GIF : remplacer par une image statique"
    ]
    add_alert(
        slide,
        "Objets clignotants : tolérance zéro",
        alert_bullets,
        top=5.5,
        alert_type="error"
    )

    add_notes(
        slide,
        "Les espaces parasites sont invisibles mais cassent la structure du document. "
        "Montrer la différence entre Afficher tout activé et désactivé. Pour les objets "
        "clignotants : c'est une règle de sécurité, pas de préférence. Un seul incident "
        "suffira pour comprendre pourquoi."
    )
    return slide
