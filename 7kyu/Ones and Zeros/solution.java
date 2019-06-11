import java.util.List;

public class BinaryArrayToNumber {

  public static int ConvertBinaryArrayToInt(List<Integer> binary) {
            
    int multiplier = 0;
    int output = 0;
    
    for( int i = binary.size(); i > 0; i-- ){
      if( binary.get(i-1) == 1 ){ output += Math.pow(2,multiplier); }
      multiplier++;
    }
      
    return output;
  }
}