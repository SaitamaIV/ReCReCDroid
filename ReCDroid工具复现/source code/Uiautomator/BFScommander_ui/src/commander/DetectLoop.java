package commander;

import java.util.ArrayList;

//该类用于检测循环和等效屏幕
public class DetectLoop {

	public DetectLoop(ArrayList<String> possibleLoop, int currentPoint, ArrayList<ArrayList<String>> allArivalSimilarList) {
		this.possibleLoop=possibleLoop;//疑似循环体的序列
		this.currentPoint=currentPoint;//本轮迭代的节点
		this.allArivalSimilarList=allArivalSimilarList;
		// TODO Auto-generated constructor stub
	}
	public ArrayList<String> possibleLoop=new ArrayList<String>();
	public ArrayList<ArrayList<String>> allArivalSimilarList=new ArrayList<ArrayList<String>>();
	public int currentPoint;
	public int looptimes=1;
	
	public ArrayList<String> getPossibleLoop() {
		return possibleLoop;
	}
	public void setPossibleLoop(ArrayList<String> possibleLoop) {
		this.possibleLoop = possibleLoop;
	}
	public int getCurrentPoint() {
		return currentPoint;
	}
	public void setCurrentPoint(int currentPoint) {
		this.currentPoint = currentPoint;
	}
	public int getLooptimes() {
		return looptimes;
	}
	public void setLooptimes(int looptimes) {
		this.looptimes = looptimes;
	}
	public ArrayList<ArrayList<String>> getAllArivalSimilarList() {
		return allArivalSimilarList;
	}
	public void setAllArivalSimilarList(
			ArrayList<ArrayList<String>> allArivalSimilarList) {
		this.allArivalSimilarList = allArivalSimilarList;
	}
}
