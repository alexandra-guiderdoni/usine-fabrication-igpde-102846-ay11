"""Slide rs_12 : faux gras / caractères Unicode - Opquast règle 14."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L,
    add_callout, add_alert, add_highlight, add_notes, new_slide,
    estimate_callout_height, estimate_alert_height, estimate_highlight_height,
)

URL_OPQUAST = "https://checklists.opquast.com/fr/qualite-numerique/les-contenus-ne-detournent-pas-de-caracteres-pour-simuler-une-mise-en-forme-visuelle"
URL_LABEL = "Opquast règle 14 - caractères détournés"


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Faux gras et caractères Unicode : le piège invisible",
        fil_ariane="4. Réseaux sociaux | Caractères spéciaux",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    top = 1.75

    probleme_titre = "Le problème"
    probleme_bullets = [
        "InstaFont, LingoJam ... proposent du 'faux gras' et 'faux italique'",
        "Exemple : \U0001d57b\U0001d578\U0001d568\U0001d573 \U0001d56c\U0001d56e\U0001d56a\U0001d574 "
        "(rendu visuel identique à du gras)",
        "Ces caractères sont des symboles mathématiques, pas du texte",
        "NVDA les lit : 'MATHEMATICAL BOLD CAPITAL B, O, N, J, O, U, R'",
        "Ou les ignore complètement - le message disparaît",
    ]
    ph = estimate_alert_height(probleme_titre, probleme_bullets, COL_W)

    triple_impact_titre = "Triple impact négatif"
    triple_impact_bullets = [
        "Accessibilité : incompréhensible pour les lecteurs d'écran",
        "SEO : Google n'indexe pas ces caractères comme du texte normal",
        "IA générative : les outils d'analyse et de traduction échouent",
    ]
    th = estimate_callout_height(triple_impact_titre, triple_impact_bullets, COL_W)

    col_h = max(ph, th)
    add_alert(slide, probleme_titre, probleme_bullets,
              top=top, left=MARGIN_L, width=COL_W, alert_type="error")
    add_callout(slide, triple_impact_titre, triple_impact_bullets,
                top=top, left=COL_R, width=COL_W, height=col_h)

    regle = (
        f"Règle qualité web : {URL_LABEL}. "
        "La mise en forme appartient au CSS, pas au contenu."
    )
    hl_h = estimate_highlight_height(regle, CONTENT_W)
    add_highlight(slide, regle,
                  top=round(top + col_h + 0.10, 2), left=MARGIN_L, width=CONTENT_W,
                  url=URL_OPQUAST)

    add_notes(
        slide,
        "Montrer en direct sur un smartphone : aller sur InstaFont, taper 'Bonjour', "
        "copier le résultat 'faux gras', le coller dans un post test, "
        "puis activer TalkBack (Android) ou VoiceOver (iPhone) pour écouter. "
        "L'effet est immédiat. "
        "La règle Opquast 14 est une référence AQW (Assurance Qualité Web) "
        "qui couvre aussi le SEO et la lisibilité IA - argument fort pour "
        "les agents qui ne sont pas encore convaincus par l'argument accessibilité seul. "
        "Solution simple : utiliser le gras natif de la plateforme (LinkedIn, "
        "Facebook permettent le formatage natif). Sinon, écrire en texte simple.",
    )
    return slide
