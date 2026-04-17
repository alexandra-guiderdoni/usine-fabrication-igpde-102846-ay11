"""Slide 26 : Easy Check 13 - Champs obligatoires.

Règles neuropédagogie appliquées :
- R5 : chunking - 3 règles simples
- R18 : sécurité psychologique - les erreurs doivent guider, pas punir
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
        titre="Champs obligatoires : dits, pas juste marqués",
        fil_ariane="3. Easy Checks | 13. Champs obligatoires",
        footer_text=f"{ctx.footer_base} / Easy Checks - Champs obligatoires",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.35)

    add_highlight(
        slide,
        "Un astérisque rouge est un signal visuel - il doit être doublé d’une information textuelle pour tous.",
        top=stack.push(estimate_highlight_height('Un astérisque rouge est un signal visuel - il doit être doublé d’une information textuelle pour tous.')),
    )

    add_callout(
        slide,
        "Ce qu’il faut vérifier :",
        [
            "Les champs obligatoires sont indiqués textuellement (« obligatoire » ou « *requis »)",
            "La légende « * champ obligatoire » est présente en début de formulaire",
            "Techniquement : attribut required ou aria-required=\"true\" sur le champ",
            "En cas d’erreur : le message pointe le champ par son étiquette, pas « champ 3 »",
        ],
        top=stack.push(estimate_callout_height('Ce qu’il faut vérifier :', ['Les champs obligatoires sont indiqués textuellement (« obligatoire » ou « *requis »)', 'La légende « * champ obligatoire » est présente en début de formulaire', 'Techniquement : attribut required ou aria-required="true" sur le champ', 'En cas d’erreur : le message pointe le champ par son étiquette, pas « champ 3 »'])),
    )

    add_alert(
        slide,
        titre="Pattern recommandé",
        bullets=[
            "Marquez les champs OPTIONNELS, pas les obligatoires - plus court sur un formulaire où 90 % des champs sont requis",
        ],
        top=stack.push(estimate_alert_height('Pattern recommandé', ['Marquez les champs OPTIONNELS, pas les obligatoires - plus court sur un formulaire où 90 % des champs sont requis'])),
        alert_type="info",
    )

    add_notes(
        slide,
        "Règle d’or : couleur seule = information perdue pour les aveugles et les daltoniens. "
        "Exemple à tester : un champ obligatoire marqué uniquement par astérisque rouge - lecteur d’écran n’annonce rien. "
        "Message d’erreur à éviter : « Erreur champ 3 » → préférer « Votre adresse électronique est obligatoire ».",
    )
    return slide
