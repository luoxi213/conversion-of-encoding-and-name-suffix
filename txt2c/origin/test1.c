#include <iostream>  
#include <fcntl.h>  
#include <sys/types.h>  
#include <sys/stat.h>  
#include <unistd.h>  
using namespace std;  
  
int main(int argc, char *argv[])  
{  
    if(access(argv[1], F_OK) != 0)  
    {  
    cout << "file not found......" << endl;  
    return 0;  
    }  
  
    int fin = open(argv[1], O_RDONLY, 0777);  
    int fout = open(argv[2], O_WRONLY|O_CREAT, 0777);  
  
    char buff[1024] = {'\0'};  
    int len = 0;  
    while((len = read(fin, buff, sizeof(buff))) > 0)  
    {  
    write(fout, buff, len);  
    }  
  
    close(fin);  
    close(fout);  
  
    return 0;  
}  