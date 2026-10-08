#!/usr/bin/env python3
"""
md2pdf — Convert Markdown to accessible tagged PDF (PDF/UA-1).
Pipeline: Pandoc (Markdown → HTML5 semantic) → CSS injection → WeasyPrint (HTML → PDF/UA-1).
"""

import argparse
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(SCRIPT_DIR)
TEMPLATES_DIR = os.path.join(SKILL_DIR, 'templates')
MD2DOCX_SCRIPT = os.path.join(os.path.dirname(SKILL_DIR), 'accessible-docx', 'scripts', 'md2docx.py')
SOFFICE_PATH = '/Applications/LibreOffice.app/Contents/MacOS/soffice'

# Import module partage a11y_editorial (PRD-069)
_A11Y_SHARED = os.path.join(os.path.dirname(SKILL_DIR), 'a11y-shared-references', 'scripts')
if _A11Y_SHARED not in sys.path:
    sys.path.insert(0, _A11Y_SHARED)
try:
    from a11y_editorial import (
        detect_acronymes, corriger_capitales,
        detect_liens_generiques, detect_paragraphes_vides_html
    )
    _HAS_A11Y_EDITORIAL = True
except ImportError:
    _HAS_A11Y_EDITORIAL = False

# Candidate Python interpreters that may have WeasyPrint with Pango/GLib access.
PREFERRED_PYTHONS = [
    '/opt/homebrew/bin/python3',
    '/opt/homebrew/bin/python3.14',
    '/opt/homebrew/bin/python3.13',
    '/opt/homebrew/bin/python3.12',
    '/opt/homebrew/bin/python3.11',
    '/opt/homebrew/bin/python3.10',
    sys.executable,
    'python3',
]


def _command_exists(path):
    if os.path.isabs(path):
        return os.path.exists(path)
    return shutil.which(path) is not None


def check_deps():
    """Check that all dependencies are available."""
    ok = True

    # Pandoc
    try:
        r = subprocess.run(['pandoc', '--version'], capture_output=True, text=True)
        version = r.stdout.split('\n')[0] if r.returncode == 0 else None
        print(f"  Pandoc: {version}")
    except FileNotFoundError:
        print("  Pandoc: MANQUANT — brew install pandoc")
        ok = False

    # Python
    python = find_python()
    if _command_exists(python):
        r = subprocess.run(
            [python, '--version'],
            capture_output=True, text=True
        )
        version = (r.stdout or r.stderr).strip()
        print(f"  Python: {python} ({version})")
    else:
        print("  Python: MANQUANT — brew install python")
        ok = False

    # WeasyPrint
    r = subprocess.run(
        [python, '-c', 'import weasyprint; print(weasyprint.__version__)'],
        capture_output=True, text=True
    )
    if r.returncode == 0:
        print(f"  WeasyPrint: {r.stdout.strip()}")
    else:
        print(f"  WeasyPrint: MANQUANT — {python} -m pip install weasyprint")
        ok = False

    # Pango/GLib
    pango = glob.glob('/opt/homebrew/lib/libpango*')
    glib = glob.glob('/opt/homebrew/lib/libgobject*')
    if pango and glib:
        print("  Pango/GLib: OK")
    else:
        print("  Pango/GLib: MANQUANT — brew install pango glib")
        ok = False

    # pikepdf (XMP language metadata)
    r = subprocess.run(
        [python, '-c', 'import pikepdf; print(pikepdf.__version__)'],
        capture_output=True, text=True
    )
    if r.returncode == 0:
        print(f"  pikepdf: {r.stdout.strip()}")
    else:
        print(f"  pikepdf: MANQUANT — {python} -m pip install pikepdf")
        print("    (Optionnel: injection XMP dc:language pour conformite RGAA 13.6)")

    # Templates
    templates = [f for f in os.listdir(TEMPLATES_DIR) if f.endswith('.css')] if os.path.isdir(TEMPLATES_DIR) else []
    print(f"  Templates: {', '.join(t.replace('.css','') for t in sorted(templates)) or 'aucun'}")

    return ok


def find_python():
    """Find the best available Python for WeasyPrint/PDF post-processing."""
    for python in PREFERRED_PYTHONS:
        if _command_exists(python):
            return python
    return 'python3'


def extract_title_from_md(md_path):
    """Extract title (first H1) and subtitle (first H2) from markdown."""
    title, subtitle = None, None
    with open(md_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not title and line.startswith('# ') and not line.startswith('## '):
                title = line[2:].strip()
            elif title and not subtitle and line.startswith('## '):
                subtitle = line[3:].strip()
            if title and subtitle:
                break
    return title, subtitle


def warn_missing_alt_text(md_path):
    """Warn about images without alt text (PDF/UA-1 + WCAG 1.1.1 violation)."""
    warnings = []
    with open(md_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            # Match ![](url) or ![ ](url) — empty or whitespace-only alt
            for match in re.finditer(r'!\[(\s*)\]\(([^)]+)\)', line):
                url = match.group(2)
                warnings.append((i, url))
    if warnings:
        print(f"\n  Attention — {len(warnings)} image(s) sans texte alternatif :")
        for line_num, url in warnings:
            print(f"    Ligne {line_num}: {url}")
        print("  (Violation PDF/UA-1 et WCAG 1.1.1 — ajoutez un alt text)")
    return warnings


def _relative_luminance(hex_color):
    """Calculate relative luminance of a hex color (WCAG 2.1)."""
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = ''.join(c * 2 for c in hex_color)
    r, g, b = int(hex_color[0:2], 16) / 255, int(hex_color[2:4], 16) / 255, int(hex_color[4:6], 16) / 255
    r = r / 12.92 if r <= 0.04045 else ((r + 0.055) / 1.055) ** 2.4
    g = g / 12.92 if g <= 0.04045 else ((g + 0.055) / 1.055) ** 2.4
    b = b / 12.92 if b <= 0.04045 else ((b + 0.055) / 1.055) ** 2.4
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _contrast_ratio(hex1, hex2):
    """Calculate WCAG contrast ratio between two hex colors."""
    l1 = _relative_luminance(hex1)
    l2 = _relative_luminance(hex2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def audit_html_a11y(html_path):
    """Audit HTML for accessibility issues (contrasts in CSS, RGAA 13.8)."""
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    warnings = []

    # --- Contrast check: extract color pairs from inline <style> ---
    color_pairs = re.findall(
        r'(?:^|\s)color:\s*(#[0-9a-fA-F]{3,6})\b',
        html
    )
    bg_pairs = re.findall(
        r'background(?:-color)?:\s*(#[0-9a-fA-F]{3,6})\b',
        html
    )
    # Check each text color against white background (default)
    bg_default = '#ffffff'
    checked = set()
    for color in color_pairs:
        if color.lower() in checked:
            continue
        checked.add(color.lower())
        bg = bg_pairs[0] if bg_pairs else bg_default
        ratio = _contrast_ratio(color, bg)
        if ratio < 4.5:
            warnings.append(f"    Contraste {color}/{bg} : ratio {ratio:.1f}:1 < 4.5:1")

    # --- RGAA 5.1: data tables must have a caption (DSFR requirement) ---
    tables = re.findall(r'<table[^>]*>.*?</table>', html, re.DOTALL)
    tables_without_caption = []
    for idx, t in enumerate(tables, 1):
        if 'role="presentation"' not in t and '<caption>' not in t:
            # Extract first th content as hint
            th_m = re.search(r'<th[^>]*>([^<]+)</th>', t)
            hint = th_m.group(1).strip() if th_m else f'table {idx}'
            tables_without_caption.append(hint)
    if tables_without_caption:
        warnings.append(
            f"    RGAA 5.1 : {len(tables_without_caption)} tableau(x) de donnees sans caption "
            f"({', '.join(tables_without_caption)}). "
            f"Ajouter 'Table: titre' avant le tableau Markdown."
        )

    # --- RGAA 13.8: inaccessible content detection ---
    # Images without alt
    imgs_no_alt = re.findall(r'<img(?![^>]*\balt=)[^>]*>', html)
    if imgs_no_alt:
        warnings.append(f"    RGAA 13.8 : {len(imgs_no_alt)} image(s) sans attribut alt")

    # Iframes without title
    iframes_no_title = re.findall(r'<iframe(?![^>]*\btitle=)[^>]*>', html)
    if iframes_no_title:
        warnings.append(f"    RGAA 13.8 : {len(iframes_no_title)} iframe(s) sans attribut title")

    # --- Editorial checks (PRD-069) ---
    if _HAS_A11Y_EDITORIAL:
        # Strip technical blocks before editorial checks to avoid CSS/JS false positives.
        editorial_html = re.sub(
            r'<(style|script)\b[^>]*>.*?</\1>',
            ' ',
            html,
            flags=re.DOTALL | re.IGNORECASE,
        )
        plain_text = re.sub(r'<[^>]+>', ' ', editorial_html)

        acr = detect_acronymes(plain_text)
        if acr:
            warnings.append(f"    Acronymes non repertories : {acr}")

        _, cap_count = corriger_capitales(plain_text)
        if cap_count:
            warnings.append(f"    Capitales non accentuees : {cap_count} occurrence(s) (corrigees dans DOCX, warning seulement en PDF)")

        liens = detect_liens_generiques(editorial_html)
        if liens:
            warnings.append(f"    Liens generiques : {liens}")

        p_vides = detect_paragraphes_vides_html(editorial_html)
        if p_vides:
            warnings.append(f"    Paragraphes vides : lignes {p_vides}")

        # Justification CSS
        justify_matches = re.findall(r'text-align:\s*justify', html)
        if justify_matches:
            warnings.append(f"    Justification : {len(justify_matches)} occurrence(s) de text-align: justify")

    if warnings:
        print(f"\n  Audit a11y HTML — {len(warnings)} probleme(s) :")
        for w in warnings:
            print(w)
    else:
        print(f"  Audit a11y HTML : OK")

    return warnings


def escape_css_string(text):
    """Escape special characters for CSS content property."""
    return text.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')


def load_template(name):
    """Load a CSS template by name."""
    css_path = os.path.join(TEMPLATES_DIR, f'{name}.css')
    if not os.path.exists(css_path):
        available = [f.replace('.css', '') for f in os.listdir(TEMPLATES_DIR) if f.endswith('.css')]
        print(f"Template '{name}' introuvable. Disponibles : {', '.join(available)}")
        sys.exit(1)
    with open(css_path, 'r', encoding='utf-8') as f:
        return f.read()


def pandoc_to_html(md_path, html_path, title, subtitle, lang, toc_depth, no_toc):
    """Step 1: Convert Markdown to semantic HTML5 via Pandoc."""
    cmd = [
        'pandoc', md_path,
        '-f', 'markdown',
        '-t', 'html5',
        '--standalone',
        '--section-divs',
        '--no-highlight',
        '--metadata', f'lang={lang}',
    ]
    if title:
        cmd += ['--metadata', f'title={title}']
    if subtitle:
        cmd += ['--metadata', f'subtitle={subtitle}']
    if not no_toc:
        cmd += ['--toc', f'--toc-depth={toc_depth}']
    cmd += ['-o', html_path]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Erreur Pandoc: {result.stderr}")
        sys.exit(1)


def inject_css_and_a11y(html_path, css, lang, header_text, author=None, keywords=None,
                        logo=None, logo_alt=None):
    """Step 2: Inject CSS and accessibility attributes into the HTML."""
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace header text placeholder in CSS (with escaping)
    if header_text:
        css = css.replace('{{HEADER_TEXT}}', escape_css_string(header_text))
    else:
        css = css.replace('{{HEADER_TEXT}}', '')

    # Inject CSS
    style_block = f'<style>\n{css}\n</style>'
    html = html.replace('</head>', style_block + '\n</head>')

    # Inject logo after <body> (first page only, accessible)
    if logo and os.path.exists(logo):
        logo_abs = os.path.abspath(logo)
        alt = (logo_alt or '').replace('"', '&quot;')
        if not alt:
            print("  Attention : --logo sans --logo-alt, alt vide (violation PDF/UA-1 + WCAG 1.1.1)")
        logo_html = (
            f'<div style="margin-bottom:1.5em">'
            f'<img src="{logo_abs}" alt="{alt}" '
            f'style="max-width:80%;height:auto" role="img" />'
            f'</div>'
        )
        html = html.replace('<body>', f'<body>\n{logo_html}', 1)

    # Ensure lang attribute
    if f'lang="{lang}"' not in html:
        html = html.replace('<html', f'<html lang="{lang}"', 1)

    # Accessible TOC
    html = html.replace(
        '<nav id="TOC"',
        '<nav id="TOC" role="doc-toc" aria-label="Table des matières"'
    )

    # --- Table accessibility (RGAA thématique 5) ---

    # 1. Detect layout tables (no <thead>) and mark role="presentation"
    #    Also detect empty <thead> (all <th> empty) and remove it
    def fix_table(m):
        """Process each table for accessibility."""
        full_table = m.group(0)
        table_tag_m = re.match(r'<table[^>]*>', full_table)
        table_tag = table_tag_m.group(0) if table_tag_m else '<table>'

        thead_m = re.search(r'<thead>(.*?)</thead>', full_table, re.DOTALL)

        if thead_m:
            # Has <thead>: check if all <th> are empty
            th_contents = re.findall(r'<th[^>]*>(.*?)</th>', thead_m.group(1), re.DOTALL)
            if th_contents and all(c.strip() == '' for c in th_contents):
                # Empty thead → layout table: remove thead, add role
                new_tag = table_tag.replace('<table', '<table role="presentation"', 1)
                full_table = full_table.replace(table_tag, new_tag, 1)
                full_table = re.sub(r'<thead>.*?</thead>\s*', '', full_table, flags=re.DOTALL)
                return full_table
        else:
            # No <thead> at all → likely a layout table (e.g., metadata key-value)
            if 'role=' not in table_tag:
                new_tag = table_tag.replace('<table', '<table role="presentation"', 1)
                full_table = full_table.replace(table_tag, new_tag, 1)
            return full_table

        return full_table  # Data table with real headers: keep as-is

    html = re.sub(r'<table[^>]*>.*?</table>', fix_table, html, flags=re.DOTALL)

    # 2. Inject scope="col" on <th> in <thead> (column headers — RGAA 5.6)
    #    (?!ead) prevents matching <thead>
    html = re.sub(r'<th(?!ead)(?![^>]*scope=)', '<th scope="col"', html)

    # 3. Inject scope="row" on <th> in <tbody> (row headers — RGAA 5.6)
    def add_row_scope(m):
        tbody = m.group(0)
        tbody = re.sub(
            r'<th scope="col"(?=[^>]*>)',
            '<th scope="row"',
            tbody
        )
        return tbody

    html = re.sub(r'<tbody>.*?</tbody>', add_row_scope, html, flags=re.DOTALL)

    # Inject author/keywords metadata
    meta_tags = ''
    if author:
        escaped_author = author.replace('"', '&quot;')
        meta_tags += f'<meta name="author" content="{escaped_author}">\n'
    if keywords:
        escaped_kw = keywords.replace('"', '&quot;')
        meta_tags += f'<meta name="keywords" content="{escaped_kw}">\n'
    if meta_tags:
        html = html.replace('</head>', meta_tags + '</head>')

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)


def inject_figure_alt(pdf_path, logo_alt):
    """Post-process: tag untagged images as /Figure with /Alt (WeasyPrint limitation)."""
    python = find_python()
    script = f"""
import pikepdf

pdf = pikepdf.open({pdf_path!r}, allow_overwriting_input=True)
struct_root = pdf.Root.get('/StructTreeRoot')
if not struct_root:
    raise SystemExit('Pas de StructTreeRoot')

kids = struct_root.get('/K')

def has_figure(node):
    if isinstance(node, pikepdf.Array):
        return any(has_figure(item) for item in node)
    if isinstance(node, pikepdf.Dictionary):
        if str(node.get('/S', '')) == '/Figure':
            return True
        k = node.get('/K')
        return has_figure(k) if k is not None else False
    return False

def add_alt_to_figures(node):
    tagged = 0
    if isinstance(node, pikepdf.Array):
        for item in node:
            tagged += add_alt_to_figures(item)
    elif isinstance(node, pikepdf.Dictionary):
        if str(node.get('/S', '')) == '/Figure' and '/Alt' not in node:
            node['/Alt'] = pikepdf.String({logo_alt!r})
            tagged += 1
        k = node.get('/K')
        if k is not None:
            tagged += add_alt_to_figures(k)
    return tagged

if has_figure(kids):
    n = add_alt_to_figures(kids)
    print(f'  {{n}} /Figure balisee(s) avec /Alt')
else:
    # WeasyPrint n'a pas cree de /Figure — en creer une au debut
    doc_node = None
    if isinstance(kids, pikepdf.Dictionary) and str(kids.get('/S', '')) == '/Document':
        doc_node = kids
    elif isinstance(kids, pikepdf.Array):
        for item in kids:
            if isinstance(item, pikepdf.Dictionary) and str(item.get('/S', '')) == '/Document':
                doc_node = item
                break
    if doc_node and '/K' in doc_node:
        fig = pikepdf.Dictionary({{
            '/Type': pikepdf.Name('/StructElem'),
            '/S': pikepdf.Name('/Figure'),
            '/Alt': pikepdf.String({logo_alt!r}),
            '/P': doc_node,
        }})
        children = doc_node['/K']
        if isinstance(children, pikepdf.Array):
            children.insert(0, pdf.make_indirect(fig))
        else:
            doc_node['/K'] = pikepdf.Array([pdf.make_indirect(fig), children])
        print('  /Figure + /Alt injectee dans StructTreeRoot')
    else:
        print('  Avertissement: structure PDF incompatible, /Alt non injectee')

pdf.save({pdf_path!r})
"""
    result = subprocess.run(
        [python, '-c', script],
        capture_output=True, text=True, timeout=30
    )
    if result.returncode != 0:
        print(f"  Avertissement: injection /Figure echouee ({result.stderr.strip()})")
        return False
    if result.stdout.strip():
        print(result.stdout.strip())
    return True


def inject_pdf_metadata(pdf_path, lang, title=None, author=None, keywords=None):
    """Inject XMP metadata (language, title, author, keywords) into PDF."""
    python = find_python()

    # Build metadata assignments (single braces needed for XMP namespaces)
    DC = '{http://purl.org/dc/elements/1.1/}'
    PDF_NS = '{http://ns.adobe.com/pdf/1.3/}'
    meta_lines = [
        f"meta['{DC}language'] = {lang!r}",
    ]
    if title:
        meta_lines.append(f"meta['{DC}title'] = {title!r}")
    if author:
        meta_lines.append(f"meta['{DC}creator'] = [{author!r}]")
    if keywords:
        meta_lines.append(f"meta['{PDF_NS}Keywords'] = {keywords!r}")
    meta_block = '\n    '.join(meta_lines)

    script = f"""
import pikepdf
pdf = pikepdf.open({pdf_path!r}, allow_overwriting_input=True)
pdf.Root['/Lang'] = {lang!r}
with pdf.open_metadata(set_pikepdf_as_editor=False) as meta:
    {meta_block}
pdf.save({pdf_path!r})
"""
    result = subprocess.run(
        [python, '-c', script],
        capture_output=True, text=True, timeout=30
    )
    if result.returncode != 0:
        print(f"  Avertissement: injection XMP echouee ({result.stderr.strip()})")
        return False
    return True


def normalize_internal_links(pdf_path):
    """Resolve named internal link destinations to explicit PDF destinations.

    WeasyPrint keeps Pandoc TOC links as named destinations. Some PDF readers do
    not make those links clickable reliably. Explicit destinations are more
    robust and preserve external links untouched.
    """
    python = find_python()

    script = f"""
import pikepdf

pdf = pikepdf.open({pdf_path!r}, allow_overwriting_input=True)

def dest_name(value):
    if value is None:
        return None
    if isinstance(value, pikepdf.String):
        return str(value)
    if isinstance(value, pikepdf.Name):
        text = str(value)
        return text[1:] if text.startswith('/') else text
    if isinstance(value, str):
        return value[1:] if value.startswith('/') else value
    return None

def collect_names_tree(tree, out):
    if not isinstance(tree, pikepdf.Dictionary):
        return

    names = tree.get('/Names')
    if isinstance(names, pikepdf.Array):
        for idx in range(0, len(names) - 1, 2):
            name = dest_name(names[idx])
            dest = names[idx + 1]
            if isinstance(dest, pikepdf.Dictionary) and '/D' in dest:
                dest = dest['/D']
            if name and isinstance(dest, pikepdf.Array):
                out[name] = dest

    kids = tree.get('/Kids')
    if isinstance(kids, pikepdf.Array):
        for kid in kids:
            collect_names_tree(kid, out)

named_dests = {{}}
names_root = pdf.Root.get('/Names')
if isinstance(names_root, pikepdf.Dictionary):
    collect_names_tree(names_root.get('/Dests'), named_dests)

old_dests = pdf.Root.get('/Dests')
if isinstance(old_dests, pikepdf.Dictionary):
    for key, dest in old_dests.items():
        name = dest_name(key)
        if isinstance(dest, pikepdf.Dictionary) and '/D' in dest:
            dest = dest['/D']
        if name and isinstance(dest, pikepdf.Array):
            named_dests[name] = dest

converted = 0
for page in pdf.pages:
    annots = page.get('/Annots', [])
    for annot_ref in annots or []:
        annot = annot_ref.get_object() if hasattr(annot_ref, 'get_object') else annot_ref
        if not isinstance(annot, pikepdf.Dictionary):
            continue
        if str(annot.get('/Subtype')) != '/Link':
            continue

        dest = annot.get('/Dest')
        name = dest_name(dest)
        if name in named_dests:
            annot['/Dest'] = pikepdf.Array(named_dests[name])
            converted += 1
            continue

        action = annot.get('/A')
        if isinstance(action, pikepdf.Dictionary) and str(action.get('/S')) == '/GoTo':
            action_dest = action.get('/D')
            name = dest_name(action_dest)
            if name in named_dests:
                action['/D'] = pikepdf.Array(named_dests[name])
                converted += 1

if converted:
    pdf.save({pdf_path!r})
print(f'  {{converted}} lien(s) interne(s) normalise(s)')
"""
    result = subprocess.run(
        [python, '-c', script],
        capture_output=True, text=True, timeout=30
    )
    if result.returncode != 0:
        print(f"  Avertissement: normalisation des liens internes echouee ({result.stderr.strip()})")
        return False
    if result.stdout.strip():
        print(result.stdout.strip())
    return True


def weasyprint_to_pdf(html_path, pdf_path):
    """Step 3: Convert HTML to tagged PDF via WeasyPrint (PDF/UA-1)."""
    python = find_python()

    # Try PDF/UA-1 first
    script = f"""
import weasyprint
doc = weasyprint.HTML(filename={html_path!r})
doc.write_pdf({pdf_path!r}, pdf_variant='pdf/ua-1')
"""
    result = subprocess.run(
        [python, '-c', script],
        capture_output=True, text=True, timeout=600
    )

    if result.returncode != 0:
        # Fallback: standard PDF (still tagged, just not PDF/UA certified)
        print("  Fallback: PDF standard tagué (sans PDF/UA-1)...")
        script_fallback = f"""
import weasyprint
doc = weasyprint.HTML(filename={html_path!r})
doc.write_pdf({pdf_path!r})
"""
        result = subprocess.run(
            [python, '-c', script_fallback],
            capture_output=True, text=True, timeout=600
        )
        if result.returncode != 0:
            print(f"Erreur WeasyPrint: {result.stderr}")
            sys.exit(1)
        return False  # Not PDF/UA
    return True  # PDF/UA


def convert(md_path, output_path=None, title=None, subtitle=None, lang='fr',
            template='dsfr', toc_depth=2, no_toc=False, header_text=None,
            author=None, keywords=None, logo=None, logo_alt=None,
            page_total_footer=False):
    """Main conversion pipeline."""
    if not os.path.exists(md_path):
        print(f"Fichier introuvable: {md_path}")
        sys.exit(1)

    # Defaults
    if not output_path:
        output_path = os.path.splitext(md_path)[0] + '.pdf'

    auto_title, auto_subtitle = extract_title_from_md(md_path)
    if not title:
        title = auto_title
    if not subtitle:
        subtitle = auto_subtitle
    if not header_text:
        header_text = title or ''

    css = load_template(template)
    if page_total_footer:
        css += """

@page {
  @bottom-center {
    content: "Page " counter(page) " / " counter(pages);
  }
}
@page :first {
  @bottom-center {
    content: "Page " counter(page) " / " counter(pages);
  }
}
"""

    # Temp HTML file
    fd, html_path = tempfile.mkstemp(suffix='.html')
    os.close(fd)

    try:
        # Check alt-text before conversion
        warn_missing_alt_text(md_path)

        steps = 7 if logo else 6
        step = 0

        step += 1
        print(f"{step}/{steps} — Pandoc: Markdown → HTML5 sémantique...")
        pandoc_to_html(md_path, html_path, title, subtitle, lang, toc_depth, no_toc)

        step += 1
        print(f"{step}/{steps} — Injection CSS ({template}) + accessibilité...")
        inject_css_and_a11y(html_path, css, lang, header_text, author, keywords,
                            logo=logo, logo_alt=logo_alt)

        step += 1
        print(f"{step}/{steps} — Audit a11y HTML (contrastes WCAG + RGAA 13.8)...")
        audit_html_a11y(html_path)

        step += 1
        print(f"{step}/{steps} — WeasyPrint: HTML → PDF accessible...")
        is_ua = weasyprint_to_pdf(html_path, output_path)

        if logo and logo_alt:
            step += 1
            print(f"{step}/{steps} — Injection /Figure + /Alt (logo)...")
            inject_figure_alt(output_path, logo_alt)

        step += 1
        print(f"{step}/{steps} — Injection metadonnees XMP ({lang})...")
        inject_pdf_metadata(output_path, lang, title=title, author=author, keywords=keywords)

        step += 1
        print(f"{step}/{steps} — Normalisation des liens internes PDF...")
        normalize_internal_links(output_path)

        size = os.path.getsize(output_path)
        variant = "PDF/UA-1" if is_ua else "PDF tagué"
        print(f"\nPDF généré : {output_path}")
        print(f"  Taille : {size / 1024 / 1024:.1f} Mo")
        print(f"  Standard : {variant}")
        print(f"  Langue : {lang}")
        print(f"  Template : {template}")

    finally:
        if os.path.exists(html_path):
            os.remove(html_path)

    return output_path


def convert_via_docx(md_path, output_path=None, title=None, subtitle=None,
                     lang='fr', template='dsfr', author=None, keywords=None):
    """Alternative pipeline: Markdown → DOCX accessible → PDF via LibreOffice headless.

    Preserves heading hierarchy and TOC links for screen readers (unlike WeasyPrint).
    """
    if not os.path.exists(md_path):
        print(f"Fichier introuvable: {md_path}")
        sys.exit(1)

    if not os.path.exists(MD2DOCX_SCRIPT):
        print(f"Script md2docx.py introuvable: {MD2DOCX_SCRIPT}")
        sys.exit(1)

    if not os.path.exists(SOFFICE_PATH):
        print(f"LibreOffice introuvable: {SOFFICE_PATH}")
        print("  Installer: brew install --cask libreoffice")
        sys.exit(1)

    if not output_path:
        output_path = os.path.splitext(md_path)[0] + '.pdf'

    # Template mapping (formation n'existe pas en DOCX)
    docx_template = template
    DOCX_TEMPLATES = ['dsfr', 'default', 'minimal', 'rapport']
    if template not in DOCX_TEMPLATES:
        docx_template = 'default'
        print(f"  Avertissement: template '{template}' indisponible en DOCX, fallback vers 'default'")

    auto_title, auto_subtitle = extract_title_from_md(md_path)
    if not title:
        title = auto_title
    if not subtitle:
        subtitle = auto_subtitle

    # Step 1: Markdown → DOCX accessible
    fd, docx_path = tempfile.mkstemp(suffix='.docx')
    os.close(fd)

    try:
        print(f"1/4 — md2docx: Markdown → DOCX accessible ({docx_template})...")
        cmd_docx = [
            sys.executable, MD2DOCX_SCRIPT, md_path,
            '-o', docx_path,
            '--template', docx_template,
            '--lang', lang,
        ]
        if title:
            cmd_docx += ['--title', title]
        if author:
            cmd_docx += ['--author', author]
        if keywords:
            cmd_docx += ['--keywords', keywords]

        result = subprocess.run(cmd_docx, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            print(f"Erreur md2docx: {result.stderr}")
            sys.exit(1)

        # Step 2: DOCX → PDF via LibreOffice headless
        print(f"2/4 — LibreOffice: DOCX → PDF...")
        outdir = os.path.dirname(os.path.abspath(output_path))
        cmd_lo = [
            SOFFICE_PATH, '--headless', '--convert-to', 'pdf',
            '--outdir', outdir,
            docx_path,
        ]
        result = subprocess.run(cmd_lo, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            print(f"Erreur LibreOffice: {result.stderr}")
            sys.exit(1)

        # LibreOffice names output based on input filename
        lo_output = os.path.join(outdir, os.path.splitext(os.path.basename(docx_path))[0] + '.pdf')
        if os.path.exists(lo_output) and os.path.abspath(lo_output) != os.path.abspath(output_path):
            os.rename(lo_output, output_path)

        if not os.path.exists(output_path) or os.path.getsize(output_path) == 0:
            print("Erreur: PDF non genere par LibreOffice")
            sys.exit(1)

        # Step 3: Inject XMP metadata
        print(f"3/5 — Injection metadonnees XMP ({lang})...")
        inject_pdf_metadata(output_path, lang, title=title, author=author, keywords=keywords)

        # Step 4: Normalize internal links
        print(f"4/5 — Normalisation des liens internes PDF...")
        normalize_internal_links(output_path)

        # Step 5: Report
        size = os.path.getsize(output_path)
        print(f"\n5/5 — PDF genere via DOCX : {output_path}")
        print(f"  Taille : {size / 1024 / 1024:.1f} Mo")
        print(f"  Pipeline : Markdown → DOCX ({docx_template}) → PDF (LibreOffice)")
        print(f"  Langue : {lang}")
        print(f"  Accessibilite : titres et TOC preserves pour lecteurs d'ecran")

    finally:
        if os.path.exists(docx_path):
            os.remove(docx_path)

    return output_path


def main():
    parser = argparse.ArgumentParser(
        description='Convertir un Markdown en PDF accessible (PDF/UA-1)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  %(prog)s document.md
  %(prog)s document.md --title "Mon Titre" --template formation
  %(prog)s document.md -o sortie.pdf --lang fr --toc-depth 3
  %(prog)s --check
        """
    )
    parser.add_argument('input', nargs='?', help='Fichier Markdown source')
    parser.add_argument('-o', '--output', help='Chemin du PDF de sortie')
    parser.add_argument('--title', help='Titre du document')
    parser.add_argument('--subtitle', help='Sous-titre du document')
    parser.add_argument('--lang', default='fr', help='Langue du document (défaut: fr)')
    parser.add_argument('--template', default='dsfr',
                        help='Template CSS: dsfr, default, formation, rapport, minimal')
    parser.add_argument('--toc-depth', type=int, default=2,
                        help='Profondeur de la table des matières (défaut: 2)')
    parser.add_argument('--no-toc', action='store_true',
                        help='Désactiver la table des matières')
    parser.add_argument('--header-text', help='Texte de l\'en-tête courante')
    parser.add_argument('--author', help='Auteur du document (métadonnées PDF)')
    parser.add_argument('--keywords', help='Mots-clés du document (métadonnées PDF)')
    parser.add_argument('--logo', help='Image de bandeau/logo (chemin vers PNG/JPG/SVG)')
    parser.add_argument('--logo-alt', help='Texte alternatif du logo (obligatoire pour PDF/UA-1)')
    parser.add_argument('--page-total-footer', action='store_true',
                        help='Afficher « Page n / total » sur toutes les pages, couverture comprise')
    parser.add_argument('--via-docx', action='store_true',
                        help='Pipeline alternatif via DOCX accessible + LibreOffice (meilleure accessibilite lecteurs d\'ecran)')
    parser.add_argument('--check', action='store_true',
                        help='Vérifier les dépendances')

    args = parser.parse_args()

    if args.check:
        print("Vérification des dépendances :\n")
        ok = check_deps()
        print(f"\n{'Tout est OK.' if ok else 'Certaines dépendances manquent.'}")
        sys.exit(0 if ok else 1)

    if not args.input:
        parser.print_help()
        sys.exit(1)

    if args.via_docx:
        convert_via_docx(
            md_path=args.input,
            output_path=args.output,
            title=args.title,
            subtitle=args.subtitle,
            lang=args.lang,
            template=args.template,
            author=args.author,
            keywords=args.keywords,
        )
    else:
        convert(
            md_path=args.input,
            output_path=args.output,
            title=args.title,
            subtitle=args.subtitle,
            lang=args.lang,
            template=args.template,
            toc_depth=args.toc_depth,
            no_toc=args.no_toc,
            header_text=args.header_text,
            author=args.author,
            keywords=args.keywords,
            logo=args.logo,
            logo_alt=args.logo_alt,
            page_total_footer=args.page_total_footer,
        )


if __name__ == '__main__':
    main()
