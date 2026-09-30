"""Slide 02k : idée reçue 5 - ça coûte trop cher."""

from igpde_dsfr_components import (
    COL_R, COL_W, MARGIN_L,
    add_card, add_callout, add_qrcode, add_notes, new_slide,
    estimate_card_height, estimate_callout_height,
)

URL_SOURCE = "https://ideance.net/blog/4602/idees-recues-a11y"
NUMERO = 5


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        fil_ariane="1. Introduction | Idées reçues",
        titre="Idée reçue 5 / 6",
        footer_text=f"{ctx.footer_base} / Accueil",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    top_cols = 2.30
    idee_text = "« Ça coûte trop cher »"

    decrypt_bullets = [
        "Oui - si l'accessibilité est traitée comme un ajustement en fin de projet",
        "Non - si elle est intégrée dès la conception (approche « shift left »)",
        "Corriger un document Word après publication : 10 fois plus cher que le faire d'emblée",
        "Les réflexes appris aujourd'hui ne coûtent rien : juste un changement d'habitude",
    ]

    extra_height = 0.08
    callout_h = estimate_callout_height("Décryptage", decrypt_bullets, COL_W, line_spacing=1.30, compact=True) + extra_height
    card_h = estimate_card_height("Idée reçue", [idee_text], COL_W, numero=NUMERO)

    add_card(
        slide, "Idée reçue", idee_text,
        top=top_cols, left=MARGIN_L, width=COL_W, height=card_h, numero=NUMERO,
    )
    add_callout(
        slide, "Décryptage", decrypt_bullets,
        top=top_cols, left=COL_R, width=COL_W, line_spacing=1.30, compact=True,
        extra_height=extra_height,
    )

    url_top = round(top_cols + callout_h + 0.15, 2)
    add_qrcode(slide, "_assets/qrcode-ideance-idees-recues.png",
               url=URL_SOURCE, top=url_top, left=COL_R, size=0.95,
               label=URL_SOURCE, label_width=COL_W - 1.10)

    add_notes(
        slide,
        "Analogie bâtiment : une rampe d'accès intégrée dès la construction coûte quelques centaines d'euros. "
        "La reprise après construction, plusieurs milliers. "
        "Pour les documents : appliquer les styles Titre dans Word, c'est 30 secondes de plus. "
        "Corriger un PDF de 50 pages après coup, c'est des heures. "
        "L'accessibilité est rentable quand elle est intégrée - c'est le message central.",
    )
    return slide
