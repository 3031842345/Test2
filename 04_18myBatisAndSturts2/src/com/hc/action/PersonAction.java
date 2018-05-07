package com.hc.action;

import java.util.List;

import javax.servlet.http.HttpServletRequest;

import org.apache.ibatis.session.SqlSession;
import org.apache.struts2.ServletActionContext;
import org.apache.struts2.util.ServletContextAware;

import com.entity.Per;
import com.hc.tools.DBHelp;
import com.hcl.dao.PerDao;
import com.opensymphony.xwork2.ActionContext;
import com.opensymphony.xwork2.ActionSupport;

public class PersonAction extends ActionSupport {
	HttpServletRequest request=ServletActionContext.getRequest();
	private Per per;
	private int count=0;
	public String select() throws Exception {
		    SqlSession ss=DBHelp.getSqlSession();
		    Integer sum=ss.getMapper(PerDao.class).pageCount();
		     request.getSession().setAttribute("sum", sum);
			List<Per> per=ss.getMapper(PerDao.class).perShow(count,3);
			request.getSession().setAttribute("Per", per);
			return SUCCESS;
	}
	
	public String update() throws Exception {
		SqlSession ss=DBHelp.getSqlSession();
		Per pe=per;
		System.out.println(pe.getId()+" "+pe.getName()+" "+pe.getProFession()+" "+pe.getSex());
		ss.getMapper(PerDao.class).updatePer(pe);
		ss.commit();
		return this.select();
	}
	
	public String insert() throws Exception {
		SqlSession ss=DBHelp.getSqlSession();
		Per pe=per;
		System.out.println(pe.getName()+" "+pe.getProFession()+" "+pe.getSex());
		ss.getMapper(PerDao.class).insertPer(pe);
		ss.commit();
		return this.select();
	}
	
	public String delete() throws Exception {
		SqlSession ss=DBHelp.getSqlSession();
		int id=Integer.parseInt(request.getParameter("id"));
		ss.getMapper(PerDao.class).delPer(id);
		ss.commit();
		return this.select();
	}
	
	
	public Per getPer() {
		return per;
	}

	public void setPer(Per per) {
		this.per = per;
	}

}
