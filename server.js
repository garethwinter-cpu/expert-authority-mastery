const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 8080;
const ROOT = __dirname;

// static assets (shared/wellness.css); html served by explicit routes below
app.use('/shared', express.static(path.resolve(ROOT, 'shared')));

const page = (file) => (req, res) => res.sendFile(path.resolve(ROOT, file));

app.get('/', page('index.html'));
app.get('/expert-authority', page('expert-authority.html'));
app.get('/ai-founders', page('ai-founders.html'));
app.get('/positioning', page('positioning.html'));

// legacy link from the first deploy of this repo
app.get('/proposal', (req, res) => res.redirect(301, '/expert-authority'));

app.get('/healthz', (req, res) => res.status(200).send('ok'));

app.listen(PORT, () => {
  console.log('Mastery Proposals running on port ' + PORT + ' from ' + ROOT);
});
