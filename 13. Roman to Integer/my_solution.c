int romanToInt(char * s){
    int i=0;
    int counter=0;
    while (i<strlen(s)){
        printf("Iterator %d", i);
        printf("\n %d ", s[i]);
        if (s[i] == 73){
            if (s[i+1] == 86){
                counter+=4;
                i+=2;
            }
            else if (s[i+1] == 88){
                counter+=9;
                i+=2;
            }
            else{
                printf("\n %s ", "I");
                counter++;
                i++;
            }
        }
        else if (s[i] == 86){
            printf("%s ", "V");
            counter+=5;
            i++;
        } 
        else if (s[i] == 88){
            if (s[i+1] == 76){
                printf("\n %s ", "XL");
                counter+=40;
                i+=2;
            }
            else if (s[i+1] == 67){
                printf("\n %s ", "XC");
                counter+=90;
                i+=2;
            }
            else{
                printf("\n %s ", "X");
                counter+=10;
                i++;
            }
        } 
        else if (s[i] == 76){
            printf("%s ", "L");
            counter+=50;
            i++;
        } 
        else if (s[i] == 67){
            if (s[i+1] == 68){
                printf("\n %s ", "CD");
                counter+=400;
                i+=2;
            }
            else if (s[i+1] == 77){
                printf("\n %s ", "CM");
                counter+=900;
                i+=2;
            }
            else{
                printf("%s ", "C");
                counter+=100;
                i++;
            }
        } 
        else if (s[i] == 68){
            printf("%s ", "D");
            counter+=500;
            i++;
        } 
        else if (s[i] == 77){
            printf("%s ", "M");
            counter+=1000;
            i++;
        } 
    }
    return counter;
}