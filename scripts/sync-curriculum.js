#!/usr/bin/env node
// Refresh data/curriculum.json and covers/ from Airtable. Needs AIRTABLE_TOKEN.
//   AIRTABLE_TOKEN=pat... node scripts/sync-curriculum.js
const fs = require('fs');
const path = require('path');
const { fetchLive } = require('../lib/curriculum');
const ROOT = path.resolve(__dirname, '..');
const slug = (t) => String(t).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 70);
(async () => {
  if (!process.env.AIRTABLE_TOKEN) { console.error('AIRTABLE_TOKEN is required'); process.exit(1); }
  const data = await fetchLive();
  fs.mkdirSync(path.resolve(ROOT, 'covers'), { recursive: true });
  for (const s of data.sessions) {
    if (!s.cover) continue;
    const file = 'covers/' + slug(s.title) + '.jpg';
    const res = await fetch(s.cover);
    if (res.ok) { fs.writeFileSync(path.resolve(ROOT, file), Buffer.from(await res.arrayBuffer())); s.cover = file; }
  }
  data.mode = 'snapshot';
  fs.writeFileSync(path.resolve(ROOT, 'data', 'curriculum.json'), JSON.stringify(data, null, 1));
  console.log('wrote data/curriculum.json with ' + data.sessions.length + ' sessions');
})();
