#include <stdio.h>
#include <stdlib.h>

#define DEFAULTSIZE 100

void show(char* words,int size); 
char* morespace(char* words,int* maxsize);

int main() {
	
	//ͨ��malloc������ȡһ��ָ����ʽ���ַ����� 
	char* words = (char*)malloc(sizeof(char)*DEFAULTSIZE);
	
    int size = 0;//��¼�ַ�����Ŀǰ�洢�˶����ַ� 
    
    int maxsize = DEFAULTSIZE;//��¼Ŀǰ�ַ�����Ĵ�С
	 
    char ch;
    
    //���û�û��ʹ��EOF��������ʱ��������ѭ�� 
    while(scanf("%c",&ch) != -1){
    	//��������Ŀ����Ӣ�ķִʣ��˴�ֻ��Ӣ���ַ������ܳ��ֵ����ӷ��Լ��ո�ͻ��ж����ַ����� 
        if(ch == ' ' || (ch>=65&&ch<=122) || ch == '-' || ch == '\'' || ch == '\n'){
            words[size] = ch;
            ++size;
        }
        //ÿ����һ���ַ����ж�һ�������Ƿ����ˡ�����Ѿ����ˣ�����morespace���� 
        if(size == maxsize){
            words = morespace(words,&maxsize); 
        }
    }
    
    show(words,size);//������ 
    
    free(words);//�ͷ��ڴ� 
    
    return 0;
}

//����ִʽ����ÿ������һ�� 
void show(char* words,int size){
	
	int new_line = 0; //��¼�Ƿ��Ѿ������У��ɴ���������ж���Ŀ��� 
	
    for(int i = 0;i<size-1;++i){
        if(words[i] == ' ' || words[i] == '\n'){
        	//�����ǰ����ַ���û�л����У���ô������з��ָ��˵��� 
        	if(new_line == 0){
	            printf("\n");
	            new_line = 1;//������ֵ���Ϊ1 
	        }
        }
        //�����Ƿָ����ո���У���Ϊ���ʵ���ɲ��֣�������� 
        else{
            printf("%c",words[i]);
            new_line = 0;//��ʱΪһ�����ʵ��ַ�����������ǻ��д���Ϊ0 
        }
    }
}

//��ȡ����ռ���ַ����� 
char* morespace(char* words,int* maxsize){
	
	//ͨ��malloc�������һ��������ַ����� 
    char* new_words = (char*)malloc(sizeof(char)*(*maxsize+DEFAULTSIZE));
    
	//����ָ������޸�maxsize��ֵ 
    *maxsize = *maxsize + DEFAULTSIZE;
    
	//��ԭ���ַ���������ַ���������µ������� 
    for(int i = 0;i<*maxsize;++i){
        new_words[i] = words[i];
    }
    
	//�����µ��ַ����� 
    return new_words;
}

