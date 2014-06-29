'use strict';

var ab = function(exp_name, id_user){
    var self = this;
    self.sorteioURI = 'http://localhost:8001/api/experimento/' + exp_name + '/user/?id=' + id_user;
    self.sorteio = '';
};

ab.prototype.getSorteio = function(){
    var self = this;
    var request = new XMLHttpRequest();
    request.onload = function(){
        self.sorteio = this.responseText;
    };
    request.open('get', self.sorteioURI, true);
    request.send();    
};

module.exports.ab = ab;
