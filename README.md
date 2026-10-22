# Portfolio Forge

**A portfolio creator for game makers — By Gopinath.**

Create a responsive portfolio from sections, grids, and components. Everything you create is saved as editable configuration when you export your website.

## Start here

1. Extract this entire ZIP. Keep its files and `vendor` folder together.
2. Open **index.html** in a current desktop Chrome or Edge browser. There is no installation or build step.
3. Choose a blank canvas or a role-based starter.
4. Add sections, split their grids, and place components.
5. Check your portfolio in **Browse** mode at desktop, tablet, and mobile widths.
6. Click **Export website**. The downloaded ZIP is your finished static website, with readable config files and all your uploaded assets.
7. To publish, extract that exported website ZIP and upload its contents to your static host. The `index.html` must be at your hosting root. Upload the exported portfolio, not this creator, if you want visitors to see your portfolio.

You can also host this creator itself as a static site. It requires neither accounts nor a server database. Opening it locally is sufficient; browser storage availability can vary in private browsing or restricted environments, so keep exported ZIP backups.

## How to build

### Sections first

- **Fit:** fills the viewport after the top navigation. If your content cannot fit, it grows to keep text accessible.
- **Flexible:** choose a minimum section height in rem.
- **Infinite:** add as many subsections as needed. Each subsection can grow to fit content or use a minimum rem/viewport height.
- **Projects:** a category bar or filter sidebar and a collection of cards. Categories can also be hidden.
- **Content panel:** a separate canvas that opens from a button near the bottom of the screen.
- **Project page:** created automatically with a project card. It uses the same infinite subsection builder.

Section display names must be unique. Asset roots and exported section IDs are stable when you rename a section.

### Split the space

Select an empty grid cell, then choose **Cell layout → Split this cell**. Choose rows or columns and enter 2–4 positive percentages totaling 100, such as `30, 70` or `10, 40, 50`.

You can nest up to three split levels. Each leaf cell holds one component; a list counts as one component. Splitting an occupied cell moves its component into the first child cell. Select a parent from the section’s layout hierarchy to adjust its proportions later.

Columns stack in reading order on small screens. Use the nine-position alignment selector, Fit component to cell, padding, and gap to control placement. Measurements use rem, with viewport percentages available for subsection height. A rem follows the browser's base font size, normally 16px; the layout rules provide the responsiveness.

### Place and edit components

Drag a component from the left palette into an empty cell. You can also select the cell and click the component. Select a placed component for its floating formatting toolbar and collapsible inspector. Double-click plain text in the preview to type directly.

The floating toolbar remains inside the preview and scrolls horizontally if needed. Its move handle lets you move a component to another empty cell. Collapse the sidebar or inspector to give the preview more room.

Components include text, buttons, images, video, galleries, code snippets, Sketchfab viewers, contact forms, dropdowns, lists, dividers, and spacers. Every component has a visibility switch. Lists support text, buttons, dropdowns, images, and images with captions. Shared item appearance applies to new list items; use an individual override when one item needs different styling.

In infinite sections, project pages and content panels, **Add a layout preset** creates an editable image breakdown, paired-image comparison, video with notes, code walkthrough, model viewer, or profile/skills layout. These are normal grids and components after insertion.

### Appearance and backgrounds

Website settings control the global font, background, text, accent, navigation, contact dock, and footer. Components can override font and appearance. Project headings, card text, category navigation and subsection titles have their own appearance controls.

Backgrounds have separate base, image/video, and overlay layers. A one-color array is solid; multiple colors create a gradient with your chosen angle. Image and overlay opacity are independent. Optional edge fading blends the image into a chosen page color.

Background videos are muted and respect reduced-motion preferences. Standard local video components have controls; YouTube embeds load after clicking Play. Galleries support images and video, captions, arrow navigation, and image enlargement.

### Projects and categories

Add a Projects section, create categories, then add cards. A card can belong to several categories. Choose category buttons, a checkbox filter sidebar, or no category UI. Set card counts separately for desktop, tablet, and mobile; choose visible details or a hover reveal design.

A card can open a full project page, replace the cards inline, or open an external URL. When you add another card, choose whether to copy a previous project's page layout. Copies have independent settings and initially reuse the same asset paths.

Project pages support category and subcategory navigation tied to their subsections, with an optional sticky bar. Subsections can be collapsible and initially expanded or collapsed. Code blocks provide a file name, language label, line numbers, selected-line highlights, wrapping, vertical scrolling, and an explanation below.

### Links, pop-up panels, and downloads

Buttons and dropdown options can:

1. Scroll to a section.
2. Open a content panel.
3. Close the current panel.
4. Open a link or document in a new tab.
5. Download a file.

Content panels have their own backgrounds, subsections, grids, and components. They can close on scroll and have a built-in close control. Opening another panel replaces the current one. Local downloadable files are most reliable; remote servers can override the browser's download behavior.

### Assets stay organized

Each section has protected roots:

```
assets/<section-id>/images/
assets/<section-id>/videos/
assets/<section-id>/documents/
assets/<section-id>/models/
```

Upload through Asset library and create subfolders as needed. Choose an asset from any section to reuse it. Dropping files directly onto a cell first asks where to store them. Duplicate filenames get a numeric suffix. Referenced files cannot be deleted until you remove their references. Removing a section or card keeps its uploaded assets available.

Original files are preserved; the creator does not reduce image quality or silently transcode video. Compress large media before uploading. Lazy images, deferred embeds, and metadata-only video loading reduce unnecessary loading, but no site can promise instant media on every connection.

For an interactive 3D model, link a public **Sketchfab** model. FBX/GLB/other source files can be stored in Models and offered for download. This release does not render raw FBX files locally.

## Save, reopen, and publish

- Local drafts save in this browser on this device. **Save draft** also saves explicitly.
- **Export website** is your portable backup and publishing package.
- **Open ZIP** reads a Portfolio Forge website export, including its edited configurations and assets. This creator does not analyze/import arbitrary third-party sites; that belongs to the separate Portfolio Studio editor.
- **Ctrl+Z / Cmd+Z** undo; **Ctrl+Y / Cmd+Shift+Z** redo. Inputs keep their normal text-editing undo while focused.
- Editor dark/light mode is independent of your portfolio’s theme. Dark is the initial editor theme.

Your exported website includes its own README explaining manual configuration edits and hosting. All user content lives in `config/site.js` and `config/sections/*.js`, not in the HTML shell. Config objects are JSON-compatible JavaScript assignments with readable names and indentation.

## Contact forms and external services

No hidden email service or account is supplied. Without an endpoint, contact forms open an email composer or Gmail and clearly say they have not sent mail themselves. You may add a compatible HTTPS form endpoint, then test its delivery and cross-origin policy on your host. Never put secret API keys into a public config.

YouTube and Sketchfab need internet access and publicly accessible content. Third-party playback, embedding permissions, mail delivery, and browser privacy settings remain outside the creator’s control.

## Files in this creator

`index.html` is the creator shell; `editor.css` and `app.js` provide the editor; `model.js` defines configuration and validation; `runtime.js` and `site.css` render portfolios; `resources.js` includes the same runtime and CSS for local preview/export; `vendor` contains JSZip and its license. If you change runtime.js or site.css, run `python build.py` to refresh resources.js before packaging.

See **TEST-REPORT.md** for completed verification and the scope of testing. The `verification` folder contains reproducible model and browser test harnesses. Tests use isolated draft storage and synthetic project data.
