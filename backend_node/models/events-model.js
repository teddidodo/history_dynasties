const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const eventSchema = new Schema({
  dynasty_id: {type: mongoose.Types.ObjectId, required: true, ref: 'Dynasty'},
  year: {type: String, required: true},
  period: {type: String, required: true},
  description: {type: String, required: true},
});

module.exports = mongoose.model('Event', eventSchema);
