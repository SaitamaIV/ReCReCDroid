package commander;

//描述语义相似度的类
public class Similarity {
	private String SimID;
	private String SentenceWord;//文本描述中的词语，会与GUI组件进行语义匹配
	private String ResultWord;//真实的GUI组件
	public String getSimID() {
		return SimID;
	}
	public void setSimID(String simID) {
		SimID = simID;
	}
	public String getSentenceWord() {
		return SentenceWord;
	}
	public void setSentenceWord(String sentenceWord) {
		SentenceWord = sentenceWord;
	}
	public String getResultWord() {
		return ResultWord;
	}
	public void setResultWord(String resultWord) {
		ResultWord = resultWord;
	}
}
