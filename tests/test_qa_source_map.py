"""Tests du registre source map PRD-119 Phase 2."""

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

import qa_source_map  # noqa: E402
from igpde_dsfr_components import add_callout, create_presentation, new_slide  # noqa: E402


def test_source_map_distingue_deux_composants_identiques(tmp_path):
    prs, layouts = create_presentation()
    slide = new_slide(prs, layouts, layout_name="titre_contenu", titre="Test", page_num=1)
    output = tmp_path / "source-map.json"

    qa_source_map.enable(PROJECT_ROOT, output_path=output)
    try:
        qa_source_map.start_slide(
            slide_index=1,
            slide_number="99",
            source_file="tests/test_qa_source_map.py",
            page_num=1,
        )
        add_callout(slide, "Même titre", ["Même contenu"], top=2.40)
        add_callout(slide, "Même titre", ["Même contenu"], top=3.70)
        qa_source_map.finish_slide(title="Test")
        qa_source_map.write()
    finally:
        qa_source_map.reset()

    data = json.loads(output.read_text(encoding="utf-8"))
    components = [
        component for component in data["components"]
        if component["component_type"] == "add_callout"
    ]

    assert len(components) == 2
    assert [component["call_order"] for component in components] == [1, 2]
    assert components[0]["component_id"] != components[1]["component_id"]
    assert components[0]["source_file"] == "tests/test_qa_source_map.py"
    assert isinstance(components[0]["call_lineno"], int)
    assert components[0]["shapes"][0]["rect"]["top"] != components[1]["shapes"][0]["rect"]["top"]
