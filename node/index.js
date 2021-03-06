var ghRequest = require('request');
var fs = require('fs');
var _ = require('lodash');
var test = false;
var util = require('util');

var ghOptions = {
    url: 'https://api.github.com/repos/stedolan/jq/commits?per_page=50',
    headers: {
        'User-Agent': 'request'
    }
};

function handleNetworkResponse(err, body, callback) {
    if(err) {return callback(err); }
    var same = _.filter(body, function(val) {
        return val.commit.author.name === val.commit.committer.name
    });
    var shas = _.map(same, function(val) {
        return val.sha;
    })
    console.log(util.inspect(shas, { showHidden: true, depth: null }));
    return callback(null, shas);
}

function makeRequest(ghOptions, callback) {
    if (test) {
        //read in file
        return fs.readFile('./data/commits.json', 'utf8', function (err, str) {
            if(err) {return callback(err); }

            handleNetworkResponse(null, JSON.parse(str), callback);
        });
    } else {
        return ghRequest(ghOptions, function (err, resp, body) {
            if(err) { return callback(err); }

            handleNetworkResponse(null, JSON.parse(body), callback);

        })
    }

}

exports.handler = function(event, context, callback) {
    makeRequest(ghOptions, callback);

    // Use callback() and return information to the caller.
}
