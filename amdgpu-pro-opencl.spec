#No debug file
%global debug_package %{nil}

Name:           amdgpu-pro-opencl
Version:        16.30.3
Release:        315407
License:        AMD EULA
URL:            http://www.amd.com
Source0:        https://www2.ati.com/drivers/linux/amdgpu-pro_%{version}-%{release}.tar.xz
ExclusiveArch:  x86_64

Summary:        AMDGPU-PRO OpenCL ICD library

%description
This is the OpenCL ICD library from AMDGPU-PRO.

OpenCL (Open Computing Language) is a multivendor open standard for
general-purpose parallel programming of heterogeneous systems that include
CPUs, GPUs and other processors.

%prep
%setup -q -n amdgpu-pro-driver

%build
#no build

%install
#For libdrm_amdgpu.so
mkdir libdrm-amdgpu-pro-amdgpu1_%{version}-%{release}_amd64
cd libdrm-amdgpu-pro-amdgpu1_%{version}-%{release}_amd64
ar x ../libdrm-amdgpu-pro-amdgpu1_%{version}-%{release}_amd64.deb
tar -C . -xf data.tar.xz
install -D usr/lib/x86_64-linux-gnu/amdgpu-pro/libdrm_amdgpu.so.1.0.0 %{buildroot}%{_libdir}/%{name}/libdrm_amdgpo.so.1.0.0
cd ..

#For libamdocl*64.so and amdocl64.icd
mkdir amdgpu-opencl-icd_%{version}-%{release}_amd64
cd amdgpu-opencl-icd_%{version}-%{release}_amd64
ar x ../amdgpu-pro-opencl-icd_%{version}-%{release}_amd64.deb
tar -C . -xf data.tar.xz
sed -i "s|libdrm_amdgpu|libdrm_amdgpo|g" usr/lib/x86_64-linux-gnu/amdgpu-pro/libamdocl64.so
install -D usr/lib/x86_64-linux-gnu/amdgpu-pro/libamdocl*64.so %{buildroot}%{_libdir}/%{name}/
cp -r etc %{buildroot}

ln -s libdrm_amdgpo.so.1.0.0 %{buildroot}%{_libdir}/%{name}/libdrm_amdgpo.so.1
ln -s libamdocl64.so %{buildroot}%{_libdir}/%{name}/libOpenCL.so
ln -s libamdocl64.so %{buildroot}%{_libdir}/%{name}/libOpenCL.so.1
ln -s libamdocl64.so %{buildroot}%{_libdir}/%{name}/libOpenCL.so.1.0.0

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%config(noreplace) %{_sysconfdir}/OpenCL/vendors/amdocl*.icd
%{_libdir}/%{name}

%changelog
