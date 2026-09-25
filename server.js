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
// AI for Founders: the dated draft curriculum, held in data/ai-founders-curriculum.json until aligned with Vishen
const AIF_TEMPLATE = path.resolve(ROOT, 'ai-founders.html');
const AIF_DATA = path.resolve(ROOT, 'data', 'ai-founders-curriculum.json');
app.get('/ai-founders', (req, res) => {
  const data = JSON.parse(fs.readFileSync(AIF_DATA, 'utf8'));
  const html = fs.readFileSync(AIF_TEMPLATE, 'utf8').replace('__CURRICULUM_JSON__', safeJson(data));
  res.set('Cache-Control', 'no-cache').type('html').send(html);
});
app.get('/api/ai-founders', (req, res) => res.set('Cache-Control', 'no-cache').json(JSON.parse(fs.readFileSync(AIF_DATA, 'utf8'))));
// the August proposal (case, summit plan, evidence) stays readable at its own route
app.get('/ai-founders-proposal', page('ai-founders-proposal.html'));
app.get('/ai-founders-proposal/:tab', (req, res) => res.redirect(302, '/ai-founders-proposal#' + encodeURIComponent(req.params.tab)));
app.get('/ai-founders/:tab', (req, res) => res.redirect(301, '/ai-founders-proposal#' + encodeURIComponent(req.params.tab)));
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
