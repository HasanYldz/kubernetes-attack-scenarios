cmake_minimum_required(VERSION 3.5)
project(MyApp)

set(CMAKE_CXX_STANDARD 14)
find_package(Drogon CONFIG REQUIRED)
find_package(Boost REQUIRED COMPONENTS system filesystem)

include_directories(${Boost_INCLUDE_DIRS})
include_directories(${DROGON_INCLUDE_DIRS})

add_executable(myapp main.cpp)
target_link_libraries(myapp PRIVATE Drogon::Drogon ${Boost_LIBRARIES})

