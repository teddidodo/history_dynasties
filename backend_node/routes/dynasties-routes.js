const express = require('express');
const dynastiesController = require('../controllers/dynasties-controller');
// eslint-disable-next-line new-cap
const router = express.Router();

router.get('/', dynastiesController.getDynasties);
router.get('/random/dynasty', dynastiesController.getRandomDynasties);
router.get('/:dynasty', dynastiesController.getDynastyByName);

module.exports = router;
