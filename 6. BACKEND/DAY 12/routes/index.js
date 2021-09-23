var express = require('express');
var router = express.Router();

const { registerChecks } = require('../middlewares/registerChecks');
const register = require('../controllers/register');

/* GET home page. */
router.get('/', function(req, res, next) {
  const sess = req.session;
  sess.username = 'abhay';
  
  res.render('index', { title: 'Express' });
});


/* For register */
router.post('/register', registerChecks, register)


module.exports = router;
