"""Slide 17 : Point de contrôle rapide 7 - Langue de la page.

Règles neuropédagogie appliquées :
- R8 : analogie - le lecteur d'écran est un comédien qui attend son script
- R15 : jargon supprimé - attribut lang expliqué en 1 phrase
"""

from igpde_dsfr_components import (
    Stack,
    add_alert,
    add_callout,
    add_highlight,
    add_notes,
    estimate_alert_height,
    estimate_callout_height,
    estimate_highlight_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Langue de la page : l’accent juste du lecteur d’écran",
        fil_ariane="3. points de contrôle rapides | 7. Langue",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - Langue",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.10, gap=0.18)

    add_highlight(
        slide,
        "Sans langue déclarée, le lecteur d’écran peut choisir une mauvaise prononciation et rendre le texte pénible à écouter.",
        top=stack.push(estimate_highlight_height('Sans langue déclarée, le lecteur d’écran peut choisir une mauvaise prononciation et rendre le texte pénible à écouter.')),
    )

    add_callout(
        slide,
        "Ce qu’il faut vérifier :",
        [
            "La balise <html> porte un attribut lang (ex. lang=\"fr\")",
            "Les passages dans une autre langue sont balisés : <span lang=\"en\">workshop</span>",
            "Le code langue suit la norme ISO 639 : fr, en, de, es - pas « français »",
        ],
        top=stack.push(estimate_callout_height('Ce qu’il faut vérifier :', ['La balise <html> porte un attribut lang (ex. lang="fr")', 'Les passages dans une autre langue sont balisés : <span lang="en">workshop</span>', 'Le code langue suit la norme ISO 639 : fr, en, de, es - pas « français »'])),
    )

    add_alert(
        slide,
        titre="Comment vérifier sans coder",
        bullets=[
            "Clic droit → Afficher le code source → regarder la 1ʳᵉ ligne <html lang=\"…\">",
            "Ou extension « Web Developer » → Information → View Document Language",
        ],
        top=stack.push(estimate_alert_height('Comment vérifier sans coder', ['Clic droit → Afficher le code source → regarder la 1ʳᵉ ligne <html lang="…">', 'Ou extension « Web Developer » → Information → View Document Language'])),
        alert_type="info",
    )

    add_notes(
        slide,
        "Démo : activer VoiceOver ou NVDA sur une page sans lang et comparer la prononciation. "
        "Analogie : un comédien à qui on ne dit pas dans quelle langue jouer - il bute sur chaque mot. "
        "Piège : un gabarit peut être visuellement français tout en oubliant lang=\"fr\" dans le code.",
    )
    return slide
