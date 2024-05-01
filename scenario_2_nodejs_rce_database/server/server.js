var express = require('express');
var cookieParser = require('cookie-parser');
var escape = require('escape-html');
var serialize = require('node-serialize');
var mysql = require('mysql');
var app = express();

// Set up MySQL connection
var con = mysql.createConnection({
    host: "mysql-service",
    user: "user",
    password: "veryweakpassword", // Use the intentionally insecure password
    database: "rcedb"
});

con.connect(function(err) {
    if (err) {
        console.error('Error connecting to MySQL: ' + err.stack);
        return;
    }
    console.log('Connected to MySQL as ID ' + con.threadId);
});

app.use(cookieParser())

app.get('/', function (req, res) {
    if (req.cookies.profile) {
        var str = new Buffer(req.cookies.profile, 'base64').toString();
        var obj = serialize.unserialize(str);
        if (obj.username) {
            // Display username and make a simple MySQL query to fetch some data
            con.query('SELECT info FROM person WHERE lastname = ?', [obj.lastname], (err, result) => {
                if (err) {
                    res.send("Error fetching user data!");
                } else {
                    var userData = result.length ? result[0].info : "No additional info";
                    res.send("Hello " + escape(obj.username) + ". " + userData);
                }
            });
        } else {
            res.send("Hello World");
        }
    } else {
        res.cookie('profile', "eyJ1c2VybmFtZSI6ImFqaW4iLCJjb3VudHJ5IjoiaW5kaWEiLCJjaXR5IjoiYmFuZ2Fsb3JlIn0=", {
            maxAge: 900000,
            httpOnly: true
        });
        res.send("Hello World");
    }
});

app.listen(4242, () => {
    console.log(`Server is running on http://localhost:4242`);
});

