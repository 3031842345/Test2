package com.hc.tools;

import java.io.IOException;
import java.io.InputStream;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

public class DBHelp {
	
	public static SqlSession getSqlSession()
	{
		SqlSession session=null;
		try{
			InputStream input=Resources.getResourceAsStream("mybatis_config.xml");
			SqlSessionFactory factory=new SqlSessionFactoryBuilder().build(input);
			session=factory.openSession(false);
		}catch(IOException e){
			e.printStackTrace();	
		}
		return session;
	}
	public static void closeSqlSession(SqlSession session){
		if(session!=null){
			session.close();
		}
	}
}
