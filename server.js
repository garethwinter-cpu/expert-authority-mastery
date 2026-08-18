const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 8080;
const ROOT = __dirname;

app.use(express.static(ROOT, { extensions: ['html'] }));

app.get('/', (req, res) => {
  res.sendFile(path.resolve(ROOT, 'index.html'));
});

app.get('/proposal', (req, res) => {
  res.sendFile(path.resolve(ROOT, 'index.html'));
});

app.get('/healthz', (req, res) => res.status(200).send('ok'));

app.listen(PORT, () => {
  console.log('Expert & Authority Mastery proposal running on port ' + PORT + ' from ' + ROOT);
});
