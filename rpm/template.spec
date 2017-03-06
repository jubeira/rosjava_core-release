Name:           ros-indigo-rosjava-core
Version:        0.2.2
Release:        0%{?dist}
Summary:        ROS rosjava_core package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://ros.org/wiki/rosjava_core
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-rosgraph-msgs
BuildRequires:  ros-indigo-rosjava-bootstrap
BuildRequires:  ros-indigo-rosjava-build-tools
BuildRequires:  ros-indigo-rosjava-messages
BuildRequires:  ros-indigo-rosjava-test-msgs
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-tf2-msgs

%description
An implementation of ROS in pure-Java with Android support.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Mar 06 2017 Damon Kohler <damonkohler@google.com> - 0.2.2-0
- Autogenerated by Bloom

* Wed Feb 25 2015 Damon Kohler <damonkohler@google.com> - 0.2.1-0
- Autogenerated by Bloom

