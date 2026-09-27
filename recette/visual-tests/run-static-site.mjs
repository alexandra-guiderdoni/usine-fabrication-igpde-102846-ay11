#!/usr/bin/env node

import { spawnSync } from "node:child_process";
import { existsSync, mkdirSync, readFileSync, readdirSync, statSync, writeFileSync } from "node:fs";
import path from "node:path";
import process from "node:process";

const rootDir = path.resolve(new URL("..", import.meta.url).pathname);
const siteDir = path.resolve(process.env.SHIPGUARD_SITE_DIR || path.join(rootDir, "..", "docs"));
const visualDir = path.join(rootDir, "visual-tests");
const resultsDir = path.join(visualDir, "_results");
const screenshotsDir = path.join(resultsDir, "screenshots");
const pagesDir = path.join(visualDir, "pages");
const sessionName = process.env.AGENT_BROWSER_SESSION || "shipguard-igpde-site";
const baseUrl = (process.argv[2] || process.env.SHIPGUARD_BASE_URL || "http://127.0.0.1:8765").replace(/\/$/, "");
const scopeDir = (process.argv[3] || process.env.SHIPGUARD_SCOPE || ".").replace(/^\.\/?/, "").replace(/\/$/, "") || ".";

mkdirSync(pagesDir, { recursive: true });
mkdirSync(screenshotsDir, { recursive: true });

function walk(dir, predicate, acc = []) {
  for (const entry of readdirSync(dir)) {
    if (entry === "visual-tests") continue;
    const full = path.join(dir, entry);
    const st = statSync(full);
    if (st.isDirectory()) {
      walk(full, predicate, acc);
    } else if (predicate(full)) {
      acc.push(full);
    }
  }
  return acc;
}

function rel(file) {
  const base = file.startsWith(siteDir + path.sep) ? siteDir : rootDir;
  return path.relative(base, file).replaceAll(path.sep, "/");
}

function slugify(value) {
  return value
    .replace(/\.html$/i, "")
    .replace(/\/index$/i, "/index")
    .replace(/[^a-zA-Z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .toLowerCase() || "index";
}

function yamlQuote(value) {
  return JSON.stringify(String(value));
}

function titleFromHtml(html, fallback) {
  const match = html.match(/<title[^>]*>([\s\S]*?)<\/title>/i);
  if (!match) return fallback;
  return match[1].replace(/\s+/g, " ").trim() || fallback;
}

function routeFromRel(relativePath) {
  if (relativePath === "index.html") return "/";
  if (relativePath.endsWith("/index.html")) return `/${relativePath.replace(/\/index\.html$/i, "/")}`;
  return `/${relativePath}`;
}

function manifestPathForPage(relativePath) {
  return path.join(pagesDir, `${slugify(relativePath)}.yaml`);
}

function screenshotName(relativePath) {
  return `${slugify(relativePath)}.png`;
}

function localTargetExists(fromFile, rawTarget) {
  if (!rawTarget || rawTarget.startsWith("#")) return null;
  if (/^(https?:|mailto:|tel:|sms:|data:|javascript:)/i.test(rawTarget)) return null;

  const cleanTarget = rawTarget.split("#")[0].split("?")[0];
  if (!cleanTarget) return null;

  const decoded = decodeURIComponent(cleanTarget);
  const targetPath = decoded.startsWith("/")
    ? path.join(siteDir, decoded)
    : path.resolve(path.dirname(fromFile), decoded);

  if (existsSync(targetPath)) return null;
  if (existsSync(path.join(targetPath, "index.html"))) return null;

  return rawTarget;
}

function scanLocalReferences(file, html) {
  const missing = [];
  const attrPattern = /\b(?:href|src|poster|action)=["']([^"']+)["']/gi;
  let match;
  while ((match = attrPattern.exec(html)) !== null) {
    const missingTarget = localTargetExists(file, match[1]);
    if (missingTarget) missing.push(missingTarget);
  }
  return [...new Set(missing)].sort();
}

function detectTags(html) {
  const tags = ["static-html"];
  if (/<form\b/i.test(html)) tags.push("form");
  if (/<video\b|<audio\b|<iframe\b/i.test(html)) tags.push("media");
  if (/<dialog\b/i.test(html)) tags.push("modal");
  if (/<button\b/i.test(html)) tags.push("interactive");
  return tags;
}

function writeConfig() {
  const configPath = path.join(visualDir, "_config.yaml");
  if (existsSync(configPath)) return;
  writeFileSync(
    configPath,
    [
      "# ShipGuard visual tests for the static Easy Check IGPDE site",
      `base_url: ${yamlQuote(baseUrl)}`,
      "credentials: {}",
      'screenshots_dir: "visual-tests/_results/screenshots"',
      'report_path: "visual-tests/_results/report.md"',
      'agent_browser_path: "agent-browser"',
      "build_command: null",
      "",
    ].join("\n"),
  );
}

function generateManifests(pages) {
  for (const page of pages) {
    const html = readFileSync(page, "utf8");
    const relativePath = rel(page);
    const route = routeFromRel(relativePath);
    const title = titleFromHtml(html, relativePath);
    const tags = detectTags(html);
    const manifest = [
      `name: ${yamlQuote(title)}`,
      `description: ${yamlQuote(`Auto-generated from ${relativePath}`)}`,
      "priority: medium",
      "requires_auth: false",
      "timeout: 30s",
      `tags: [${tags.map((tag) => yamlQuote(tag)).join(", ")}]`,
      "",
      "steps:",
      "  - action: open",
      `    url: ${yamlQuote(`{base_url}${route}`)}`,
      "  - action: screenshot",
      `    path: ${yamlQuote(`visual-tests/_results/screenshots/${screenshotName(relativePath)}`)}`,
      "  - action: llm-check",
      `    description: ${yamlQuote("Page loads and renders content")}`,
      `    criteria: ${yamlQuote("Visible content is present, the page is not blank, and no local resource appears broken.")}`,
      "    severity: critical",
      `    screenshot: ${yamlQuote(screenshotName(relativePath))}`,
      "",
    ].join("\n");
    writeFileSync(manifestPathForPage(relativePath), manifest);
  }
}

function runAgent(args, options = {}) {
  const result = spawnSync("agent-browser", ["--session", sessionName, ...args], {
    cwd: rootDir,
    encoding: "utf8",
    input: options.input,
    maxBuffer: 20 * 1024 * 1024,
  });
  if (result.status !== 0) {
    const detail = [result.stdout, result.stderr].filter(Boolean).join("\n").trim();
    throw new Error(`agent-browser ${args.join(" ")} failed${detail ? `\n${detail}` : ""}`);
  }
  return result.stdout.trim();
}

function tryAgent(args) {
  const result = spawnSync("agent-browser", ["--session", sessionName, ...args], {
    cwd: rootDir,
    encoding: "utf8",
    maxBuffer: 20 * 1024 * 1024,
  });
  return [result.status, [result.stdout, result.stderr].filter(Boolean).join("\n").trim()];
}

function parseEvalJson(output) {
  try {
    const parsed = JSON.parse(output);
    return typeof parsed === "string" ? JSON.parse(parsed) : parsed;
  } catch {
    // Fall through to substring parsing for agent-browser versions that wrap output.
  }

  const firstBrace = output.indexOf("{");
  const lastBrace = output.lastIndexOf("}");
  if (firstBrace === -1 || lastBrace === -1) {
    throw new Error(`Cannot parse eval JSON: ${output}`);
  }
  return JSON.parse(output.slice(firstBrace, lastBrace + 1));
}

function evaluatePage() {
  const script = `
(() => {
  const text = document.body ? document.body.innerText.trim() : "";
  const brokenImages = Array.from(document.images)
    .filter((img) => img.currentSrc && img.complete && img.naturalWidth === 0)
    .map((img) => img.getAttribute("src") || img.currentSrc);
  return JSON.stringify({
    title: document.title || "",
    h1Count: document.querySelectorAll("h1").length,
    textLength: text.length,
    brokenImages,
    forms: document.querySelectorAll("form").length,
    media: document.querySelectorAll("audio, video, iframe").length,
    dialogs: document.querySelectorAll("dialog").length
  });
})()
`;
  return parseEvalJson(runAgent(["eval", "--stdin"], { input: script }));
}

function normalizeErrors(output) {
  if (!output) return [];
  if (/no page errors|no errors|aucune erreur/i.test(output)) return [];
  return output.split("\n").map((line) => line.trim()).filter(Boolean);
}

function runVisualTests(pages) {
  const tests = [];
  tryAgent(["close"]);
  runAgent(["set", "viewport", "1440", "1000"]);

  for (const [index, page] of pages.entries()) {
    const started = Date.now();
    const relativePath = rel(page);
    const route = routeFromRel(relativePath);
    const id = `pages/${slugify(relativePath)}`;
    const manifest = rel(manifestPathForPage(relativePath));
    const screenshotRel = `visual-tests/_results/screenshots/${screenshotName(relativePath)}`;
    const screenshotAbs = path.join(rootDir, screenshotRel);
    const html = readFileSync(page, "utf8");
    const missingLocalTargets = scanLocalReferences(page, html);
    const failures = [];
    let pageInfo = null;
    let pageErrors = [];
    let status = "PASS";

    try {
      tryAgent(["errors", "--clear"]);
      runAgent(["open", `${baseUrl}${route}`]);
      const [waitStatus] = tryAgent(["wait", "--load", "networkidle"]);
      if (waitStatus !== 0) runAgent(["wait", "1000"]);

      const actualUrl = runAgent(["get", "url"]);
      if (!actualUrl.startsWith(`${baseUrl}${route}`.replace(/\/$/, ""))) {
        failures.push(`URL inattendue : ${actualUrl}`);
      }

      pageInfo = evaluatePage();
      pageErrors = normalizeErrors(tryAgent(["errors", "--clear"])[1]);

      if (pageInfo.textLength < 80) failures.push("contenu visible trop court ou page possiblement blanche");
      if (pageInfo.brokenImages.length > 0) failures.push(`images cassées : ${pageInfo.brokenImages.join(", ")}`);
      if (missingLocalTargets.length > 0) failures.push(`références locales introuvables : ${missingLocalTargets.join(", ")}`);
      if (pageErrors.length > 0) failures.push(`erreurs navigateur : ${pageErrors.slice(0, 3).join(" | ")}`);

      runAgent(["screenshot", "--full", screenshotAbs]);
      if (!existsSync(screenshotAbs) || statSync(screenshotAbs).size < 1024) {
        failures.push("capture absente ou vide");
      }
    } catch (error) {
      status = "ERROR";
      failures.push(error.message);
    }

    if (status !== "ERROR" && failures.length > 0) status = "FAIL";

    const durationMs = Date.now() - started;
    tests.push({
      id,
      manifest,
      name: titleFromHtml(html, relativePath),
      url: route,
      status,
      duration_ms: durationMs,
      screenshot: screenshotRel,
      failure_reason: failures.length ? failures.join("; ") : null,
      checks: {
        text_length: pageInfo?.textLength ?? null,
        h1_count: pageInfo?.h1Count ?? null,
        forms: pageInfo?.forms ?? null,
        media: pageInfo?.media ?? null,
        dialogs: pageInfo?.dialogs ?? null,
        missing_local_targets: missingLocalTargets,
        page_errors: pageErrors,
      },
    });

    console.log(`[sg-visual-run] Test ${index + 1}/${pages.length} - ${id} (${status})`);
  }

  tryAgent(["close"]);
  return tests;
}

function writeResults(tests) {
  const summary = {
    total: tests.length,
    pass: tests.filter((test) => test.status === "PASS").length,
    fail: tests.filter((test) => test.status === "FAIL").length,
    error: tests.filter((test) => test.status === "ERROR").length,
    stale: 0,
    skipped: 0,
    duration_ms: tests.reduce((sum, test) => sum + test.duration_ms, 0),
  };
  const results = {
    schema_version: "1.0",
    timestamp: new Date().toISOString(),
    base_url: baseUrl,
    summary,
    tests,
  };
  writeFileSync(path.join(resultsDir, "visual-results.json"), `${JSON.stringify(results, null, 2)}\n`);

  const failed = tests.filter((test) => test.status !== "PASS");
  const report = [
    "# Recette ShipGuard du site Easy Check IGPDE",
    "",
    `Date : ${new Date().toISOString()}`,
    `Base URL : ${baseUrl}`,
    "",
    "## Synthèse",
    "",
    `- Total : ${summary.total}`,
    `- Réussites : ${summary.pass}`,
    `- Échecs : ${summary.fail}`,
    `- Erreurs : ${summary.error}`,
    "",
    "## Échecs et erreurs",
    "",
    failed.length
      ? failed.map((test) => `- ${test.id} : ${test.failure_reason}`).join("\n")
      : "Aucun échec détecté sur les critères de livraison du site.",
    "",
    "## Toutes les pages",
    "",
    ...tests.map((test) => `- ${test.status} - ${test.id} - ${test.url}`),
    "",
    "## Limites",
    "",
    "- Les défauts d'accessibilité volontaires de `site-inaccessible/` ne sont pas comptés comme échecs.",
    "- La recette vérifie le chargement, les ressources locales, les erreurs navigateur et les captures complètes.",
    "- Les captures doivent être relues visuellement dans le tableau ShipGuard.",
    "",
  ].join("\n");
  writeFileSync(path.join(resultsDir, "report.md"), report);

  const regressions = failed.length
    ? ["regressions:", ...failed.map((test) => `  - id: ${yamlQuote(test.id)}\n    status: ${yamlQuote(test.status)}\n    failure_reason: ${yamlQuote(test.failure_reason)}`), ""].join("\n")
    : "regressions: []\n";
  writeFileSync(path.join(visualDir, "_regressions.yaml"), regressions);
  writeAuditResults(tests);

  return { summary, failed };
}

function sourceFileFromRoute(route) {
  if (route === "/") return "index.html";
  const routePath = route.replace(/^\//, "").replace(/\/$/, "/index.html");
  return routePath.endsWith(".html") ? routePath : `${routePath}.html`;
}

function lineForTargets(relativePath, targets) {
  const filePath = path.join(siteDir, relativePath);
  if (!existsSync(filePath)) return null;
  const lines = readFileSync(filePath, "utf8").split("\n");
  for (const target of targets) {
    const index = lines.findIndex((line) => line.includes(target));
    if (index !== -1) return index + 1;
  }
  return null;
}

function classifyAuditBug(test) {
  const missingTargets = test.checks?.missing_local_targets || [];
  const hasMedia = missingTargets.some((target) => /\.(mp4|mp3|webm|ogg|wav|m4a)(\?|#|$)/i.test(target));
  return {
    severity: hasMedia ? "high" : "medium",
    category: hasMedia ? "accessibility" : "infra",
  };
}

function buildAuditBug(test, index) {
  const missingTargets = test.checks?.missing_local_targets || [];
  const sourceFile = sourceFileFromRoute(test.url);
  const { severity, category } = classifyAuditBug(test);
  const targetLabel = missingTargets.length === 1
    ? missingTargets[0]
    : `${missingTargets.length} ressources locales`;

  return {
    id: `SG-SITE-${String(index + 1).padStart(3, "0")}`,
    severity,
    category,
    file: sourceFile,
    line: lineForTargets(sourceFile, missingTargets),
    title: `Ressource locale absente sur ${test.name}`,
    description: `La page référence ${targetLabel}, mais la ressource n'existe pas dans le site livré.`,
    recommendation: "Ajouter la ressource attendue dans `docs/assets/` ou adapter la source HTML vers un fichier réellement livré.",
    fix_applied: false,
    verified: true,
    verification_score: 95,
    evidence: "measured",
    impacted_ui_routes: [test.url],
  };
}

function writeAuditResults(tests) {
  const failedWithMissingTargets = tests.filter((test) => (test.checks?.missing_local_targets || []).length > 0);
  const bugs = failedWithMissingTargets.map(buildAuditBug);
  const bySeverity = { critical: 0, high: 0, medium: 0, low: 0 };
  const byCategory = {};

  for (const bug of bugs) {
    bySeverity[bug.severity] = (bySeverity[bug.severity] || 0) + 1;
    byCategory[bug.category] = (byCategory[bug.category] || 0) + 1;
  }

  const riskScore = Math.min(100, bySeverity.critical * 30 + bySeverity.high * 20 + bySeverity.medium * 10 + bySeverity.low * 3);
  const auditResults = {
    schema_version: "1.0",
    tool: "sg-code-audit",
    mode: "quick",
    scope: scopeDir,
    report_only: true,
    timestamp: new Date().toISOString(),
    summary: {
      total_bugs: bugs.length,
      by_severity: bySeverity,
      by_category: byCategory,
      files_audited: tests.length,
      files_modified: 0,
      risk_score: riskScore,
    },
    bugs,
    impacted_ui_routes: bugs.map((bug) => ({
      route: bug.impacted_ui_routes[0],
      bug_count: 1,
    })),
    agents: [
      {
        id: "static-site-assets",
        label: "Static site asset audit",
        status: "completed",
        bugs_found: bugs.length,
        paths: [`${scopeDir}/**/*.html`, "assets/"],
      },
    ],
  };

  writeFileSync(path.join(resultsDir, "audit-results.json"), `${JSON.stringify(auditResults, null, 2)}\n`);
}

function main() {
  const scanRoot = scopeDir === "." ? siteDir : path.join(siteDir, scopeDir);
  if (!existsSync(scanRoot) || !statSync(scanRoot).isDirectory()) {
    throw new Error(`Scope directory not found: ${scopeDir}`);
  }

  const pages = walk(scanRoot, (file) => file.endsWith(".html")).sort((a, b) => rel(a).localeCompare(rel(b), "fr"));
  if (pages.length === 0) {
    throw new Error(`No HTML page found in scope: ${scopeDir}`);
  }

  writeConfig();
  generateManifests(pages);
  const tests = runVisualTests(pages);
  const { summary, failed } = writeResults(tests);

  console.log(`[sg-visual-run] Summary: ${summary.pass}/${summary.total} PASS, ${summary.fail} FAIL, ${summary.error} ERROR`);
  if (failed.length) {
    for (const test of failed) console.log(`[sg-visual-run] ${test.status} ${test.id}: ${test.failure_reason}`);
    process.exitCode = 1;
  }
}

main();
