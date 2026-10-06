const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 8080;
const ROOT = __dirname;

// static assets (shared/wellness.css); html served by explicit routes below
app.use('/shared', express.static(path.resolve(ROOT, 'shared')));
app.use('/authors', express.static(path.resolve(ROOT, 'authors'), { maxAge: '7d' }));

const page = (file) => (req, res) => res.sendFile(path.resolve(ROOT, file));

// Expert & Authority curriculum: rendered from Airtable (lib/curriculum.js) on every request.
const curriculum = require('./lib/curriculum');
const fs = require('fs');
const TEMPLATE = path.resolve(ROOT, 'expert-authority.html');
const safeJson = (obj) => JSON.stringify(obj).replace(/</g, '\\u003c').replace(/\u2028/g, '\\u2028').replace(/\u2029/g, '\\u2029');
app.use('/covers', express.static(path.resolve(ROOT, 'covers'), { maxAge: '1d' }));
app.get('/expert-authority', async (req, res) => {
  const data = await curriculum.load();
  const html = fs.readFileSync(TEMPLATE, 'utf8').replace('__CURRICULUM_JSON__', safeJson(data));
  res.set('Cache-Control', 'no-cache').type('html').send(html);
});
app.get('/api/curriculum', async (req, res) => {
  res.set('Cache-Control', 'no-cache').json(await curriculum.load());
});

app.get('/', page('index.html'));
// earlier curriculum drafts (v1 to v5 and the comparison) were retired on 23 September 2026;
// their links land on the live curriculum
['/expert-authority-v2', '/expert-authority-v3', '/expert-authority-v4', '/expert-authority-v5', '/expert-authority-compare']
  .forEach((r) => app.get(r, (req, res) => res.redirect(301, '/expert-authority')));
app.get('/accelerator-edit-script', page('expert-authority-accelerator-script.html'));
// AI for Founders: /ai-founders is the front door, /ai-founders/curriculum the dated draft. Both render
// data/ai-founders-curriculum.json, held in the repo until aligned with Vishen, so they can never disagree.
const AIF_DATA = path.resolve(ROOT, 'data', 'ai-founders-curriculum.json');
const aifPage = (file) => (req, res) => {
  const data = JSON.parse(fs.readFileSync(AIF_DATA, 'utf8'));
  const html = fs.readFileSync(path.resolve(ROOT, file), 'utf8').replace('__CURRICULUM_JSON__', safeJson(data));
  res.set('Cache-Control', 'no-cache').type('html').send(html);
};
// AI for Founders icon: blue square, "Ai"
['favicon-aif.svg', 'favicon-aif-32.png', 'favicon-aif-512.png', 'apple-touch-icon-aif.png']
  .forEach((f) => app.get('/' + f, (req, res) => res.set('Cache-Control', 'public, max-age=86400').sendFile(path.resolve(ROOT, f))));
app.get('/ai-founders', aifPage('ai-founders-home.html'));
app.get('/ai-founders/curriculum', aifPage('ai-founders.html'));
app.get('/api/ai-founders', (req, res) => res.set('Cache-Control', 'no-cache').json(JSON.parse(fs.readFileSync(AIF_DATA, 'utf8'))));
// AI for Founders lives under /ai-founders/* so it reads as its own product next to Expert & Authority
app.get('/ai-founders/proposal', page('ai-founders-proposal.html'));
app.get('/ai-founders/guild', page('ai-founders-guild.html'));
app.get('/ai-founders-proposal', (req, res) => res.redirect(301, '/ai-founders/proposal'));
app.get('/ai-founders-guild', (req, res) => res.redirect(301, '/ai-founders/guild'));
app.get('/ai-founders-proposal/:tab', (req, res) => res.redirect(301, '/ai-founders/proposal#' + encodeURIComponent(req.params.tab)));
// deep links shared from the August page, when the proposal lived at /ai-founders
['programme', 'programme-w5', 'authors'].forEach((t) => app.get('/ai-founders/' + t, (req, res) => res.redirect(301, '/ai-founders/proposal#' + t)));
app.get('/positioning', page('positioning.html'));
app.get('/expert-authority-guild', page('expert-authority-guild.html'));
app.get('/ai-founders-guild', page('ai-founders-guild.html'));

// legacy link from the first deploy of this repo
app.get('/proposal', (req, res) => res.redirect(301, '/expert-authority'));

// note: /healthz is intercepted by Google's frontend on Cloud Run and never
// reaches the container - use /health for uptime checks
app.get('/health', (req, res) => res.status(200).send('ok'));

app.listen(PORT, () => {
  console.log('Mastery Proposals running on port ' + PORT + ' from ' + ROOT);
});
