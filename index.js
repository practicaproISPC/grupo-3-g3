const express = require('express')
const app = express()
const port = 3000
// app.get('/', (req, res) => {
//     res.send('Hello World!')
// })
// app.listen(port, () => {
//     console.log(`Example app listening at http://localhost:${port}`)
// })


app.use('/static', express.static(__dirname + '/public'));

var PORT = process.env.PORT || 3000;
app.listen(PORT, function () {
    console.log('Example app listening on port 3000! or ' + PORT);
});