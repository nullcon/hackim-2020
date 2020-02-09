const express = require('express')
var proxy = require('express-http-proxy');
var url = require('url');
var bodyParser = require('body-parser')
var dns = require('dns');
dnsPromises = dns.promises;
var request = require('request');
var rp = require('request-promise');



const app = express()
const port = 3000


function getProxy(){
 console.log("Proxy: "+proxy)
 return proxy;
}


// support parsing of application/json type post data
app.use(bodyParser.json());

//support parsing of application/x-www-form-urlencoded post data
app.use(bodyParser.urlencoded({ extended: true }));

app.use(express.static('public'));

app.all('/api/1/', function(req,res,next){
  res.send("Need a tenant");
});

app.all('/api/1/:id',function(req, res, next){
   proxy=req.header('X-Tunnel-To');
   url2=req.url;
   if(proxy){
     Gproxy=proxy;
    if(!url.parse(proxy).protocol)
     proxy = "http://"+proxy
    proxyParse=url.parse(proxy)
    //console.log(proxyParse)
    const blacklists = ["127","local","::",":","http://0/","0.0.0.0","file","/"];
    for(blacklist in blacklists){
	if (Gproxy.toString().includes(blacklists[blacklist])){
                //console.log(blacklists[blacklist])
		res.send('Not permitted!');
		return
	}
    }

   const ips=["127.0.0.1","169.254.169.254","169","127","192","168"]
    //console.log(proxyParse.hostname)


    async function test(host) {
      let data = await dnsPromises.lookup(host);
      return data;
    }
    test(proxyParse.hostname).then(function(result) {
     //console.log(result)
     addresses=result.address;
      if(result.family!=4){
         res.send('Only Ipv4 allowed');
         return
       }
    //console.log(addresses);
    if(addresses){
      for(blacklist in ips){
        if (addresses.toString().includes(ips[blacklist])){
                //console.log(ips[blacklist])
                res.send('So smart, But still Internal not permitted!');
                return next();
        }
       }
     }


    proxyPath = proxyParse.path;
    req.url="/proxyDontBrute8123123/"+req.params.id;
    next();
    }).catch(function (err){
        res.send(err)
     });
   }
   else{
    res.send("No need of bruteforce!");
   }
});


app.use('/proxyDontBrute8123123', proxy(getProxy,{
  proxyReqPathResolver(req) {
        const reqPath = url.parse(url2).path;
        return proxyPath+reqPath;
    },
   timeout: 2000,
  userResDecorator: function(proxyRes, proxyResData, userReq, userRes) {
    if(proxyRes.statusCode==303){
     symbol=Object.getOwnPropertySymbols(userRes)
     data=userRes[symbol[3]]
     location=data.location[1]
      ProxyRedirect=location;
      body=rp(ProxyRedirect)
       .then(function (htmlString) {
         return htmlString
      })
      .catch(function (err) {
        return err
       });
      return body;
     }
    else{
     return proxyResData;
    }
  },

  userResHeaderDecorator(headers, userReq, userRes, proxyReq, proxyRes) {
    if(userRes.statusCode==303){
      userRes.statusCode=200;
    }
    return headers;
  },



}),);


app.listen(port, () => console.log(`Example app listening on port ${port}!`))

