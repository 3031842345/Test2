<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%
	String path = request.getContextPath();
	String basePath = request.getScheme() + "://"
			+ request.getServerName() + ":" + request.getServerPort()
			+ path + "/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<base href="<%=basePath%>">

<title>My JSP 'index.jsp' starting page</title>
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="cache-control" content="no-cache">
<meta http-equiv="expires" content="0">
<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
<meta http-equiv="description" content="This is my page">
<!--
	<link rel="stylesheet" type="text/css" href="styles.css">
	-->
</head>

<body>
	<h1>欢迎您登陆成功！</h1>
	<table>
		<thead>
			<tr>
				<td>id</td>
				<td>姓名</td>
				<td>性别</td>
				<td>职业</td>
			</tr>
		</thead>
		<tbody>
			<c:forEach items="${sessionScope.Per }" var="per">
				<tr>
					<td>${per.id}</td>
					<td>${per.name}</td>
					<td><c:choose>
							<c:when test="${per.sex}==1">
        		男
        	</c:when>
							<c:otherwise>
        		女
         	</c:otherwise>
						</c:choose></td>
					<td>${per.proFession}</td>
					<td><input type="button" name="update" value="修改"
						onclick="javaScript:location='/04_18myBatisAndSturts2/Update.jsp?id='+${per.id}">
					</td>
					<td><input type="button" name="delete" value="删除"
						onclick="javaScript:location='/04_18myBatisAndSturts2/Person!delete.action?id='+${per.id}">
					</td>
				</tr>
			</c:forEach>
			<tr>
				<td colspan="6" align="center"><a
					href="/04_18myBatisAndSturts2/Person!insert.action">增加商品</a>
				</td>
			</tr>
		</tbody>
		<tfoot>
		<c:if test="${sessionScope.count==null }">
			
		</c:if>
		<tr><td><input type="button" value="首页" onclick="javaScript:location='/04_17HibernateAndMyBatis/goodsAction.do?ope=PageShow&pageOpr=0'"></td>
		<td><input type="button" value="上一页" onclick="javaScript:location='/04_17HibernateAndMyBatis/goodsAction.do?ope=PageShow&pageOpr=up'"></td>
		<td><input type="button" value="下一页" onclick="javaScript:location='/04_17HibernateAndMyBatis/goodsAction.do?ope=PageShow&pageOpr=down'"></td>
		<td><input type="button" value="末页" onclick="javaScript:location='/04_17HibernateAndMyBatis/goodsAction.do?ope=PageShow&pageOpr=${sessionScope.sum}'"></td>
		<td>
			<c:if test="${sessionScope.sum}!=null">
				${sessionScope.count }/${sessionScope.sum}
			</c:if>
		</td>
		</tr>
		</tfoot>
	</table>
</body>
</html>
