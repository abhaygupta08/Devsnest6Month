const {DataTypes} = require('sequelize');
const sequelize = require('../database/index.js');

const User = sequelize.define('User',{
 
    fullName : {
        type : DataTypes.STRING,
        allowedNull : false
    },
    email : {
        type : DataTypes.STRING,
        allowedNull : false
    },
    password : {
        type : DataTypes.STRING,
        allowedNull : false
    }

});

module.exports = User;