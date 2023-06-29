# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_point_cloud_processing_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED point_cloud_processing_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(point_cloud_processing_FOUND FALSE)
  elseif(NOT point_cloud_processing_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(point_cloud_processing_FOUND FALSE)
  endif()
  return()
endif()
set(_point_cloud_processing_CONFIG_INCLUDED TRUE)

# output package information
if(NOT point_cloud_processing_FIND_QUIETLY)
  message(STATUS "Found point_cloud_processing: 0.0.0 (${point_cloud_processing_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'point_cloud_processing' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${point_cloud_processing_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(point_cloud_processing_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${point_cloud_processing_DIR}/${_extra}")
endforeach()
