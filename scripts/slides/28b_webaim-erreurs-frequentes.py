"""Slide d'accroche : WebAIM Million 2026, erreurs fréquentes.

Règles neuropédagogie appliquées :
- R2 : primauté - annoncer les familles d'erreurs avant les checks
- R12 : quick wins - montrer que quelques erreurs concentrent l'impact
- R16 : tableau de correspondance pour préparer la suite du module
"""

from igpde_dsfr_components import add_callout, add_notes, add_tableau, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Six erreurs qui justifient les points de contrôle rapides",
        fil_ariane="3. points de contrôle rapides | WebAIM Million 2026",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - WebAIM",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    headers = ["Erreur fréquente", "Pages concernées", "Point d’entrée"]
    rows = [
        ["Texte à faible contraste", "83,9 %", "Contraste"],
        ["Texte alternatif d’image manquant", "53,1 %", "Images"],
        ["Étiquette de formulaire manquante", "51 %", "Formulaires"],
        ["Liens vides", "46,3 %", "Images / clavier (partiel)"],
        ["Boutons vides", "30,6 %", "Clavier / formulaires (partiel)"],
        ["Langue du document absente", "13,5 %", "Langue"],
    ]
    add_tableau(
        slide,
        headers,
        rows,
        top=2.20,
        col_widths=[4.40, 2.55, 5.33],
        row_h=0.43,
    )

    add_callout(
        slide,
        "À retenir",
        [
            "Ces six familles représentent 96 % des erreurs détectées par WebAIM.",
            "Les points de contrôle rapides donnent une méthode courte pour les repérer sans audit complet.",
        ],
        top=5.55,
        line_spacing=1.0,
    )

    add_notes(
        slide,
        "Source : The WebAIM Million, mise à jour 2026, https://webaim.org/projects/million/. "
        "Les pourcentages indiquent la part des pages d’accueil concernées par chaque type d’erreur. "
        "Faire le lien avec le programme : les stagiaires vont maintenant apprendre à repérer ces familles "
        "par des gestes simples - contraste, images, titres, clavier, langue, formulaires. "
        "Préciser que les liens et boutons vides ne sont pas un Point de contrôle rapide autonome dans ce module, "
        "mais qu’ils ressortent souvent via les tests images, clavier et formulaires. "
        "Insister sur la logique de pré-diagnostic : on ne remplace pas l’audit RGAA, on sait mieux quoi remonter.",
    )
    return slide
