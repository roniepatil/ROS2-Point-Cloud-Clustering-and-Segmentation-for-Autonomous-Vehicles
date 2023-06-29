#include <iostream>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include <pcl/filters/voxel_grid.h>

int main(){
    // Read it into a pointer PCLPointCloud2, creating a shade pointer and allocating some memory
    pcl::PCLPointCloud2::Ptr cloud (new pcl::PCLPointCloud2());
    // class PCDReader reads the point cloud
    pcl::PCDReader cloud_reader;
    std::string path = "/home/rohit/pcl_ws/src/ROS2-Point-Cloud-Clustering-and-Segmentation-for-Autonomous-Behaviour/point_cloud_processing/point_clouds/table_scene.pcd";
    // Read the point cloud and put it into the created pointer
    cloud_reader.read(path,*cloud);
    // Print out number of points
    std::cout<<"Number of point "<< cloud->width * cloud->height << std::endl;
    return 0;
}
