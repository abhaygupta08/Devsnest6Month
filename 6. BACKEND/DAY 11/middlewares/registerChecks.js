/*
For email and password validations
*/

const {emailValidator, passwordValidator} = require('../utils/validations');

const registerChecks = (req, res,next) => {
    const {email,password,confirmPassword} = req.body;
    if (typeof (email) === 'string' && typeof (password) === 'string' && typeof (confirmPassword) === 'string' && email.length > 0 && password.length >= 8 && confirmPassword == password && emailValidator(email) && passwordValidator(password)) {
        next();
    }
    else{
        res.status(401).send('Initial Checks failed');
    }
}

module.exports = {registerChecks};