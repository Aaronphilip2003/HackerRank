public class HelloWorld{

     public static void main(String []args)
     {
      String s3="";
      String s="07:05:45AM" ;
      int length=s.length();
      String last=s.substring(s.length()-2);
      if (last.equalsIgnoreCase("AM"))
        {
           s3=s.substring(0,length-2);
           System.out.println(s3);
        }
        else if (last.equalsIgnoreCase("PM"))
        {
            int index=s.indexOf(":");
            String s2=s.substring(0,2);
            int s2_int=Integer.parseInt(s2);
            s2_int=s2_int+12;
            s3=s2_int+s.substring(index,length-2);
            System.out.println(s3);
            
        }

     }
}
