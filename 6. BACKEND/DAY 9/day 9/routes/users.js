var express = require('express');
var router = express.Router();

const path = require('path');


/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});
// router.use(express.static(path.join(__dirname, 'public')));

router.get('/file/:fName', function(req, res, next) {
  // console.log(__dirname + req.params.fName);
  res.sendFile(path.join(__dirname, '../public/images/'+req.params.fName))
})

module.exports = router;
