<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>

	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
		<meta name="description" content="">
		<meta name="author" content="">
		<title>用户注册</title>
		<link href="css/register.css" rel="stylesheet">
		<script src="jsjquery.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
	</head>

	<body>
<img alt="" src="img/bg-2.png" class="wave">

<div class="container">

  <div class="img">
    <img alt="" src="img/img-4.svg">
  </div>
  <div class="login-box">
    <form method="post" action="servlet/AddUserServlet">

      <img src="img/avatar.svg" alt="" class="avatar">
      <h2>Register</h2>
      <div class="input-group">
        <div class="icon">
          <i class="fa fa-user"></i>
        </div>
        <div>

          <h5>Username</h5>
          <input type="text" id="focusedInput" class="input" name="username" >
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
      
      <div class="input-group">
        <div class="icon">
          <i class="fa fa-lock"></i>
        </div>
        <div>
          <h5>UserID</h5>
          <input type="text" id="focusedInput" class="input" name="id" >
        </div>
      </div>
      
      <div class="input-group">
        <div class="icon">
          <i class="fa fa-lock"></i>
        </div>
        <div>
          <h5>Nickname</h5>
          <input type="text" id="focusedInput" class="input" name="nickname" >
        </div>
      </div>

      <button class="btn" type="submit">提交</button>
      
    </form>


  </div>



  <script src="js/ie10-viewport-bug-workaround.js"></script>


</body>

</html>
