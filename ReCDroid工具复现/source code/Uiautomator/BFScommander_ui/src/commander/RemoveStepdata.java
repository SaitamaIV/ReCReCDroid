package commander;

import java.util.ArrayList;

public class RemoveStepdata {

public int generationpass=0;
public ArrayList<Integer> children=new ArrayList<Integer>();//记录子节点
public ArrayList<Integer> gradChildren=new ArrayList<Integer>();//记录子孙节点

public ArrayList<ArrayList<Integer>> descendant= new ArrayList<ArrayList<Integer>>();//second arralist is for the classid collected.

public RemoveStepdata(int level){
	for (int i=0; i<=level; i++){
		descendant.add(new ArrayList<Integer>());//获得所有子孙节点
	}
}

public int getGenerationpass() {
	return generationpass;
}
public void setGenerationpass(int generationpass) {
	this.generationpass = generationpass;
}
public ArrayList<Integer> getChildren() {
	return children;
}
public void setChildren(ArrayList<Integer> children) {
	this.children = children;
}
public ArrayList<Integer> getGradChildren() {
	return gradChildren;
}
public void setGradChildren(ArrayList<Integer> gradChildren) {
	this.gradChildren = gradChildren;
}
public ArrayList<ArrayList<Integer>> getDescendant() {
	return descendant;
}
public void setDescendant(ArrayList<ArrayList<Integer>> descendant) {
	this.descendant = descendant;
}

}
