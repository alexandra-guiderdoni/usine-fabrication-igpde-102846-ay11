"""Slide 11 : Point de contrôle rapide 4 - Outils de mesure du contraste.

Règles neuropédagogie appliquées :
- R16 : tableau d'outils
- R19 : feedback immédiat - chaque outil donne le verdict en 1 clic
- R24 : plan d'action - choisir son outil fétiche
"""

from igpde_dsfr_components import add_alert, add_notes, add_tableau, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Contraste : 3 outils à avoir sous la main",
        fil_ariane="3. points de contrôle rapides | 4. Contraste",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - Contraste",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    headers = ["Outil", "Usage", "Quand l’utiliser"]
    rows = [
        [
            "DevTools Chrome / Firefox",
            "Clic droit sur un texte → Inspecter → pastille de couleur.",
            "Mesure ponctuelle pendant la rédaction ou la relecture.",
        ],
        [
            "WebAIM Contrast Checker",
            "webaim.org/resources/contrastchecker - coller les deux couleurs hex.",
            "Avant de choisir une charte graphique ou un thème.",
        ],
        [
            "Colour Contrast Analyser (CCA)",
            "App desktop - pipette qui mesure n’importe quelle zone d’écran.",
            "Tester des maquettes Figma, des captures d’écran, des PDF.",
        ],
    ]
    add_tableau(
        slide, headers, rows,
        top=2.4,
        col_widths=[3.20, 4.58, 4.50],
        row_h=0.72,
    )

    add_alert(
        slide,
        titre="Piège classique",
        bullets=[
            "Texte gris clair sur fond blanc (#999 sur #FFF) : 2,85:1 - échec même en texte large",
            "Bouton bleu avec texte bleu marine « moderne » : souvent sous le seuil",
        ],
        top=5.00, height=1.05,
        alert_type="warning",
    )

    add_notes(
        slide,
        "Démo live : prendre la page d’accueil de Bercy et mesurer 3 textes au hasard. "
        "Laisser les stagiaires deviner avant la mesure. "
        "Engagement (R24) : choisissez votre outil préféré d’ici la fin de la session et testez 5 couleurs "
        "de votre charte dans la semaine.",
    )
    return slide
