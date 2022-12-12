/* eslint-disable new-cap */
const HttpError = require('../models/http-error');
const Dynasty = require('../models/dynasties-model');

// GET REQUESTS
const getDynasties = async (req, res, next) => {
  let dynasties;
  try {
    dynasties = await Dynasty.find();
  } catch (error) {
    return next(
        new HttpError('Could not find any dynasty', 500),
    );
  }

  return res.status(200)
      .json({
        dynasties: dynasties.map(
            (request) => request.toObject({getters: true})),
      });
};

const getRandomDynasties = async (req, res, next) => {
  let dynasty;
  const random_number = Math.floor(Math.random() * 8) + 0;

  try {
    dynasty = await Dynasty.findById(random_number);
  } catch (error) {
    return next(
        new HttpError('Could not find any dynasty', 500),
    );
  }

  return res.status(200).json({
    dynasty
  });
};

const getDynastyByName = async (req, res, next) => {
  const dynasty_name = req.params.dynasty;

  if (!dynasty_name) {
    return next(
      new HttpError('Could not find any parameter', 404),
    );
  }

  dynasty_name = dynasty_name.toLowerCase()
  let dynasty;
  
  try {
    dynasty = await Dynasty.find({name: dynasty_name})
  } catch (error) {
    return next(
        new HttpError('Could not find any dynasty', 500),
    );
  }
  
  if (!dynasty) {
    return next(
        new HttpError('Could not find any dynasty with this name', 404),
    );
  }

  return res.status(200).json({dynasty: dynasty.toObject({getters: true})});
};

exports.getDynasties = getDynasties;
exports.getRandomDynasties = getRandomDynasties;
exports.getDynastyByName = getDynastyByName;
