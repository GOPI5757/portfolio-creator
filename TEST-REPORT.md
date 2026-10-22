# Verification report

Portfolio Forge · 23 October 2026

## Automated results

**85 checks passed; 0 failed in the final runs.**

- **30 model checks:** four role starters, configuration validity, percentage splits, depth cap, occupied cells, page cloning with independent IDs, stable asset paths, path traversal rejection, duplicate IDs, serialization, unique generated IDs, and 100 randomized weighted layouts.
- **34 runtime/browser checks:** complete rendering, initial viewport fit, responsive project grids, category buttons, multi-select filters, inline and full-page project routes, back navigation, collapsed subsections, category scrolling, code wrapping and vertical scrolling, highlighted lines, galleries/lightboxes, pop-up open/close, URL parsing, contact form validation, all component types, shared/individual list styles, alignment and fit, long content, disabled sections, and column lists.
- **21 creator workflow checks:** initial theme, blank creation, section wizard, invalid/valid split input, placement/move event handling, occupied-cell protection, inspector and inline text updates, undo/redo keyboard events, list overrides, project-page creation and copying, layout presets, upload destination flow, media decoding, theme/panel toggles, bounded mobile preview, document integrity, export content, ZIP re-import, and persisted draft restoration.

Portfolio rendering was checked at **320, 390, 768, 1280, and 1920 pixels** wide. The creator workflow harness used a desktop frame and verified that the mobile preview remains inside its available workspace.

## Interactive checks

Using the browser UI, verification covered choosing a starter, selecting and directly editing text, editing inspector fields, creating a project/category mapping, creating a weighted custom grid, inserting a component, choosing preview sizes, uploading and selecting an actual image, opening a project in Browse mode, exporting a ZIP, and reopening that same ZIP.

The downloaded ZIP was independently opened and checked from disk. It had separate section configs, the uploaded SVG was byte-identical to its source, and profile content was stored in configuration rather than HTML. JavaScript syntax checks passed for the model, creator, and runtime.

Issues found and fixed during testing included text changes not promptly reaching the preview, selection clicks being interrupted by inline-edit refresh, uploaded Blob media failing inside the preview frame, stale inspector scroll positions, and control contrast.

## Test boundaries

- The browser’s URL policy permits HTTP/HTTPS only. It blocked the direct `file://` launch test. Browser verification used localhost; direct file launch in desktop Chrome/Edge was not interactively verified here. The application uses classic local scripts and bundled resources rather than module imports or fetch-based startup.
- The browser automation could not perform a physical drag across its scaled iframe surface. Drag/drop event handling, component placement, moving components, and file-drop destination handling were covered by automated browser event tests. The click-to-place alternative was checked interactively. This is not a claim of physical drag testing on every browser or touch device.
- Tests use local synthetic images and project data. YouTube/Sketchfab URL handling was tested; playback restrictions, remote availability, private models, and network performance are controlled by those services.
- No real contact message was sent. Form validation and the honest email-composer fallback were tested. A custom sending endpoint must be tested with its actual service after configuration.
- Media is preserved, not silently compressed or transcoded. Large archives can exceed a browser's available memory or storage. Imports have a 1 GB extracted asset limit; practical limits may be lower on some devices.
- Verification does not establish that no possible browser, media file, content combination, or user-selected color scheme can expose a bug. Test the portfolio you create before publishing it.

## Reproduce

Run `node verification/model.test.js` for model checks. To run browser checks, serve this folder locally (`python -m http.server 8792`), then open:

- `http://localhost:8792/verification/harness.html`
- `http://localhost:8792/verification/editor-harness.html`

The pages show each assertion and the final totals. Workflow tests use a separate draft database and synthetic data. Normal creator drafts remain in their regular database.
