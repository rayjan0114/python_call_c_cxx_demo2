/*========================================================
    這是關於 python ctypes call C/C++ opencv 的範例

    會先從 python BGR uint8 numpy (H,W,3) <----> C++ cv::Mat

======================================*/

#include <cstdlib>
#include <iostream>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc/types_c.h>
#include <vector>

//=====================================================================================================

extern "C" {

unsigned char* donothing( unsigned char* ptr, int H, int W ) {
    cv::Mat        img( H, W, CV_8UC3, ptr );
    unsigned char* buffer = ( unsigned char* )malloc( sizeof( unsigned char ) * H * W * 3 );
    memcpy( buffer, img.data, H * W * 3 );
    return buffer;
}

void release( unsigned char* data ) {
    std::cout << "release " << std::addressof( data ) << " !!" << std::endl;
    free( data );
}  // end_release
}  // end
