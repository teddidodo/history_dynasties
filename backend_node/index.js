require('dotenv').config();

const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const cors = require('cors');
const HttpError = require('./models/http-error');
const app = express();
const http = require('http');
const server = http.createServer(app);

const {default: mongoose} = require('mongoose');
const port = process.env.PORT || 4000;

const url = "MongoDB URL"

app.use(bodyParser.json());
app.use(cors());

const dynastiesRoutes = require('./routes/dynasties-routes');
app.use('/dynasties', dynastiesRoutes);

const eventsRoutes = require('./routes/events-routes');
app.use('/events', eventsRoutes);

app.get('/', (req, res) => {
  console.log('This is main page!');
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.use((req, res, next) => {
  const error = new HttpError('Could not find this route.', 404);
  throw error;
});

app.use((req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  // eslint-disable-next-line max-len
  res.setHeader('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, Authorization');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  next();
});

app.use((error, req, res, next) => {
  if (res.headerSent) {
    return next(error);
  }
  res.status(error.code || 500);
  res.json({message: error.message || 'Unknown error occurred!'});
});

mongoose
    .connect(url)
    .then(() => {
      server.listen(port, () => {
        console.log(`Server is running at port ${port}`);
      });
    })
    .catch((error) => {
      console.log(error);
    });


module.exports = server;
