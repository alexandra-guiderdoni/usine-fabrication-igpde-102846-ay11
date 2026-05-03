"""Slide 54 : réseaux sociaux - enjeux et annonce des 4 gestes."""

from igpde_dsfr_components import (
    CONTENT_W, GAP, MARGIN_L, Stack,
    add_callout, add_alert, add_highlight, add_notes,
    estimate_highlight_height, estimate_callout_height, estimate_alert_height, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Pourquoi l'accessibilité sur les réseaux ?",
        fil_ariane="4. Réseaux sociaux",
        footer_text=f"{ctx.footer_base} / Module 4",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.30, gap=0.35)

    texte_hl = (
        "Les réseaux sociaux sont devenus un canal officiel de communication "
        "publique - et donc soumis aux mêmes obligations d'accessibilité."
    )
    add_highlight(slide, texte_hl, top=stack.push(estimate_highlight_height(texte_hl)))

    public_titre = "Votre audience est plus large que vous ne le pensez"
    public_bullets = [
        "12 millions de personnes en situation de handicap en France (INSEE 2021)",
        "Utilisateurs en contexte défavorable : faible luminosité, connexion lente, bruit",
        "Moteurs de recherche et outils d'IA qui analysent vos contenus",
        "Collègues et citoyens qui lisent sans images activées",
    ]
    ph = estimate_callout_height(public_titre, public_bullets, CONTENT_W)
    add_callout(slide, public_titre, public_bullets,
                top=stack.push(ph), left=MARGIN_L, width=CONTENT_W)

    gestes_titre = "4 gestes, 2 minutes par post"
    gestes_bullets = [
        "Geste 1 - Texte alternatif : décrire chaque image en 1 phrase",
        "Geste 2 - Émojis : 1 ou 2 maximum, en fin de message",
        "Geste 3 - Hashtags : CamelCase et regroupés en fin de post",
        "Geste 4 - Texte natif : jamais de faux gras ou faux italique",
    ]
    add_alert(slide, gestes_titre, gestes_bullets,
              top=stack.push(0), left=MARGIN_L, width=CONTENT_W, alert_type="success")

    add_notes(
        slide,
        "La stat des 12 millions vient de l'INSEE (enquête Handicap-Santé 2021). "
        "Ne pas chercher à impressionner avec des chiffres spectaculaires - "
        "le vrai impact c'est 'quelqu'un dans votre public ne pourra pas lire ce post'. "
        "Annoncer la structure : 4 gestes que vous allez voir en détail. "
        "Commencer par une question : 'Sur vos 10 derniers posts, "
        "combien avaient un texte alternatif sur les images ?'",
    )
    return slide
