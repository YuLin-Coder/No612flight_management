<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>


<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <meta name="description" content="">
    <meta name="author" content="">

    <title>小giao兔飞机订票系统</title>


    


    <link href="css/login.css" rel="stylesheet">

    <script src="js/ie-emulation-modes-warning.js"></script>


  </head>

  <body>
  <img alt="" src="img/bg.png" class="wave">

    <div class="container">
    
      <div class="img">
      	<img alt="" src="img/img-3.svg">
      </div>
      <div class="login-box">
  <form method="post" action="servlet/LoginServlet">
    <c:if test="${sessionScope.loginMsg!=null}">
      <div class="alert alert-info" role="alert">
        ${loginMsg}
        ${sessionScope.loginMsg=null}
      </div>
    </c:if>
    <img src="img/avatar.svg" alt="" class="avatar">
    <h2>Welcome</h2>
    <div class="input-group">
      <div class="icon">
        <i class="fa fa-user"></i>
      </div>
      <div>

        <h5>Username</h5>
        <input type="text" id="inputEmail" class="input" name="username" required="" autofocus="">
      </div>
    </div>
    <div class="input-group">
      <div class="icon">
        <i class="fa fa-lock"></i>
      </div>
      <div>

        <h5>Password</h5>
        <input type="password" id="inputPassword" class="input" name="password" required="">
      </div>
    </div>
    <a href="#">Forgot Password?</a>
        <button class="btn" type="submit">登录</button>
        <button class="btn" type="button" onclick="javascript:window.location.href='register.jsp';">注册</button>
      </form>
      

    </div> 


   
    <script src="js/ie10-viewport-bug-workaround.js"></script>
  

</body></html>
