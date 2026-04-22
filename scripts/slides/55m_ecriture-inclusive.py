"""Slide rs_13 : écriture inclusive - 3 stratégies OK, point médian à éviter."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L,
    add_callout, add_alert, add_highlight, add_notes, new_slide,
    estimate_callout_height, estimate_alert_height, estimate_highlight_height,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Écriture inclusive : ce qui est accessible et ce qui ne l'est pas",
        fil_ariane="4. Réseaux sociaux | Geste 4 - Texte natif",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    top = 2.30

    ok_titre = "3 stratégies accessibles"
    ok_bullets = [
        "Doublon explicite : 'les agents et les agentes' - clair à l'oral",
        "Féminin-masculin : 'les citoyennes et citoyens' - lu correctement",
        "Formulation épicène : 'les personnes concernées', 'l'équipe' - neutre et fluide",
    ]
    oh = estimate_callout_height(ok_titre, ok_bullets, COL_W)

    eviter_titre = "À éviter : le point médian"
    eviter_bullets = [
        "agent.e.s : le point médian est lu 'point' par les lecteurs d'écran",
        "NVDA lit : 'agent point e point s' - incompréhensible",
        "DGLFLF (2021) : le point médian est déconseillé dans les communications "
        "officielles pour des raisons de lisibilité et d'accessibilité",
        "La DINUM et le RGAA vont dans le même sens",
    ]
    eh = estimate_alert_height(eviter_titre, eviter_bullets, COL_W)

    col_h = max(oh, eh)
    add_callout(slide, ok_titre, ok_bullets,
                top=top, left=MARGIN_L, width=COL_W, height=col_h)
    add_alert(slide, eviter_titre, eviter_bullets,
              top=top, left=COL_R, width=COL_W, alert_type="warning")

    message = (
        "L'objectif : une communication qui inclut tout le monde "
        "ET que tout le monde peut comprendre - sans choix à faire."
    )
    hl_h = estimate_highlight_height(message, CONTENT_W)
    add_highlight(slide, message,
                  top=round(top + col_h + 0.25, 2), left=MARGIN_L, width=CONTENT_W)

    add_notes(
        slide,
        "Sujet sensible à traiter avec neutralité - ne pas prendre position sur "
        "le fond idéologique, uniquement sur la technicité d'accessibilité. "
        "Le message clé : l'accessibilité et l'inclusion ne s'opposent pas. "
        "Le point médian pose un problème technique réel (lecteur d'écran) "
        "indépendamment de toute position politique. "
        "La DGLFLF et la DINUM sont des références institutionnelles solides "
        "pour les agents qui auraient des doutes sur la légitimité de la recommandation.",
    )
    return slide
