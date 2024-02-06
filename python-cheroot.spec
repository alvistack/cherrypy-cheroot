# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-cheroot
Epoch: 100
Version: 10.0.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Highly-optimized, pure-python HTTP server
License: BSD-3-Clause
URL: https://github.com/cherrypy/cheroot/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Cheroot is the high-performance, pure-Python HTTP server used by
CherryPy.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-cheroot
Summary: Highly-optimized, pure-python HTTP server
Requires: python3
Requires: python3-importlib-metadata
Requires: python3-jaraco.collections
Requires: python3-more-itertools >= 2.6
Requires: python3-six >= 1.11.0
Provides: python3-cheroot = %{epoch}:%{version}-%{release}
Provides: python3dist(cheroot) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cheroot = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cheroot) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cheroot = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cheroot) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-cheroot
Cheroot is the high-performance, pure-Python HTTP server used by
CherryPy.

%files -n python%{python3_version_nodots}-cheroot
%license LICENSE.md
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-cheroot
Summary: Highly-optimized, pure-python HTTP server
Requires: python3
Requires: python3-importlib-metadata
Requires: python3-jaraco.collections
Requires: python3-more-itertools >= 2.6
Requires: python3-six >= 1.11.0
Provides: python3-cheroot = %{epoch}:%{version}-%{release}
Provides: python3dist(cheroot) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cheroot = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cheroot) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cheroot = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cheroot) = %{epoch}:%{version}-%{release}

%description -n python3-cheroot
Cheroot is the high-performance, pure-Python HTTP server used by
CherryPy.

%files -n python3-cheroot
%license LICENSE.md
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-cheroot
Summary: Highly-optimized, pure-python HTTP server
Requires: python3
Requires: python3-importlib-metadata
Requires: python3-jaraco-collections
Requires: python3-more-itertools >= 2.6
Requires: python3-six >= 1.11.0
Provides: python3-cheroot = %{epoch}:%{version}-%{release}
Provides: python3dist(cheroot) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cheroot = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cheroot) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cheroot = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cheroot) = %{epoch}:%{version}-%{release}

%description -n python3-cheroot
Cheroot is the high-performance, pure-Python HTTP server used by
CherryPy.

%files -n python3-cheroot
%license LICENSE.md
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
