package com.hcl.dao;

import java.util.List;

import org.apache.ibatis.annotations.Param;

import com.entity.Login;

public interface LoginDao {

	public List<Login> findByExample(@Param("name") String name,
			@Param("pass") String pass);

}
