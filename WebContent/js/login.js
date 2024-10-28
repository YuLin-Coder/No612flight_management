
function login()
{
    var Username = document.getElementById("User");
    var Email = document.getElementById("Email");
    var pass = document.getElementById("Password");

    if(Username.value == ''){
        alert("请输入用户名！");
    }else if(Email.value==''){
        alert("请输入邮箱地址！");
    }else{
        alert("请输入密码！")
    }



}