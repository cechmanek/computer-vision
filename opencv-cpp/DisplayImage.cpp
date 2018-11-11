#include <stdio.h>
#include <opencv2/opencv.hpp>
//#include "C:\Users\GJ.Cechmanek\opencv\build\include\opencv2\core.hpp"


The reason I cannot make this work with gcc/g++ compiler is because g++ is 
using mingw and the opencv precompiled binaries i downloaded are meant for 
visual studio. To make opencv workable with g++ i have to build the libaries
from the source files using cmake, which may not be too difficult









using namespace cv;

int main(int argc, char** argv )
{
    if ( argc != 2 )
    {
        printf("usage: DisplayImage.out <Image_Path>\n");
        return -1;
    }
    Mat image;
    image = imread( argv[1], 1 );
    if ( !image.data )
    {
        printf("No image data \n");
        return -1;
    }
    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", image);
    waitKey(0);
    return 0;
}