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
		if (user.size() > 0) {//������ݿ�����������ݣ����½�ɹ�!
			System.out.println("�ҳɹ��ˣ�");
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
