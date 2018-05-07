package com.hc.action;

import java.util.List;

import org.apache.ibatis.session.SqlSession;

import com.entity.Login;
import com.hc.tools.DBHelp;
import com.hcl.dao.LoginDao;
import com.opensymphony.xwork2.ActionSupport;

public class LoginAction extends ActionSupport {

	private Login login;

	@Override
	public String execute() throws Exception {
		SqlSession session = DBHelp.getSqlSession();
		/*System.out.println(name+" "+pass);*/
		//System.out.println(login.getName()+" "+ login.getPass());
		List<Login> user = session.getMapper(LoginDao.class).findByExample(
				login.getName(), login.getPass());
		if (user.size() > 0) {//如果数据库里面存在数据，则登陆成功!
			System.out.println("我成功了！");
			return SUCCESS;
		} else {
			return ERROR;
		}
	}

	public Login getLogin() {
		return login;
	}

	public void setLogin(Login login) {
		this.login = login;
	}
	
}
