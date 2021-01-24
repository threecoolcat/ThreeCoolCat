(function(){
var inputs = document.getElementsByTagName('input');
for (var i = 0; i < inputs.length; i++) {
    var inp = inputs[i];
    if (inp.getAttribute('type') === 'text' && inp.className.match(/vTimeField/)) {
        laydate({elem: '#'+inp.id,  format: 'hh-mm-ss', });
    }else if (inp.getAttribute('type') === 'text' && inp.className.match(/vDateField/)) {
        laydate({elem: '#'+inp.id,  format: 'YYYY-MM-DD', });
    }
}
})();
