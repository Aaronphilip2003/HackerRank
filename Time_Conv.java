import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'timeConversion' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */

    public static String timeConversion(String s) 
    {
      String s3="";
      int length=s.length();
      String last=s.substring(s.length()-2);
      String first=s.substring(0,2);
      boolean flag=false;
      if(first.equals("12"))
      {
          flag=true;
      }
      if (last.equalsIgnoreCase("AM")&& flag==false )
        {
           s3=s.substring(0,length-2);
        }
      else if(last.equalsIgnoreCase("AM")&& flag==true)  
      {
          int index=s.indexOf(":");
          s3="00"+s.substring(index,length-2);
      }
      else if (last.equalsIgnoreCase("PM")&& flag==false)
        {
            int index=s.indexOf(":");
            String s2=s.substring(0,2);
            int s2_int=Integer.parseInt(s2);
            s2_int=s2_int+12;
            s3=s2_int+s.substring(index,length-2);
        }
        else if(last.equalsIgnoreCase("PM")&& flag==true)
        {
            s3=s.substring(0,length-2);
        }
        return s3;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = bufferedReader.readLine();

        String result = Result.timeConversion(s);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
