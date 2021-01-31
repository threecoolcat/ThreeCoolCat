(function () {
	"use strict";

	var treeviewMenu = $('.app-menu');

	// Toggle Sidebar
	$('[data-toggle="sidebar"]').click(function(event) {
		event.preventDefault();
		$('.app').toggleClass('sidenav-toggled');
	});

	// Activate sidebar treeview toggle
	$("[data-toggle='treeview']").click(function(event) {
		event.preventDefault();
		if(!$(this).parent().hasClass('is-expanded')) {
			//treeviewMenu.find("[data-toggle='treeview']").parent().removeClass('is-expanded');
		}
		$(this).parent().toggleClass('is-expanded');
	});

	// Set initial active toggle
	$("[data-toggle='treeview.'].is-expanded").parent().toggleClass('is-expanded');

	//Activate bootstrip tooltips
	$("[data-toggle='tooltip']").tooltip();
    $('.nav-tabs').width($('#pages').width()-17);
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
function setCookie(c_name,value,expiredays)
{
    var exdate=new Date();
    exdate.setDate(exdate.getDate()+expiredays);
    document.cookie=c_name+ "=" +escape(value)+((expiredays==null) ? "" : ";expires="+exdate.toGMTString());
};
function getCookie(c_name)
{
    if (document.cookie.length>0)
    {
        c_start=document.cookie.indexOf(c_name + "=");
        if (c_start!=-1)
        {
            c_start=c_start + c_name.length+1;
            c_end=document.cookie.indexOf(";",c_start);
            if (c_end==-1) c_end=document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
};
function bodyscroll(){
    var activeframes = $(".tab-pane.active iframe");
    var tp = document.body.scrollTop;
    if (activeframes.length == 1) {

        var content = activeframes[0].contentDocument;
        var apptitle = content.getElementsByClassName("app-title");
        var wintool = content.getElementsByClassName("formtoolbox");
        $(apptitle).css("top", tp+"px");
        $(wintool).css("top", tp+"px");
    }
};

function addTab(id, name , url, canClose, reload=false){
    closableTab.addTab({'id':id,'name':name,'url':url,'closable':canClose, 'reload':reload}, null);
};
// todo: need add this method
function closeTab(item) {
    closableTab.closeTab(item);
}