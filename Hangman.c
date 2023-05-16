#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include<stdbool.h> 
#include <string.h>

#define MAX_LENGTH 1024
char *getRandomWord(FILE *f){
    char line[MAX_LENGTH];
    int n = 0, randLine;
    //count lines
    while (fgets(line, MAX_LENGTH, f)){
        n++;
    }
    srand(time(NULL));
    randLine = rand() % n;

    fseek(f, 0, SEEK_SET);

    int lineNum = 0;
    char *word = (char*)malloc(MAX_LENGTH * sizeof(char));
    while (fgets(line, MAX_LENGTH, f)){
        if (lineNum == randLine){
            strncpy(word, line, MAX_LENGTH);
            word[strlen(word)-1] = '\0'; //remove the newline character
            break;
        }
        lineNum++;
    }
    fclose(f);
    return word;
}
int getLen(char *word){
    return strlen(word);
}
int letterInWord(char letter, char *word){
    int n = 0;
    for (int i=0; i<strlen(word); i++){
        if (letter == word[i]){
            n++;
        }
    }
    return n;
}
void removeChar(char *lettersLeft, char letter){
    char *dst = lettersLeft;
    for (char *src = lettersLeft; *src != '\0'; src++) {
    *dst = *src;
        if (*dst != letter) {
            dst++;
        }
    
    }
    *dst = '\0';
}
void displeyChar(char *letters){
    for (int i=0; i<strlen(letters); i++){
        printf("%c ", letters[i]);
    }
    puts("");
}
bool letterAlreadyPicked(char character, char *letters){
    if (!strchr(letters, character)){
        return false;
    }
    return true;
}
void beginDrawing(int strikes){
    if (strikes == 0){
        puts("____________");
        puts("   |/      ");
        puts("   |");
        puts("   |");
        puts("   |");
        puts("   |");
        puts("   |");
        puts("   |");
        puts("  _|___");
    }
    else if (strikes == 1){
        puts("____________");
        puts("   |/      |");
        puts("   |      (_)");
        puts("   |");
        puts("   |");
        puts("   |");
        puts("   |");
        puts("   |");
        puts("  _|___");      
    }
    else if (strikes == 2){
        puts("____________");
        puts("   |/      |");
        puts("   |      (_)");
        puts("   |       |");
        puts("   |       |");
        puts("   |");
        puts("   |");
        puts("   |");
        puts("  _|___");      
    }
    else if (strikes == 3){
        puts("____________");
        puts("   |/      |");
        puts("   |      (_)");
        puts("   |      \\|");
        puts("   |       |");
        puts("   |");
        puts("   |");
        puts("   |");
        puts("  _|___");      
    }
    else if (strikes == 4){
        puts("____________");
        puts("   |/      |");
        puts("   |      (_)");
        puts("   |      \\|/");
        puts("   |       |");
        puts("   |");
        puts("   |");
        puts("   |");
        puts("  _|___");      
    }
    else if (strikes == 5){
        puts("____________");
        puts("   |/      |");
        puts("   |      (_)");
        puts("   |      \\|/");
        puts("   |       |");
        puts("   |      /");
        puts("   |");
        puts("   |");
        puts("  _|___");      
    }
    else if (strikes == 6){
        puts("____________");
        puts("   |/      |");
        puts("   |      (_)");
        puts("   |      \\|/");
        puts("   |       |");
        puts("   |      / \\");
        puts("   |");
        puts("   |");
        puts("  _|___");      
    }
}
int displayWord(char *word, char *guessedLetters){
    int numCorrect = strlen(guessedLetters);
    int n=0;
    
    for (int i = 0; i< strlen(word); i++){
        int change = 0;
        for (int j = 0; j < numCorrect; j++){

            if (word[i] == guessedLetters[j]){
                printf("%c ", word[i]);
                n++;
                change+=1;
            }
            
        }
        if (change != 1){
            printf("_ ");
        }
    }
    puts("");
    return n;
}
bool win(char *word, char numGuessed){
    if (strlen(word) == numGuessed){
        return true;
    }
    return false;
}
void displayChar(char *lettersLeft){
    for (int i = 0; i<strlen(lettersLeft); i++){
        printf("%c ", lettersLeft[i]);
    }
    puts("");
}


/*
  ____________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___
    */
int main(void){
    char lettersLeft[] = "abcdefghijklmnopqrstuvwxyz";
    char ch;
    char a;
    char file[] = "usa.txt";
    FILE *f = fopen(file, "r");
    if (!f){
        fprintf(stderr, "File cannot be opened");
    }
    char lettersGuessed[27] = "";
    char *word = getRandomWord(f);
    int numCorrect = 0;
    int strikes= 0;
    beginDrawing(0);
    puts("");
    puts("");
    numCorrect = displayWord(word, lettersGuessed);
    displayChar(lettersLeft);
    
    while (!win(word, numCorrect)){
        printf("Enter a character: ");
        ch = scanf("%c", &a);
        // eat newline char
        while (letterAlreadyPicked(ch, lettersGuessed)) // may break
        {
            printf("Enter a character: ");
            ch = getchar();
            
        }
        removeChar(lettersLeft, ch);// may break
        strcat(lettersGuessed, &ch);
        if (!letterInWord(ch, word)){
            strikes +=1;
        }
        if (strikes == 6){
            beginDrawing(strikes);
            printf("You lose, the word was %s\n", word);
            return 0;
        }
        else{
            beginDrawing(strikes);
            puts("");
            puts("");
            numCorrect = displayWord(word, lettersGuessed);
            displayChar(lettersLeft);
        }
        
    }
    puts("You got the word!");

}