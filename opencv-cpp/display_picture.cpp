/*
ex 2.-1. a simple opencv program that loads an image from disk and displays it
on the screen
gjhc
2018 march 11
*/

//#include "stdafx.h"
#include <opencv2/opencv.hpp>

int main(int argc, char** argv) {
	cv::Mat img = cv::imread(argv[1], -1);

	if (img.empty()) return -1;

	cv::namedWindow("Example1", cv::WINDOW_AUTOSIZE);
	cv::imshow("Example1", img);
	cv::waitKey(0);
	cv::destroyWindow("Example1");


	return 0;
}