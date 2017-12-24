$(function(){
    $('#accunt').blur(function(){
        //失去焦点时获取输入框中的内容
        var account = $(this).val()
        //向服务器发送数据进行验证
        $.getJSON('/checkaccount/', {'account': account}, function(data){
            if(data['state'] == 200){
                $('#account_check').css('color', '#00ff00');
            }else if (data['state'] == 201){
                $('#account_check').css('color', '#ff0000');
            }
            $('#account_check').html(data['msg'])
        })
    })

    $('#passwd').blur(function(){
        var pwd = $('#pass').val()
        var pwdc = $('#passwd').val()
        $.getJSON('/checkpassword/', {'pwd': pwd, 'pwdc': pwdc}, function(data){
            if(data['state'] == 200){
                $('#password_check').css('color', '#00ff00')
            }else if (data['state'] == 201){
                $('#password_check').css('color', '#ff0000')
            }
            $('#password_check').html(data['msg'])
        })
    })

    $('#uname').blur(function(){
        //失去焦点时获取输入框中的内容
        var username = $(this).val()
        //向服务器发送数据进行验证
        $.getJSON('/checkusername/', {'username': username}, function(data){
            if(data['state'] == 200){
                $('#username_check').css('color', '#00ff00');
            }else if (data['state'] == 201){
                $('#username_check').css('color', '#ff0000');
            }
            $('#username_check').html(data['msg'])
        })
    })
})


//注册信息校验函数
function check(){
    var account = $('#accunt').val()
    var pwd = $('#pass').val()
    var pwdc = $('#passwd').val()
    var username = $('#uname').val()

    var bl
    $.ajaxSettings.async = false
    $.getJSON('/checkaccount/', {'account': account}, function(data){
        if(data['state'] == 200){
            $.getJSON('/checkpassword/', {'pwd': pwd, 'pwdc': pwdc}, function(data){
                if(data['state'] == 200){
                    $.getJSON('/checkusername/', {'username': username}, function(data){
                        if(data['state'] == 200){
                            bl = true
                        }else{
                            alert('用户名格式不正确')
                            bl = false
                        }
                    })
                }else{
                    alert('密码不符合要求')
                    bl = false
                }
            })
        }else{
            alert('账号格式不正确')
            bl = false
        }
    })
    $.ajaxSettings.async = true
    return bl
}
