"""Slide 52 : Clôture de session - Engagement personnel.

Règles neuropédagogie appliquées :
- R26 : Engagement explicite (« Je m'engage à... ») pour appropriation
- R27 : Continuité pédagogique (redirection vers ressources)
- R28 : Fermeture psychologique du module
"""

from igpde_dsfr_components import (
    add_highlight, add_alert, add_notes, new_slide
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_soustitre",
        titre="À vous de jouer",
        fil_ariane="2. Documents accessibles | Clôture",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Fin",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_highlight(
        slide,
        "Je m'engage à vérifier les styles de titre et le texte alternatif sur mon prochain document.",
        top=2.3
    )

    alert_bullets = [
        "Ressources en ligne : template Word accessible sur templates.office.com",
        "Support : guide Microsoft Rendre vos documents Word accessibles",
        "Aide rapide : Fichier > Vérifier l'accessibilité (le vérificateur détecte 80 % des oublis)"
    ]
    add_alert(
        slide,
        "Pour continuer seul(e)",
        alert_bullets,
        top=4.0,
        alert_type="info"
    )

    add_highlight(
        slide,
        "Dans 7 jours : refaites le quiz final. Dans 30 jours : ouvrez un vrai document et appliquez la checklist.",
        top=6.0
    )

    add_notes(
        slide,
        "Dernière diapo : fermeture psychologique. L'engagement explicite (« je m'engage ») "
        "crée une intention comportementale plus forte qu'une simple affirmation. Laisser "
        "chaque stagiaire écrire son engagement personnel en bas de la diapo (physique ou "
        "mental). La répétition J+7 et J+30 est un contrat entre le stagiaire et lui-même : "
        "respectez le calendrier, les réflexes s'installent."
    )
    return slide
