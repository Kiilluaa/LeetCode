public class WordAnalyzer {
    public static void main(String[] args) {
        String word = "java";

        System.out.println(word.length());
        System.out.println(word.charAt(0));
        System.out.println(word.charAt(3));
    }
}

// word.length()
// word.charAt(i)
// word.equals(other)
// word.substring(a,b)
// word.toLowerCase()

/* LOOP THROUGH EVERY CHARACTER
for(int i=0;i<word.length();i++){
    char letter = word.charAt(i);
    System.out.println(letter);
}
*/

/* COUNT A CHARACTER
public static int countA(String word){
    int count = 0;
    for(int i=0;i<word.length;i++){
        if(word.charAt(i) == 'a'){
            count++;
        }
    }
    return count;
}
*/

/* PRACTICE
1: 0
2: word.length() - 1
3: word.charAt(0)
4: word.charAt(word.length() - 1)
5: length() is a method call
6: for(int i=0;i<word.length();i++)
7: int count = 0; for(int i=0;i<word.length;i++){if(word.charAt(i) == 'a'){count++;}} return count;
8: 
int count = 0;
for(int i=0;i<word.length;i++){
    if(word.charAt(i) == 'a' || word.charAt(i) == 'e' || word.charAt(i) == 'i' || word.charAt(i) == 'o' || word.charAt(i) == 'u'){
        count++;
    }
}
return count;
9: if(word.charAt(i) == ' '){
        return true;
   }
   return false;
10: word.equals(other)
11: `==` compares references for objects; `equals` compares String contents.
12: 
public static String firstChar(String text){
    return text.charAt(0);
}
13:
public static char lastChar(String text){
    return text.charAt(text.length() - 1);
}
14:
public static int countLetter(String text, char target){
    count = 0;
    for(int i=0;i<text.length;i++){
        if(text.charAt(i) == target){
            count++;
        }
    }
    return count;
}
15: 2 because you need the string input and what you want to count
16:
for(int i=word.length()-1;i>=0;i--){
    System.out.println(word.charAt(i));
}
17:
if(word.length()==0){
    return true;
}
return false;

or

return word.length()==0;
*/