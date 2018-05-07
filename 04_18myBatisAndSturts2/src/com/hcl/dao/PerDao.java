package com.hcl.dao;

import java.util.List;

import org.apache.ibatis.annotations.Param;

import com.entity.Per;

/**
 * 页面显示dao
 * @author 热枕
 *
 */
public interface PerDao {
	
	public List<Per> perShow(@Param("startPage") Integer a,@Param("endPage") Integer b);//显示人物列表
	
	public Integer pageCount();//显示总页数
	
	public void updatePer(Per pers);//更新人物
	
	public void insertPer(Per pers);//新增人物
	
	public void delPer(Integer id);//删除人物
	
}
