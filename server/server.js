const express = require('express')

const app = express()
const port = 3000

app.get('/', (req, res) => {
    var randomNumber = Math.round(Math.random())
    data = {"randomNumber": randomNumber}
    res.send(data)
})

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`)
})