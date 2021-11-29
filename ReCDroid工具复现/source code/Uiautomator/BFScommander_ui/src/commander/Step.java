package commander;

import java.util.ArrayList;

//记录被nlp解析后的GUI事件描述的类
public class Step {
	public String type;
	public String step;
	public ArrayList<ArrayList<String>> clickwhere;
	public String clicktype;
	public boolean clicktimes;
	public ArrayList<ArrayList<String>> typewhat;
	public ArrayList<ArrayList<String>> digittypewhat;
	public ArrayList<ArrayList<String>> typewhere;
	public ArrayList<ArrayList<String>> digittypewhere;
	public boolean typetimes;
	public ArrayList<ArrayList<String>> createwhat;
	public ArrayList<String> sentence;
	public int sentenceid;//sentenceid是该句子在报告中的出现顺序，将会在SortRules中会使用

	public Step(){
		clickwhere=new ArrayList<ArrayList<String>>();
		typewhat=new ArrayList<ArrayList<String>>();
		digittypewhat=new ArrayList<ArrayList<String>>();
		typewhere=new ArrayList<ArrayList<String>>();
		digittypewhere=new ArrayList<ArrayList<String>>();
		createwhat=new ArrayList<ArrayList<String>>();
		sentence=new ArrayList<String>();
	}



	public ArrayList<ArrayList<String>> getClickwhere() {
		return clickwhere;
	}



	public void setClickwhere(ArrayList<ArrayList<String>> clickwhere) {
		this.clickwhere = clickwhere;
	}



	public ArrayList<ArrayList<String>> getTypewhat() {
		return typewhat;
	}



	public void setTypewhat(ArrayList<ArrayList<String>> typewhat) {
		this.typewhat = typewhat;
	}



	public ArrayList<ArrayList<String>> getDigittypewhat() {
		return digittypewhat;
	}



	public void setDigittypewhat(ArrayList<ArrayList<String>> digittypewhat) {
		this.digittypewhat = digittypewhat;
	}



	public ArrayList<ArrayList<String>> getTypewhere() {
		return typewhere;
	}



	public void setTypewhere(ArrayList<ArrayList<String>> typewhere) {
		this.typewhere = typewhere;
	}



	public ArrayList<ArrayList<String>> getDigittypewhere() {
		return digittypewhere;
	}



	public void setDigittypewhere(ArrayList<ArrayList<String>> digittypewhere) {
		this.digittypewhere = digittypewhere;
	}



	public ArrayList<ArrayList<String>> getCreatewhat() {
		return createwhat;
	}



	public void setCreatewhat(ArrayList<ArrayList<String>> createwhat) {
		this.createwhat = createwhat;
	}



	public String getType() {
		return type;
	}



	public void setType(String type) {
		this.type = type;
	}



	public String getStep() {
		return step;
	}



	public void setStep(String step) {
		this.step = step;
	}




	public String getClicktype() {
		return clicktype;
	}



	public void setClicktype(String clicktype) {
		this.clicktype = clicktype;
	}



	public boolean isClicktimes() {
		return clicktimes;
	}


	public void setClicktimes(boolean clicktimes) {
		this.clicktimes = clicktimes;
	}



	public boolean isTypetimes() {
		return typetimes;
	}



	public void setTypetimes(boolean typetimes) {
		this.typetimes = typetimes;
	}




	public ArrayList<String> getSentence() {
		return sentence;
	}



	public void setSentence(ArrayList<String> sentence) {
		this.sentence = sentence;
	}



	public int getSentenceid() {
		return sentenceid;
	}



	public void setSentenceid(int sentenceid) {
		this.sentenceid = sentenceid;
	}
	
	
}
