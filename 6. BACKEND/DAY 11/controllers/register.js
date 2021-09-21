const User = require('../models/user');
const bcrypt = require ('bcrypt');
/**
 * 
 * to interact with databse 
 */
const saltRounds = 10;
const register = async(req, res) => {
    const {email,password} = req.body;
    try{
        const alreadyExists = await User.findOne({where : {email: email}});
        if(alreadyExists){
            res.status(401).send('Email Already Exists');
            next();
        }
        //if valid then next
        // use hashing for password
        const salt = bcrypt.genSaltSync(saltRounds);
        const hash = bcrypt.hashSync(password,salt); 
        
        const newUser = new User({email : email.toLowerCase(), password : hash})
        const SavedUser = await newUser.save();
        res.status(201).send(SavedUser);
    }
    catch(err){
        console.error(err);
        res.send(500).send('Something went wrong');
    }
}

module.exports = register;