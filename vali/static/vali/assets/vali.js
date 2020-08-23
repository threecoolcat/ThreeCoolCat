(function () {
    $('[data-toggle="sidebar"]').click(function(event) {
        if ($('.object-tools').hasClass('object-tools-mr')){
            $('.object-tools').animate({'margin-right': '3%'});
        }else{
            $('.object-tools').animate({'margin-right': '16%'});
        }
        $('.object-tools').toggleClass('object-tools-mr');
    });
    if ($('.vali-multicheckbox').length > 0){
        //handle permission's help text , hide <p>
        $('.related-widget-wrapper').parent().addClass('col').removeClass('col-7').next().hide();
        // ul
        $('.vali-multicheckbox').each(function(){
            // if the label's text is seprate appname | modelname | permission
            var is_perm_label = false;
            var inputs = {};
            // li
            $(this).children().each(function(){
                var lbl = $(this).find('label');
                if (lbl.length > 0){
                    var txts = lbl.text().trim().split('|');
                    // app | model | permission
                    if (txts.length  == 3){
                        is_perm_label = true;
                        var appname = txts[0].trim();
                        var modelname = txts[1].trim();
                        var permission = txts[2].trim();
                        var perm_html = '<div class="animated-checkbox"><label>'+lbl.find('input').prop('outerHTML')+'<span class="label-text">'+permission+'</span></label></div>';
                        if (appname in inputs){
                            if (modelname in inputs[appname]){
                                inputs[appname][modelname].push(perm_html);
                            }else{
                                inputs[appname][modelname] = [perm_html];
                            }
                        }else{
                            inputs[appname] = {};
                            inputs[appname][modelname] = [perm_html];
                        }
                    }
                }
            });
            if (is_perm_label){
                // rebuild lines appname | model | permissions for add change delete
                var html = "";
                for (var key in inputs) {
                    html += '<li class="list-group-item list-group-item-action"><div class="row"><span class="col-2">'
                    +key+'</span><div class="col">';
                    var counter = 0;
                    for (var mkey in inputs[key]){
                        if (counter == Object.keys(inputs[key]).length -1){
                            html += '<div class="row px-0"><span class="col-2">'+mkey+'</span>';
                        }else{
                            html += '<div class="row px-0 line-head mr-1 mb-1"><span class="col-2">'+mkey+'</span>';
                        }
                        inputs[key][mkey].sort();
                        for (var inputkey in inputs[key][mkey]){
                            html += '<div class="col">'+ inputs[key][mkey][inputkey]+'</div>';
                        }
                        html += '</div>';
                        counter += 1;
                    }
                    html += '</div></div></li>';
                }
                $(this).children().remove();
                $(this).html(html);
            }else{
                $(this).children().addClass('list-group-item');
            }
        });
    }
})();