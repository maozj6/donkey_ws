This is for donkey car and ROS2


## Structre

Design 2 nodes:

1.pubish_node: get images from camera and pulish them

2. give_node: receive images from pubish_node and process images to get instructions(steering/gas/brake)

## TODO

1. connect camera with pubish_node and publish images

2. embend neural network into give_node to give instructions 

3.(optional) 2 nodes are enough, the give_node can directly give instructions to the donkey car or build the 3rd node to receive instructions and deliver them to the car indirectly



pkg_name=donkey_project

## Compile



colcon build



## Run

source install/setup.bash

ros2 run donkey_project pub_node

ros2 run donkey_project give_node


ros2 topic list

ros2 node info /$node_name


## DIR tree

jetson@nano:~/donkey_ws$ tree
.
├── build
│   ├── COLCON_IGNORE
│   └── donkey_project
│       ├── build
│       │   └── lib
│       │       └── donkey_project
│       │           ├── gi.py
│       │           ├── __init__.py
│       │           └── pub.py
│       ├── colcon_build.rc
│       ├── colcon_command_prefix_setup_py.sh
│       ├── colcon_command_prefix_setup_py.sh.env
│       ├── donkey_project.egg-info
│       │   ├── dependency_links.txt
│       │   ├── entry_points.txt
│       │   ├── PKG-INFO
│       │   ├── requires.txt
│       │   ├── SOURCES.txt
│       │   ├── top_level.txt
│       │   └── zip-safe
│       ├── install.log
│       └── prefix_override
│           ├── __pycache__
│           │   └── sitecustomize.cpython-38.pyc
│           └── sitecustomize.py
├── install
│   ├── COLCON_IGNORE
│   ├── donkey_project
│   │   ├── lib
│   │   │   ├── donkey_project
│   │   │   │   ├── give_node
│   │   │   │   ├── give_node=donkey_project.gi:mainpub_node
│   │   │   │   └── pub_node
│   │   │   └── python3.8
│   │   │       └── site-packages
│   │   │           ├── donkey_project
│   │   │           │   ├── gi.py
│   │   │           │   ├── __init__.py
│   │   │           │   ├── pub.py
│   │   │           │   └── __pycache__
│   │   │           │       ├── gi.cpython-38.pyc
│   │   │           │       ├── __init__.cpython-38.pyc
│   │   │           │       └── pub.cpython-38.pyc
│   │   │           └── donkey_project-0.0.0-py3.8.egg-info
│   │   │               ├── dependency_links.txt
│   │   │               ├── entry_points.txt
│   │   │               ├── PKG-INFO
│   │   │               ├── requires.txt
│   │   │               ├── SOURCES.txt
│   │   │               ├── top_level.txt
│   │   │               └── zip-safe
│   │   └── share
│   │       ├── ament_index
│   │       │   └── resource_index
│   │       │       └── packages
│   │       │           └── donkey_project
│   │       ├── colcon-core
│   │       │   └── packages
│   │       │       └── donkey_project
│   │       └── donkey_project
│   │           ├── hook
│   │           │   ├── ament_prefix_path.dsv
│   │           │   ├── ament_prefix_path.ps1
│   │           │   ├── ament_prefix_path.sh
│   │           │   ├── pythonpath.dsv
│   │           │   ├── pythonpath.ps1
│   │           │   └── pythonpath.sh
│   │           ├── package.bash
│   │           ├── package.dsv
│   │           ├── package.ps1
│   │           ├── package.sh
│   │           ├── package.xml
│   │           └── package.zsh
│   ├── local_setup.bash
│   ├── local_setup.ps1
│   ├── local_setup.sh
│   ├── _local_setup_util_ps1.py
│   ├── _local_setup_util_sh.py
│   ├── local_setup.zsh
│   ├── setup.bash
│   ├── setup.ps1
│   ├── setup.sh
│   └── setup.zsh
├── log
│   ├── build_2023-04-18_04-26-47
│   │   ├── donkey_project
│   │   │   ├── command.log
│   │   │   ├── stderr.log
│   │   │   ├── stdout.log
│   │   │   ├── stdout_stderr.log
│   │   │   └── streams.log
│   │   ├── events.log
│   │   └── logger_all.log
│   ├── build_2023-04-18_04-29-00
│   │   ├── donkey_project
│   │   │   ├── command.log
│   │   │   ├── stderr.log
│   │   │   ├── stdout.log
│   │   │   ├── stdout_stderr.log
│   │   │   └── streams.log
│   │   ├── events.log
│   │   └── logger_all.log
│   ├── build_2023-04-18_04-52-37
│   │   ├── donkey_project
│   │   │   ├── command.log
│   │   │   ├── stderr.log
│   │   │   ├── stdout.log
│   │   │   ├── stdout_stderr.log
│   │   │   └── streams.log
│   │   ├── events.log
│   │   └── logger_all.log
│   ├── build_2023-04-18_04-53-26
│   │   ├── donkey_project
│   │   │   ├── command.log
│   │   │   ├── stderr.log
│   │   │   ├── stdout.log
│   │   │   ├── stdout_stderr.log
│   │   │   └── streams.log
│   │   ├── events.log
│   │   └── logger_all.log
│   ├── build_2023-04-18_04-54-09
│   │   ├── donkey_project
│   │   │   ├── command.log
│   │   │   ├── stderr.log
│   │   │   ├── stdout.log
│   │   │   ├── stdout_stderr.log
│   │   │   └── streams.log
│   │   ├── events.log
│   │   └── logger_all.log
│   ├── build_2023-04-18_04-54-45
│   │   ├── donkey_project
│   │   │   ├── command.log
│   │   │   ├── stderr.log
│   │   │   ├── stdout.log
│   │   │   ├── stdout_stderr.log
│   │   │   └── streams.log
│   │   ├── events.log
│   │   └── logger_all.log
│   ├── build_2023-04-18_04-55-14
│   │   ├── donkey_project
│   │   │   ├── command.log
│   │   │   ├── stderr.log
│   │   │   ├── stdout.log
│   │   │   ├── stdout_stderr.log
│   │   │   └── streams.log
│   │   ├── events.log
│   │   └── logger_all.log
│   ├── build_2023-04-18_05-04-45
│   │   ├── donkey_project
│   │   │   ├── command.log
│   │   │   ├── stderr.log
│   │   │   ├── stdout.log
│   │   │   ├── stdout_stderr.log
│   │   │   └── streams.log
│   │   ├── events.log
│   │   └── logger_all.log
│   ├── COLCON_IGNORE
│   ├── latest -> latest_build
│   └── latest_build -> build_2023-04-18_05-04-45
├── README.md
└── src
    └── donkey_project
        ├── donkey_project
        │   ├── gi.py
        │   ├── __init__.py
        │   └── pub.py
        ├── package.xml
        ├── resource
        │   └── donkey_project
        ├── setup.cfg
        ├── setup.py
        └── test
            ├── test_copyright.py
            ├── test_flake8.py
            └── test_pep257.py

49 directories, 126 files

## history command

colcon build --package-select donkey_project

ros2 pkg list | grep don


