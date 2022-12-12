const express = require('express');
const eventsController = require('../controllers/events-controller');
// eslint-disable-next-line new-cap
const router = express.Router();

router.get('/', eventsController.getEvents);
router.get('/:dynasty', eventsController.getEventsByDynasty);
module.exports = router;
