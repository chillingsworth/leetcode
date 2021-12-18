bool isValid(char * s){
    int paren = 0;
    int square = 0;
    int curly = 0;

    for(int i = 0; s[i]; i++)
        if (s[i] == '('){
            paren += 1;
        }
        else if (s[i] == ')'){
            paren -= 1;
        }
        else if (s[i] == '['){
            square += 1;
        }
        else if (s[i] == ']'){
            square -= 1;
        }
        else if (s[i] == '{'){
            curly += 1;
        }
        else if (s[i] == '}'){
            curly -= 1;
        }
    if (paren == 0 && square == 0 && curly == 0){
        return true;
    }
    else{
        return false;
    }
}