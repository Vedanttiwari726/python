const express = require('express')
const app = express();
const mongoose = require('mongoose')
require('dotenv').config()
const userRoute = require('../API/models/Routes/user')
const videoRoute = require('../API/models/Routes/video')
const bodyParser = require('body-parser')
const fileUpload=require('express-fileupload')


const ConnectWithDatabase=async()=>{
    try{
      const res  = await mongoose.connect(process.env.MONGO_URL)
      console.log('Connected with Database....')

    }
    catch(err){
        console.log(err)
    }
}
ConnectWithDatabase()
app.use(bodyParser.json())
app.use(fileUpload({
    useTempFiles : true,
   // tempFileDir : '/tmp/'
}));

app.use('/user',userRoute)
app.use('/video',videoRoute)
app.use(express.json())


module.exports = app;
