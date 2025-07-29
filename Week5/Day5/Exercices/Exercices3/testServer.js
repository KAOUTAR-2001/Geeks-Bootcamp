import express from 'express';

const app = express();
const port = 5000;

console.log('✅ testServer.js loaded');

app.get('/test', (req, res) => {
  console.log('✅ Test route hit');
  res.send('Test route working!');
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});