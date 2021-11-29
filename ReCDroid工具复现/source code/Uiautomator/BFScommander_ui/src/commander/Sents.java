package commander;

import java.util.ArrayList;
import java.util.HashMap;

//记录GUI事件的自然语言描述的类
public class Sents {
	public int sentid;
	public ArrayList<String> sentswords;
	public ArrayList<String> nounlist;
	public HashMap<String,String> verbs;
	
	public HashMap<String, String> getVerbs() {
		return verbs;
	}

	public void setVerbs(HashMap<String, String> verbs) {
		this.verbs = verbs;
	}

	public Sents(){
		sentswords=new ArrayList<String>();
		nounlist=new ArrayList<String>();
		verbs=new HashMap<String,String>();
	}

	public int getSentid() {
		return sentid;
	}

	public void setSentid(int sentid) {
		this.sentid = sentid;
	}

	public ArrayList<String> getSentswords() {
		return sentswords;
	}

	public void setSentswords(ArrayList<String> sentswords) {
		this.sentswords = sentswords;
	}

	public ArrayList<String> getNounlist() {
		return nounlist;
	}

	public void setNounlist(ArrayList<String> nounlist) {
		this.nounlist = nounlist;
	}

}
