package com.hcl.dao;

import java.util.List;

import org.apache.ibatis.annotations.Param;

import com.entity.Per;

/**
 * ҳ����ʾdao
 * @author ����
 *
 */
public interface PerDao {
	
	public List<Per> perShow(@Param("startPage") Integer a,@Param("endPage") Integer b);//��ʾ�����б�
	
	public Integer pageCount();//��ʾ��ҳ��
	
	public void updatePer(Per pers);//��������
	
	public void insertPer(Per pers);//��������
	
	public void delPer(Integer id);//ɾ������
	
}
