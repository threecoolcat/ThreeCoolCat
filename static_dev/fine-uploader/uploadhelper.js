var upload_finish = true;
var uploadhelper = {
    /**
    * 保存文件url的元素ID，用于上传成功后回写数据
    field_name 字段名
    restype 资源类型，widget中指定
    initial 初始数据调用的url, 返回数据的格式参考fineuploader 例  [{uuid:, name:, thumbnailUrl:}]
    multiple 是否允许上传多个文件
    disabled 控件是否可操作， =true时， 按钮不可见，区域不可接受对象
    */
    config: function(field_name, restype, initial, multiple=false, disabled=false){
        var rootpath = '/common';
        var static_url = '/static';
        var version = "5.14.1";
        var imgUploader = new qq.FineUploader({
            element: document.getElementById('uploader-'+field_name),
            template: 'qq-template',
            sizeLimit: 268435436,
            debug: true,
            autoUpload: true,
            debug: false,
            multiple: multiple,
            validation: {
                allowedExtensions: ['jpeg', 'jpg', 'png', 'pdf', 'dcm', 'doc', 'docx']
            },
            request: {
                endpoint: rootpath+'/upload/file/'+restype+'/'
            },
            deleteFile:{
                endpoint: rootpath+'/upload/delete/'+restype,
                enabled:true
            },
            session:{
                endpoint: initial,
                refreshOnReset:true
            },
            callbacks:{
                onComplete:function(id, name ,response, xhr){
                    if (response.code == 0){
                        if (multiple){
                            //多个文件时，生成多个input,记录文件名，并增加文件个数
                            $("#"+field_name+"_count").val(id);
                            $("#id_"+field_name).after('<input type="hidden" id="file_'+field_name+id+'" name="file_'+field_name+id+'" value="'+response.data+'"/>')
                            .after('<input type="hidden" id="name_'+field_name+id+'" name="name_'+field_name+id+'" value="'+name+'"/>');
                        }else{
                            //单个文件上传的， 直接写到本控件ID的input中
                            $("#id_"+field_name).val(response.data);
                        }
                    }
                },
                onSubmit:function(id, name){
                    //var ups = this.getUploads();
                    if (disabled) {
                        return false;
                    }
                    //判断重复文件
                },
                onSessionRequestComplete: function(response, success,xhrOrXdr){
                    if (success){
                        if (response.length > 0){
                            if (response[0].type == "image"){
                            }else{
                                $("#attachments_"+response[0].type+"_count").val(response.length-1);
                                for (var i=0;i<response.length;i++){
                                    var field_name = "attachments_"+response[i].type;
                                    $("#id_"+field_name)
                                    .after('<input type="hidden" id="file_'+field_name+i+'" name="file_'+field_name+i+'" value="'+response[i].thumbnailUrl+'"/>')
                                    .after('<input type="hidden" id="name_'+field_name+i+'" name="name_'+field_name+i+'" value="'+response[i].name+'"/>')
                                }
                            }
                            if (disabled){
                                $(".qq-upload-button").remove();
                                $(".qq-upload-delete").remove();
                                $('.qq-uploader').attr('qq-drop-area-text', '');
                            }
                        }
                    }
                },
                onPasteReceived:function(blob){
                    upload_finish = false;
                },
                onAllComplete:function(succeed, failed){
                    upload_finish = true;
                },
                onDelete: function(id){
                     return true;
                },
                onSubmitDelete: function(id){

                },
                onDeleteComplete: function(id, xhr, isError){
                    var resp = JSON.parse(xhr.response);
                    if (resp.type == 'emr' || resp.type == 'pacs' || resp.type =='lis' || resp.type == 'other'){
                        $("#file_attachments_"+resp.type+id).remove();
                        $("#name_attachments_"+resp.type+id).remove();
                    }else{
                        $("#id_"+field_name).val("");
                    }
                }
            },
            thumbnails: {
                placeholders: {
                    waitingPath: static_url + '/fine-uploader/'+version+'/placeholders/waiting-generic.png',
//                    notAvailablePath:static_url + '/fine-uploader/'+version+'/placeholders/not_available-generic.png'
                    notAvailablePath:static_url + '/images/doc.png'
                }
            }
        });
        if (disabled){
            $(".qq-upload-button").remove();
            $(".qq-upload-delete").remove();
            $('.qq-uploader').attr('qq-drop-area-text', '');
        }
    },

    preview: function(img){
        var fileid = $(img).parent().attr('qq-file-id');
        var compid = $(img).parent().parent().parent().parent().attr("id")
        var ids = compid.split('_');
        if (ids.length == 2){
            var url = '';
            var type = ids[1];
            url = $('#file_attachments_'+type+fileid).val();
            if (url.substr(-3) == 'pdf'){
                //pdf使用pdf.js预览
                window.open('/static/pdf.js/web/viewer.html?file='+url, 'pdf文档', 'height='+(window.innerHeight-100)+',width='+window.innerWidth+',top=200,left=200,toolbar=no,menubar=no,scrollbars=no, resizable=yes,location=no, status=no');
            }else if (url.substr(-3) == 'dcm'){
                //dcm使用 cornerstone预览
                window.open('/static/cornerstone/index.html?url='+url,'DICOM影像', 'height='+(window.innerHeight-100)+',width='+window.innerWidth+',top=200,left=200,toolbar=no,menubar=no,scrollbars=no, resizable=yes,location=no, status=no');
            }else if (url.substr(-3) == 'jpg' || url.substr(-3) == 'png' || url.substr(-4) == 'jpeg'){
                //图片使用新窗口预览
                window.open(url, '图片', 'height='+(window.innerHeight-100)+',width='+window.innerWidth+',top=200,left=200,toolbar=no,menubar=no,scrollbars=no, resizable=yes,location=no, status=no');
            }else if (url.substr(-3) == 'doc' || url.substr(-4) == 'docx'){
                //word文档，下载到本地预览
                window.location.href = url;
            }

        }
    }
}
