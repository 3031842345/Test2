package com.entity;

import java.util.Date;

/**
 * 实体类
 * @author 热枕
 *
 */
public class Per{
	
	private Integer id;//id
	
	private String name;//名字
	
	private String sex;//性别
	
	private String url;//url
	
	private String proFession;//职位
	
	private String introDuce;//简介
	
	private Date createdTime;//创建时间
	
	private Date updatedTime;//更新时间

	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getSex() {
		return sex;
	}

	public void setSex(String sex) {
		this.sex = sex;
	}

	public String getUrl() {
		return url;
	}

	public void setUrl(String url) {
		this.url = url;
	}

	public String getProFession() {
		return proFession;
	}

	public void setProFession(String proFession) {
		this.proFession = proFession;
	}

	public String getIntroDuce() {
		return introDuce;
	}

	public void setIntroDuce(String introDuce) {
		this.introDuce = introDuce;
	}

	public Date getCreatedTime() {
		return createdTime;
	}

	public void setCreatedTime(Date createdTime) {
		this.createdTime = createdTime;
	}

	public Date getUpdatedTime() {
		return updatedTime;
	}

	public void setUpdatedTime(Date updatedTime) {
		this.updatedTime = updatedTime;
	}
	
	

}
