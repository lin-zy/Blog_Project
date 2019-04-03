/**
 * Created by Yang on 2019/4/1.
 */
$(function(){
    var num = 0
    $.ajax({
        url:'http://127.0.0.1:8000/Serializers_Posts',
        type:get,
        dataType:'jsonp',
        beforeSend:function(){
            $('#load_more').innerText="加载中"

        },
        success:function(data){
            $('#load_more').html('加载更多')
            if(data.list ==null){
                $('#load_more').html("暂无更多数据");
                $('#load_more').attr('disabled',true);
                return false
            }
            if(data.allnum <= num){
                 $('#load_more').html("暂无更多数据");
                $('#load_more').attr('disabled',true);
            }
            var html ='';
            for(var i = 0;i<data.list.length;i++){
                html +='<div class="page-header "><h1 style="font-family: 黑体 ;display: inline" ><a href="" style="text-decoration: none;">{{ post.title }} </a></h1> <i class="glyphicon glyphicon-eye-open "  style="display:inline;margin-left: 2px;"></i>&nbsp;&nbsp;<i class="glyphicon glyphicon-tag "  style="display:inline;"></i>&nbsp;<a href="}">{{ post.category }}</a>&nbsp;<i class="glyphicon glyphicon-time "  style="display:inline;"></i>&nbsp;{{ post.created_time|date:"Y-m-d" }}</div> <figure class="highlight"> <span class="c1"><b class="lead">{{ post.body|truncatechars:200|safe }}</b></span> <a href="">查看更多</a> </figure>'
            }
            $('.highlight').append(html)
            isNum = data.allnum

        }





    })
})