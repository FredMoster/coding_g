// STRING PARSING

import java.util.*;
import java.io.*;
import java.math.*;

class Solution {

    final static String INDENT = "    ";

    public static String indented(String c, int currIndent) {
        String output = "";
        for (int i = 0; i<currIndent; i++) {
            output += INDENT;
        }
        return output+c;
    }


    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        if (in.hasNextLine()) in.nextLine();

        // Build
        List<String> fullCGX = new ArrayList<>();
        String currString = "";
        String currPrimitive = "";
        for (int i = 0; i < N; i++) {
            String cGXLine = in.nextLine();

            for (char c : cGXLine.trim().toCharArray()) {
                if ((currString.isEmpty() && c == '\'') || (!currString.isEmpty() && c != '\'')) {
                    currString += c;
                } else if (!currString.isEmpty() && c == '\'') {
                    currString += c;
                    fullCGX.add(currString);
                    currString = "";
                } else if (c == '(' || c == ')' || c == ';' || c == '=') {
                    if (!currPrimitive.isEmpty()) {
                        fullCGX.add(currPrimitive);
                        currPrimitive = "";
                    }
                    fullCGX.add(""+c);
                } else if (c != ' ' && c != '\t') {
                    currPrimitive += c;
                }
            }
        }
        if (!currPrimitive.isEmpty()) fullCGX.add(currPrimitive);

        // Parse
        String output = "";
        int currIndent = 0;
        boolean indentNextChar = false;
        boolean newLineNextChar = false;
        String lastChar = ";";

        for (String currChar: fullCGX) {
            if (currChar.equals("(")) {
                if (!lastChar.equals(";")) output += "\n";
                output += indented(currChar, currIndent);
                currIndent += 1;
                indentNextChar = true;
                newLineNextChar = true;
            } else if (currChar.equals(")")) {
                currIndent -= 1;
                output += "\n" + indented(currChar, currIndent);
            } else if (currChar.equals(";")) {
                output += currChar + "\n";
                indentNextChar = true;
            } else if (currChar.equals(" ") || currChar.equals("\t")) {
                if (!lastChar.equals("=")) output += currChar;
            } else {
                if (newLineNextChar) output += "\n";
                if (indentNextChar) output += indented("", currIndent);
                output += currChar;
                indentNextChar = false;
                newLineNextChar = false;
            }
            lastChar = currChar;
        }

        System.out.println(output);
    }
}
