$(document).ready(function() {
    var url="http://127.0.0.1:8000/rentalsApi/";
    $.ajax({
        dataType:'json',
        url:url,
        success:function(datas){
            console.log(datas)
        }

    })


}

)