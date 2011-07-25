%define gcj_support 1
Name:		pdftk
Version:	1.44
Release:	4
Summary:	PDF Tool Kit
License:	GPLv2+
Group:		Publishing
URL:		http://www.pdfhacks.com/pdftk/
Source0:	http://www.pdfhacks.com/pdftk/%{name}-%{version}-src.zip
Patch0:		pdftk-1.44-makefile-fix.patch
BuildRequires:	java-devel-gcj
BuildRequires:	libgcj-devel
BuildRequires:	unzip
BuildRequires:	fastjar
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
Requires:	bouncycastle

%description
Pdftk is a simple tool for doing everyday things with PDF documents.
Keep one in the top drawer of your desktop and use it to:
- Merge PDF Documents
- Split PDF Pages into a New Document
- Decrypt Input as Necessary (Password Required)
- Encrypt Output as Desired
- Fill PDF Forms with FDF Data and/or Flatten Forms
- Apply a Background Watermark
- Report on PDF Metrics, including Metadata and Bookmarks
- Update PDF Metadata
- Attach Files to PDF Pages or the PDF Document
- Unpack PDF Attachments
- Burst a PDF Document into Single Pages
- Uncompress and Re-Compress Page Streams
- Repair Corrupted PDF (Where Possible)

%prep
%setup -q -n %{name}-%{version}-dist
%patch0 -p0 -b .makefix

%{__perl} -pi -e "s/\r$//g" pdftk.1.txt

%{__rm} -r java/gnu_local java/java_local
dos2unix changelog.txt

%build
pushd pdftk
GCJFLAGS="%{optflags} -I`pwd`/../java -Wno-all" %{__make} -f Makefile.Redhat
popd

%install
%{__rm} -rf %{buildroot}

%{__mkdir_p} %{buildroot}%{_bindir}
%{__cp} -a pdftk/pdftk %{buildroot}%{_bindir}/pdftk

%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__cp} -a pdftk.1 %{buildroot}%{_mandir}/man1/pdftk.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc pdftk.1.html pdftk.1.txt changelog.txt
%attr(0755,root,root) %{_bindir}/pdftk
%{_mandir}/man1/pdftk.1*
