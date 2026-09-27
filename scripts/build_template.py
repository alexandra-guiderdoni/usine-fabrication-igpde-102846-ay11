"""Construit le template IGPDE-DSFR (13,33" x 7,5") à partir du source IGPDE (10" x 5,62").

Étapes :
1. Charge le PPTX source IGPDE
2. Rescale tous les shapes du master et des layouts (facteur 1.3333)
3. Change les dimensions de la présentation
4. Supprime les slides exemples (garder master + layouts uniquement)
5. DSFRise les layouts Sommaire (cards numérotées) et Chapitre (bandeau bleu)
6. Sauvegarde en PPT-IGPDE-DSFR-base-intervenant.pptx
"""

import shutil
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Emu, Inches

SOURCES = Path(__file__).resolve().parent.parent / "_source" / "presentations-source"
SRC = SOURCES / "PPT-IGPDE-base-intervenant.pptx"
DST = SOURCES / "PPT-IGPDE-DSFR-base-intervenant.pptx"

SCALE = 13.3333 / 10.0  # ratio de changement d'échelle

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}

BLEU_FRANCE = RGBColor(0x00, 0x00, 0x91)
ROUGE_MARIANNE = RGBColor(0xE1, 0x00, 0x0F)
BLANC = RGBColor(0xFF, 0xFF, 0xFF)
NOIR = RGBColor(0x16, 0x16, 0x16)
GRIS_CLAIR = RGBColor(0xE5, 0xE5, 0xE5)
BLEU_CLAIR = RGBColor(0xE8, 0xED, 0xFF)


def rescale_xml_shapes(xml_element, scale):
    """Multiplie left/top/cx/cy (a:off, a:ext) de tous les shapes par scale."""
    for xfrm in xml_element.iter("{%s}xfrm" % NS["a"]):
        off = xfrm.find("{%s}off" % NS["a"])
        ext = xfrm.find("{%s}ext" % NS["a"])
        if off is not None:
            if off.get("x"):
                off.set("x", str(int(int(off.get("x")) * scale)))
            if off.get("y"):
                off.set("y", str(int(int(off.get("y")) * scale)))
        if ext is not None:
            if ext.get("cx"):
                ext.set("cx", str(int(int(ext.get("cx")) * scale)))
            if ext.get("cy"):
                ext.set("cy", str(int(int(ext.get("cy")) * scale)))


def main():
    if not SRC.exists():
        raise SystemExit(
            f"Source IGPDE 10 pouces introuvable : {SRC}\n"
            "Le gabarit existant n'a pas été touché. Pour le reconstruire depuis "
            "gabarits-ppt-igpde.pptx : python3 scripts/rebuild_template_from_demo.py"
        )
    if DST.exists():
        DST.unlink()
    shutil.copy(SRC, DST)

    prs = Presentation(str(DST))

    # 1. Changer dimensions
    prs.slide_width = Inches(13.3333)
    prs.slide_height = Inches(7.5)

    # 2. Rescale master et layouts
    for master in prs.slide_masters:
        rescale_xml_shapes(master.element, SCALE)
        for layout in master.slide_layouts:
            rescale_xml_shapes(layout.element, SCALE)

    # 3. Supprimer les slides exemples
    sldIdLst = prs.slides._sldIdLst
    slide_ids = list(sldIdLst)
    for sldId in slide_ids:
        rId = sldId.get("{%s}id" % NS["r"])
        try:
            prs.part.drop_rel(rId)
        except Exception:
            pass
        sldIdLst.remove(sldId)

    # 4. Sauvegarde intermédiaire
    prs.save(str(DST))
    print(f"[OK] Template rescalé sauvegardé : {DST.name}")
    print(
        f'     Dimensions : {Emu(prs.slide_width).inches:.2f}" x {Emu(prs.slide_height).inches:.2f}"'
    )
    print(f"     Layouts : {len(prs.slide_masters[0].slide_layouts)}")
    for i, layout in enumerate(prs.slide_masters[0].slide_layouts):
        print(f"       {i}: {layout.name}")


if __name__ == "__main__":
    main()
