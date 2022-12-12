/* eslint-disable max-len */
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const dynastySchema = new Schema({
  name: {type: String, required: true},
  start_year: {type: String, required: true},
  end_year: {type: String, required: true},
  house: {type: String, required: true},
  current_country: {type: String, required: false},
  country: {type: String, required: false},
});

module.exports = mongoose.model('Dynasty', dynastySchema);
