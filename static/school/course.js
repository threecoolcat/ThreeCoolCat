function update(id, status) {
$.ajax({
    url: '/school/api/courses/',
    type:"POST",
    contentType: "application/json",
    dataType: "json",
    data: JSON.stringify({id: id, status: status}),
    headers:{ "X-CSRFtoken":$.cookie("csrftoken")},
    success:function (res) {
        console.log(res)
    }
})

}