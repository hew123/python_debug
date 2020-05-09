
import java.util.List;
import java.util.*;

public class Exercise {

    public static void main(String[] args){
        ArrayList<Integer> input = new ArrayList<Integer>();
        input.add(1);
        input.add(1);
        input.add(1);
        input.add(5);
        List<Integer> result = findDuplicates(input,3);
        System.out.println(result);
    }

    public static List<Integer> findDuplicates(List<Integer> integers, int numberOfDuplicates) {
        
        Map<Integer, Integer> table = new Hashtable<>();
        for(Integer item: integers){
            if(!(table.containsKey(item))){
                table.put(item,1);
            }else{
                Integer val = table.get(item);
                table.put(item,val+1);
            }
        }
        ArrayList<Integer> result = new ArrayList<Integer>();
        
        Set<Integer> keys = table.keySet();
        for(Integer key: keys){
            if(table.get(key)==numberOfDuplicates)
                result.add(key);
        }
        
        return result;
    }

}