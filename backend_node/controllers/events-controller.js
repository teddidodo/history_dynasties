const HttpError = require('../models/http-error');
const Dynasty = require('../models/dynasties-model');
const Event = require('../models/events-model');

const getEventsByDynasty = async (req, res, next) => {
  let events;
  let dynasty_name = req.params.dynasty;

  if (!dynasty_name) {
    return next(
      new HttpError('Could not find dynasty', 400),
    );
  }

  dynasty_name = dynasty_name.toLowerCase();
  let dynasty;
  try {
    dynasty = await Dynasty.find({name: dynasty_name})
    if (!dynasty) {
      return next(
        new HttpError('Could not find dynasty', 400),
      );
    }
  } catch (error) {
    return next(
        new HttpError('Could not find any dynasty', 500),
    );
  }

  try {
    events = await Event.find({dynasty_id: dynasty._id}).populate('dynasty');
  } catch (error) {
    return next(
        new HttpError('Could not find any event', 500),
    );
  }
  const period_dict = new Map();

  events.forEach((event) => {
    if (!period_dict.has(element.period)) {
      period_dict.set(element.period, [event])
    } else {
      period_dict.get(element.period).push(event)
    }
  })        
  
  return res.status(200).json({period_dict});
};

const getEvents = async (req, res, next) => {
  let events;
  try {
    events = await Event.find().populate("dynasty");
  } catch (error) {
    return next(
        new HttpError('Could not find an event', 500),
    );
  }
  return res.status(200).json({events});
};

exports.getEventsByDynasty = getEventsByDynasty;
exports.getEvents = getEvents;
