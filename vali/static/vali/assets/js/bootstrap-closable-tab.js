/**
https://github.com/zyqwst/bootstrap-closable-tab
*/
var closableTab = {
    frameHeight: 400,
	//frame加载完成后设置父容器的高度，使iframe页面与父页面无缝对接
	frameLoad:function (frame){
       // $(frame).parent().height($("#content").height() -40);
	},
    //添加tab
	addTab:function(tabItem, change_callback){ //tabItem = {id,name,url,closable}  change_callback在标签更改时执行
		//function change_callback(self){};
		var id = "tab_seed_" + tabItem.id;
		var container ="tab_container_" + tabItem.id;
		$(".nav-link").removeClass("active").attr("aria-expanded", false);
		$(".tab-pane").removeClass("active").removeClass("show").attr("aria-expanded", false);
		var needloadtab = false;
		if(!$('#'+id)[0]){
			var li_tab = '<li class="nav-item" style="margin-left:1px" id="'+id+'"><a href="#'+container+'" class="nav-link active" aria-expanded="true" data-toggle="tab" style="position: relative">'+tabItem.name;
			if(tabItem.closable){
				li_tab = li_tab + '<i class="fa fa-window-close" tabclose="'+id+'" style="margin-left:8px;margin-top:-4px;margin-right:-4px"  onclick="closableTab.closeTab(this)"></i></a></li> ';
			}else{
				li_tab = li_tab + '</a></li>';
			}
			$('.nav-tabs').append(li_tab);
			needloadtab = true;
		}
		if (tabItem.reload){
		    $("#"+container).remove();
		    needloadtab = true;
		}
		if (needloadtab){
            var tabpanel = '<div role="tabpanel" class="tab-pane active show" aria-expanded="true" id="'+container+'" style="width: 100%;height:100%">'+
                                  '<iframe src="'+tabItem.url+'" id="tab_frame_'+tabItem.id+'" frameborder="0" style="overflow-x: hidden; overflow-y: hidden;width:100%;" height="'+($("#content").height() - 40)+'"  onload="closableTab.frameLoad(this)"></iframe>'+
                               '</div>';
            $('.tab-content').append(tabpanel);
		}else{
		    $("#"+id).children().addClass("active").attr("aria-expanded", true);
		    $("#"+container).addClass("active").addClass("show").attr("aria-expanded", true);
		}
        $(".tab-content").css({'margin-top': $('.nav-tabs').height()});
		if (change_callback){
		    change_callback($("#"+id));
		}
		$("#"+id).click(function(){
            if (change_callback){
                change_callback($("#"+id));
            }
		});
	},
	//关闭tab
	closeTab:function(item){
		var val = $(item).attr('tabclose');
		var containerId = "tab_container_"+val.substring(9);
   	    if($('#'+containerId).hasClass('active')){
   	        if ($('#'+val).prev().length > 0){
   	            $('#'+val).prev().children().addClass('active');
   	    	    $('#'+containerId).prev().addClass("active").addClass("show");
   	        }else if ($('#'+val).next().length > 0){
                $('#'+val).next().children().addClass('active');
                $('#'+containerId).next().addClass("active").addClass("show");
   	        }
   	    }
		$("#"+val).remove();
		$("#"+containerId).remove();
		$(".tab-content").css({'margin-top': $('.nav-tabs').height()});
	}
}


function addTab(id, name , url, canClose, reload=false){
    closableTab.addTab({'id':id,'name':name,'url':url,'closable':canClose, 'reload':reload}, null);
};
// todo: need add this method
function closeTab(item) {
    closableTab.closeTab(item);
}