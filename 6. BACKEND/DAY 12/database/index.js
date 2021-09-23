const {Sequelize} = require('sequelize');

/** 
 * 
 * database user name
 * database name
 * password
 * host 
 * dialect postgres mysql 
 * */

const sequelize = new Sequelize(
    "postgres",
    "postgres",
    "",
    {
        host : "localhost",
        dialect : "postgres"
    }
);

sequelize.sync();
(async () => {
    try{
        await sequelize.authenticate();
        console.log('Connection established with dB');
    }
    catch(err){
        console.error('Error connecting to dB');
    }
})();

module.exports = sequelize;