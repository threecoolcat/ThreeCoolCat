/**
* 更新课程状态，
* 因为django的安全机制， 需要传入csrftoken
* 也可以在settings.py中关闭 MIDDLEWARE 下的 'django.middleware.csrf.CsrfViewMiddleware',就可以不传这个参数
*/
function update(id, status) {
    var msg = ''
    if (status == 1) {
        msg = '是否要上架该课程'
    } else {
        msg = '是否要下架该课程'
    }
    if (window.confirm(msg) == true) {
        $.ajax({
            url: '/school/api/courses/',
            type:"POST",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({id: id, status: status}),
            headers:{ "X-CSRFtoken":$.cookie("csrftoken")},
            success:function (res) {
                // 请求成功后，刷新当前页面
//                window.location.reload()
                console.log(res)
            }
        })
    }
}