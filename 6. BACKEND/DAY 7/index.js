const app = require('express')();

app.get('/',(req,res) => {
    res.send('oK');
})

app.get('/user/:id',(req,res) => {
    res.send(req.params.id)
})

app.get('/feed?limit=20', (req, res) => {
    res.send(req.query.limit)
})

app.listen(5000);